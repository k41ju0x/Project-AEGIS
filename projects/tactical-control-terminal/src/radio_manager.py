"""AEGIS v0.7: supervised, read-only Meshtastic USB connection."""

import logging
import threading
from datetime import datetime, timezone
from pathlib import Path

from pubsub import pub
from meshtastic.serial_interface import SerialInterface

LOG = logging.getLogger("aegis.radio")


class RadioManager:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = port
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.lost_event = threading.Event()
        self.thread = None
        self.interface = None

        self.state = {
            "connected": False,
            "connection_type": "usb_serial",
            "port": port,
            "node_count": 0,
            "packets_observed": 0,
            "last_event": None,
            "device_metrics": {},
            "error": None,
        }

    def snapshot(self):
        with self.lock:
            result = dict(self.state)
            result["device_metrics"] = dict(
                self.state["device_metrics"]
            )
            return result

    def _update(self, **changes):
        with self.lock:
            self.state.update(changes)

    def _on_receive(self, packet, interface):
        decoded = packet.get("decoded") or {}
        packet_type = decoded.get("portnum", "UNKNOWN")

        changes = {
            "last_event": {
                "type": str(packet_type),
                "timestamp": datetime.now(
                    timezone.utc
                ).isoformat(timespec="seconds"),
            }
        }

        if packet_type == "TELEMETRY_APP":
            telemetry = decoded.get("telemetry") or {}
            metrics = telemetry.get("deviceMetrics") or {}

            allowed = (
                "batteryLevel",
                "voltage",
                "uptimeSeconds",
                "channelUtilization",
                "airUtilTx",
            )
    
            new_metrics = {
                key: metrics[key]
                for key in allowed
                if key in metrics
            }

            if new_metrics:
                changes["device_metrics"] = new_metrics

        with self.lock:
            self.state["packets_observed"] += 1
            self.state.update(changes)

    def _on_lost(self, interface):
        self.lost_event.set()

    def start(self):
        if self.thread and self.thread.is_alive():
            return

        self.stop_event.clear()
        self.thread = threading.Thread(
            target=self._run,
            name="aegis-meshtastic",
            daemon=True,
        )
        self.thread.start()

    def _run(self):
        pub.subscribe(self._on_receive, "meshtastic.receive")
        pub.subscribe(
            self._on_lost,
            "meshtastic.connection.lost",
        )

        try:
            while not self.stop_event.is_set():
                self.lost_event.clear()

                if not Path(self.port).exists():
                    self._update(
                        connected=False,
                        error="Serial device unavailable",
                    )
                    self.stop_event.wait(5)
                    continue

                iface = None

                try:
                    LOG.info("Connecting to %s", self.port)
                    iface = SerialInterface(devPath=self.port)
                    self.interface = iface

                    self._update(
                        connected=True,
                        node_count=len(iface.nodes),
                        error=None,
                    )

                    LOG.info("Meshtastic connection established")

                    while not self.stop_event.wait(1):
                        if self.lost_event.is_set():
                            raise ConnectionError(
                                "Radio connection lost"
                            )

                        if not Path(self.port).exists():
                            raise ConnectionError(
                                "USB device disconnected"
                            )

                except Exception as exc:
                    self._update(
                        connected=False,
                        error=type(exc).__name__,
                    )
                    LOG.warning(
                        "Radio unavailable: %s",
                        type(exc).__name__,
                    )

                finally:
                    self._update(connected=False)

                    if iface is not None:
                        try:
                            iface.close()
                        except Exception:
                            LOG.warning(
                                "Serial close failed; retrying"
                            )

                    self.interface = None

                self.stop_event.wait(5)

        finally:
            pub.unsubscribe(
                self._on_receive,
                "meshtastic.receive",
            )
            pub.unsubscribe(
                self._on_lost,
                "meshtastic.connection.lost",
            )

    def stop(self):
        self.stop_event.set()
        self.lost_event.set()

        if self.thread:
            self.thread.join(timeout=5)


radio_manager = RadioManager()


if __name__ == "__main__":
    import json
    import time

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    radio_manager.start()

    try:
        for _ in range(30):
            time.sleep(1)

            if _ % 5 == 4:
                print(
                    json.dumps(
                        radio_manager.snapshot(),
                        indent=2,
                    ),
                    flush=True,
                )
    except KeyboardInterrupt:
        pass
    finally:
        radio_manager.stop()
        print("Radio test finished.")
