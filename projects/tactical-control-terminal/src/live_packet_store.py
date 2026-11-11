"""Safe, in-memory Meshtastic event history.

No message contents, coordinates, channel keys or node IDs
are retained in public-facing event records.
"""

from collections import deque
from datetime import datetime, timezone
from threading import Lock

_lock = Lock()
_events = deque(maxlen=200)
_sequence = 0


def record_packet(packet, interface):
    """Receive metadata through the existing serial session."""
    global _sequence

    try:
        decoded = packet.get("decoded") or {}
        portnum = str(decoded.get("portnum", "UNKNOWN"))

        types = {
            "TEXT_MESSAGE_APP": "TEXT",
            "POSITION_APP": "POSITION",
            "TELEMETRY_APP": "TELEMETRY",
        }
        event_type = types.get(
            portnum, portnum.removesuffix("_APP")
        )

        local_info = getattr(interface, "myInfo", None)
        local_number = getattr(
            local_info, "my_node_num", None
        )
        sender = packet.get("from")

        is_local = (
            local_number is not None
            and sender is not None
            and int(sender) == int(local_number)
        )

        # Never expose the numerical node identifier.
        source = (
            "AEGIS-MESH-01"
            if is_local else "OTHER-OR-UNKNOWN"
        )

        with _lock:
            _sequence += 1
            _events.append({
                "id": f"LIVE-{_sequence:08d}",
                "timestamp": datetime.now(
                    timezone.utc
                ).isoformat(timespec="seconds"),
                "source": source,
                "destination": "LOCAL-RADIO",
                "packet_type": event_type,
                "rssi_dbm": None,
                "snr_db": None,
                "message": None,
                "synthetic": False,
                "data_source": "meshtastic_serial",
                "origin": (
                    "local_node"
                    if is_local else "unverified"
                ),
            })
    except (AttributeError, TypeError, ValueError):
        # Malformed events must not interrupt radio handling.
        return


def get_live_events():
    with _lock:
        return list(reversed(_events))
