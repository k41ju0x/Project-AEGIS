# AEG-006 — Tactical Control Terminal

**Status:** In Progress. **Platform:** Raspberry Pi 5 (8 GB), Raspberry Pi Touch Display 2 (10-inch), Raspberry Pi OS 64-bit (Debian Trixie).

## AEGIS Mesh Control v0.6 — deployed; v0.7 live-radio manager under development

Local-only Flask dashboard at `http://127.0.0.1:5000` displaying live CPU temperature, memory, root filesystem storage, uptime, and Active Cooler RPM. The **v0.6 backend** still reports `not_connected`/`awaiting_radio` because the Flask application has **not yet integrated** the now-present RAK4631. This is a fixed software status, not a radio connectivity failure. Touch navigation and status polling have been verified on physical hardware.

**Verified milestones:**
- Raspberry Pi OS installed; touch display, cooling, SSH and networking operational.
- Meshtastic Python package and CLI v2.7.11 in `/home/aegis/aegis-tct/.venv` (actual running Pi path; sanitized reproduction guide uses illustrative `~/tct-app`) (Python 3.13.5).
- Flask v3.1.3 running locally via `aegis-mesh.service`; starts on reboot.
- Chromium fullscreen kiosk via `labwc` graphical autostart, without keyring prompt after using a dedicated basic password-store kiosk configuration.
- v0.2 API verifies CPU temperature, memory, storage, uptime, and fan RPM.
- v0.3 RF Monitor shows offline radio status without claiming spectrum reception.
- v0.4 synthetic packet buffer/API with TEXT, POSITION and TELEMETRY test records.
- v0.5 RSSI/SNR averages, source counts and illustrative signal bars, verified on touchscreen.
- **v0.6** source and packet-type filters, 10/50/200 record display controls, Pause/Resume, Clear/Restore View; touchscreen controls verified. Only three synthetic records exist, so history-limit behavior above ten remains untested.

**November 10–11 bench milestones:** RAK4631 kit received, LoRa/BLE/GNSS antennas attached, USB interface `/dev/ttyACM0` detected, CLI 2.7.11 connected to RAK4631 firmware 2.7.15.567b8ea; US region and LONG_FAST preset verified; identity `AEGIS-MESH-01`/`AE01` verified. Live `TELEMETRY_APP`/`POSITION_APP` events and device metrics received via a standalone Python listener. A separately developed `~/aegis-tct/src/radio_manager.py` prototype passed a 30-second connection/telemetry test after an indentation repair. **This file is not yet copied to GitHub, the Flask backend is still v0.6, and no dashboard live-radio integration is deployed.**

**Pending:** Integrate a single persistent serial owner with Flask, segregate live and synthetic events, validate the kiosk and USB reconnect/reboot behavior, upload additional photo evidence, and publish the exact tested v0.7 source. One-node local telemetry does not demonstrate two-node mesh RF reception.


## Engineering build journal

**[Step-by-step build journal](docs/build-journal.md)** — chronological hardware, recorded commands, purpose, results, troubleshooting and photo register. **[Reproduction guide](REPRODUCE.md)** — separate, source-grounded fresh-install procedure, explicitly distinguishing reconstructed commands from original execution. Original photos and unrecorded terminal output still need to be added.

## Repository source files

```text
src/
  app.py
  packet_store.py
  # radio_manager.py is currently under local Pi testing; not yet committed
  templates/
    index.html
requirements.txt
docs/
  build-journal.md
```

**Observed local runtime:** `/home/aegis/aegis-tct`. The separate reproduction guide intentionally uses sanitized example paths; do not copy the example systemd unit onto the working Pi without adjusting for real paths.

Do not commit the Pi's `.venv/`, logs, keyring, keys, credentials, private channel configuration, or host-specific network information.

## Planned RF monitoring

1. **Mesh Traffic Monitor:** display received Meshtastic packet metadata (time, sender, destination, type, RSSI/SNR where present), receive counts, and text decoded by the owned radio on authorized channels.
2. **Channel Monitor:** display configured region, modem preset, channel settings and frequency slot from the connected radio; label it as configuration, not a measured spectral survey.
3. **RF Spectrum Monitor (future hardware phase):** wideband energy plots and waterfall from an SDR or compatible RF receiver. Not possible from the ordinary Meshtastic API alone.

**Safety and privacy:** logging should be disabled by default until logging is explicitly enabled; avoid publishing message bodies, location data, node IDs or secret channel keys. Restrict the web server to loopback unless remote access is deliberately designed and secured.

Tracking: [AEG-006 issue](https://github.com/k41ju0x/Project-AEGIS/issues/6).
