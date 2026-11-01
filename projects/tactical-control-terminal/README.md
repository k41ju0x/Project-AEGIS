# AEG-006 — Tactical Control Terminal

**Status:** In Progress. **Platform:** Raspberry Pi 5 (8 GB), Raspberry Pi Touch Display 2 (10-inch), Raspberry Pi OS 64-bit (Debian Trixie).

## AEGIS Mesh Control v0.6

Local-only Flask dashboard at `http://127.0.0.1:5000` displaying live CPU temperature, memory, root filesystem storage, uptime, and Active Cooler RPM. The radio and node views correctly indicate no active RAK4631 connection. Touch navigation and status polling have been verified on physical hardware.

**Verified milestones:**
- Raspberry Pi OS installed; touch display, cooling, SSH and networking operational.
- Meshtastic Python package and CLI v2.7.11 in `/home/aegis/aegis-tct/.venv` (Python 3.13.5).
- Flask v3.1.3 running locally via `aegis-mesh.service`; starts on reboot.
- Chromium fullscreen kiosk via `labwc` graphical autostart, without keyring prompt after using a dedicated basic password-store kiosk configuration.
- v0.2 API verifies CPU temperature, memory, storage, uptime, and fan RPM.
- v0.3 RF Monitor shows offline radio status without claiming spectrum reception.
- v0.4 synthetic packet buffer/API with TEXT, POSITION and TELEMETRY test records.
- v0.5 RSSI/SNR averages, source counts and illustrative signal bars, verified on touchscreen.
- **v0.6** source and packet-type filters, 10/50/200 record display controls, Pause/Resume, Clear/Restore View; touchscreen controls verified. Only three synthetic records exist, so history-limit behavior above ten remains untested.

**Pending:** Connect RAK4631 when delivered and validate actual RF packet capture; add original photos and complete remaining evidence in the journal. Version 0.6 source is published and touchscreen-tested with explicitly synthetic records.


## Engineering build journal

**[Step-by-step build journal](docs/build-journal.md)** — chronological hardware, commands, purpose, test evidence, troubleshooting and photo register. Reconstructed from verified sessions; original photos and unrecorded terminal output still need to be added.

## Repository source files

```text
src/
  app.py
  packet_store.py
  templates/
    index.html
requirements.txt
docs/
  build-journal.md
```

Do not commit the Pi's `.venv/`, logs, keyring, keys, credentials, private channel configuration, or host-specific network information.

## Planned RF monitoring

1. **Mesh Traffic Monitor:** display received Meshtastic packet metadata (time, sender, destination, type, RSSI/SNR where present), receive counts, and text decoded by the owned radio on authorized channels.
2. **Channel Monitor:** display configured region, modem preset, channel settings and frequency slot from the connected radio; label it as configuration, not a measured spectral survey.
3. **RF Spectrum Monitor (future hardware phase):** wideband energy plots and waterfall from an SDR or compatible RF receiver. Not possible from the ordinary Meshtastic API alone.

**Safety and privacy:** logging should be disabled by default until the user opts in; avoid publishing message bodies, location data, node IDs or secret channel keys. Restrict the web server to loopback unless remote access is deliberately designed and secured.

Tracking: [AEG-006 issue](https://github.com/k41ju0x/Project-AEGIS/issues/6).
