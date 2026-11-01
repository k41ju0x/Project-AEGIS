from flask import Flask, jsonify, render_template
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import glob
import socket
import shutil

from packet_store import get_events, load_synthetic_events

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
        "radio_status": "not_connected",
        "serial_candidates": serial_candidates(),
        "nodes": [],
        "node_data_status": "awaiting_radio"
    })


@app.get("/api/rf")
def rf_status():
    return jsonify({
        "radio_connected": False,
        "connection_type": None,
        "radio_region": None,
        "modem_preset": None,
        "center_frequency_mhz": None,
        "frequency_slot": None,
        "packets_received": 0,
        "last_packet": None,
        "packets": [],
        "capture_active": False,
        "spectrum_available": False,
        "data_source": "no_radio_connected"
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


if __name__ == "__main__":
    load_synthetic_events()
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
