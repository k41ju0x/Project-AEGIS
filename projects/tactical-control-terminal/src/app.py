from flask import Flask, jsonify, render_template
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import glob
import socket
import shutil

from packet_store import get_events, load_synthetic_events
from radio_manager import radio_manager
from live_packet_store import record_packet, get_live_events
from pubsub import pub
import os

app = Flask(__name__)

def read_number(path, divisor=1):
    try:
        return float(Path(path).read_text().split()[0]) / divisor
    except (OSError, ValueError, ZeroDivisionError):
        return None

def cpu_temperature():
    value = read_number(
        "/sys/class/thermal/thermal_zone0/temp", 1000
    )
    return round(value, 1) if value is not None else None

def memory_usage():
    try:
        fields = {}
        with open("/proc/meminfo") as file:
            for line in file:
                key, value = line.split(":", 1)
                fields[key] = int(value.strip().split()[0])

        total = fields["MemTotal"]
        available = fields["MemAvailable"]
        used = total - available

        return {
            "total_mb": round(total / 1024),
            "used_mb": round(used / 1024),
            "percent": round(used / total * 100, 1)
        }
    except (OSError, ValueError, KeyError, ZeroDivisionError):
        return None

def storage_usage():
    try:
        usage = shutil.disk_usage("/")
        return {
            "total_gb": round(usage.total / (1024 ** 3), 1),
            "used_gb": round(usage.used / (1024 ** 3), 1),
            "percent": round(
                usage.used / usage.total * 100, 1
            )
        }
    except (OSError, ZeroDivisionError):
        return None

def system_uptime():
    value = read_number("/proc/uptime")
    return int(value) if value is not None else None

def fan_speed():
    for directory in Path("/sys/class/hwmon").glob("hwmon*"):
        try:
            name = (directory / "name").read_text().strip()
            if name == "pwmfan":
                rpm = read_number(directory / "fan1_input")
                return int(rpm) if rpm is not None else None
        except OSError:
            continue
    return None

def serial_candidates():
    ports = set()
    for pattern in ("/dev/ttyACM*", "/dev/ttyUSB*"):
        ports.update(glob.glob(pattern))
    return sorted(ports)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/status")
def status():
    radio = radio_manager.snapshot()
    return jsonify({
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(
            ZoneInfo("America/Chicago")
        ).isoformat(timespec="seconds"),
        "app_status": "online",
        "cpu_temp_c": cpu_temperature(),
        "memory": memory_usage(),
        "storage": storage_usage(),
        "uptime_seconds": system_uptime(),
        "fan_rpm": fan_speed(),
        "radio_status": "connected" if radio["connected"] else "not_connected",
        "radio": radio,
        "serial_candidates": serial_candidates(),
        "nodes": [],
        "node_data_status": "radio_connected" if radio["connected"] else "awaiting_radio"
    })


@app.get("/api/rf")
def rf_status():
    radio = radio_manager.snapshot()
    return jsonify({
        "radio_connected": radio["connected"],
        "connection_type": radio["connection_type"] if radio["connected"] else None,
        "radio_region": None,
        "modem_preset": None,
        "center_frequency_mhz": None,
        "frequency_slot": None,
        "packets_received": 0,
        "last_packet": None,
        "packets": [],
        "capture_active": False,
        "spectrum_available": False,
        "data_source": "local_meshtastic_events" if radio["connected"] else "no_radio_connected",
        "events_observed": radio["packets_observed"],
        "last_event": radio["last_event"],
        "device_metrics": radio["device_metrics"]
    })


@app.get("/api/packets")
def packet_events():
    events = get_events()
    return jsonify({
        "mode": "synthetic_test",
        "synthetic": True,
        "radio_connected": False,
        "count": len(events),
        "packets": events,
        "notice": "SYNTHETIC TEST DATA - NOT LIVE RF TRAFFIC"
    })



@app.get("/api/packets/live")
def live_packet_events():
    events = get_live_events()
    radio = radio_manager.snapshot()
    return jsonify({
        "mode": "live_local_events",
        "synthetic": False,
        "radio_connected": radio["connected"],
        "count": len(events),
        "packets": events,
        "notice": (
            "LIVE MESHTASTIC EVENTS - "
            "LOCAL NODE AND UNVERIFIED ORIGINS"
        ),
    })


if __name__ == "__main__":
    load_synthetic_events()
    pub.subscribe(record_packet, "meshtastic.receive")
    radio_manager.start()
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("AEGIS_HTTP_PORT", "5000")),
        debug=False,
        use_reloader=False
    )
