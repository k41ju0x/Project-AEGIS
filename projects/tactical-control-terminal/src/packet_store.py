"""AEGIS packet event model and explicitly synthetic test data."""

from collections import deque
from datetime import datetime, timezone
from threading import Lock

MAX_EVENTS = 200

_events = deque(maxlen=MAX_EVENTS)
_lock = Lock()


def add_event(event):
    """Store a packet event in process memory only."""
    with _lock:
        _events.append(dict(event))


def get_events():
    """Return a snapshot of buffered events."""
    with _lock:
        return list(reversed(_events))


def clear_events():
    """Clear the in-memory event buffer."""
    with _lock:
        _events.clear()


def load_synthetic_events():
    """Load test records; never represents live radio traffic."""
    clear_events()

    timestamp = datetime.now(
        timezone.utc
    ).isoformat(timespec="seconds")

    samples = [
        ("TEST-NODE-A", "TEXT", -82, 7.5),
        ("TEST-NODE-B", "POSITION", -94, 2.1),
        ("TEST-NODE-C", "TELEMETRY", -88, 5.3),
    ]

    for index, (sender, packet_type, rssi, snr) in enumerate(samples):
        add_event({
            "id": f"SIM-{index + 1:03d}",
            "timestamp": timestamp,
            "source": sender,
            "destination": "TEST-BASE",
            "packet_type": packet_type,
            "rssi_dbm": rssi,
            "snr_db": snr,
            "message": None,
            "synthetic": True,
            "data_source": "synthetic_test",
        })
