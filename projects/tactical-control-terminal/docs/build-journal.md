# AEG-006 Engineering Build Journal

This journal records the Raspberry Pi 5 / 10-inch touchscreen Tactical Control Terminal. It is reconstructed from verified sessions; it is not a verbatim terminal transcript. Photos mentioned below are pending upload and are not represented as committed artifacts.

## Phase 1 — Assembly and OS
Installed Pi 5, DSI touchscreen, and Active Cooler. Initial blank screen resolved after EEPROM update and reboot. Debian 13 Trixie; touchscreen taps and swipes verified.

Commands and rationale:
```bash
cat /etc/os-release      # Identify OS
uname -a                 # Identify kernel
sudo apt full-upgrade    # Apply package upgrades
sudo rpi-eeprom-update   # Inspect bootloader
```
Evidence: physical assembly and working touchscreen photo to add.

## Phase 2 — Cooling and system baseline
Measured approximately 45 C CPU temperature; manual fan speed measurements approximately 7566 RPM at PWM 255 and 5099 RPM at PWM 125.
```bash
cat /sys/class/thermal/thermal_zone0/temp
ls /sys/class/hwmon/
```
Evidence: cooler and thermal testing photos pending.

## Phase 3 — Python/Flask and kiosk
Python 3.13.5, Meshtastic Python client 2.7.11, Flask 3.1.3. Virtual environment under ~/aegis-tct/.venv. Flask binds 127.0.0.1:5000. systemd unit aegis-mesh.service enabled. Chromium kiosk starts via labwc autostart.
```bash
systemctl is-enabled aegis-mesh.service
systemctl is-active aegis-mesh.service
systemctl status aegis-mesh.service --no-pager
curl -sS http://127.0.0.1:5000/api/status
```
Why: validate service, boot integration, and telemetry before adding radio features.
Evidence: kiosk photos pending.

## Phase 4 — v0.2 system monitoring
Implemented CPU temperature, memory, storage, uptime, and fan RPM. Fixed uptime parsing and hwmon pwmfan detection. Verified cards on touchscreen. Source milestone: 776c9db.

## Phase 5 — v0.3 RF monitor
```bash
curl -sS http://127.0.0.1:5000/api/rf
```
Verified radio_connected false, packets_received zero, spectrum_available false. No radio or SDR attached. Source milestone: 307f2f8.

## Phase 6 — v0.4 synthetic packets
In-memory packet store bounded at 200 events. Three explicitly synthetic samples: TEXT from TEST-NODE-A (-82 dBm, 7.5 dB), POSITION from TEST-NODE-B (-94 dBm, 2.1 dB), TELEMETRY from TEST-NODE-C (-88 dBm, 5.3 dB).
```bash
curl -i --max-time 5 http://127.0.0.1:5000/api/packets
sudo journalctl -u aegis-mesh.service -n 30 --no-pager
grep -n 'def packet_events' ~/aegis-tct/src/app.py
grep -n 'def packet_events' ~/aegis-portfolio/projects/tactical-control-terminal/src/app.py
```
Why: investigate HTTP 404. Root cause: live backend lacked the endpoint even though GitHub copy contained it. Corrected file synchronized, compiled, restarted, and three synthetic records verified.
Source milestones: 0fc2625, eab09bf.

## Phase 7 — v0.5 packet statistics
Confirmed TEXT filter shows one event, one source, -82.0 dBm RSSI and 7.5 dB SNR. Three-record averages -88.0 dBm RSSI and 5.0 dB SNR. RSSI bars are illustrative, not spectrum data. Touchscreen tested.

## Phase 8 — v0.6 history controls
Verified source filter, type filter, Pause/Resume, Clear/Restore View, RSSI bars, and statistics on touchscreen. Backend retained separately; clearing view does not delete server packet history. Version 0.6 published. History 10/50/200 selectors still need validation with more than 10 records.
Evidence: original photo of v0.6 touchscreen provided in chat; not yet uploaded to GitHub.

## Phase 9 — RAK4631 integration — not started
Await starter kit. Inventory, configure Meshtastic US915, bench test via phone, connect USB to Pi, ingest live events separately from synthetic data.

## Photo register (pending original file upload)
- photos/01-assembly.jpg — Pi and display assembly
- photos/02-kiosk.jpg — running touchscreen dashboard
- photos/03-monitoring.jpg — system telemetry
- photos/04-v06.jpg — packet history controls

## Future session format
Record goal, actual commands, reason for each command, full redacted output, what the output means, error and resolution, test pass/fail, source commit and embedded original photo. Never fabricate output or imply photos are present before they are committed.

Tracking: https://github.com/k41ju0x/Project-AEGIS/issues/6
