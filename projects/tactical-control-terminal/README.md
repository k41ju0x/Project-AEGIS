# AEG-006 — Tactical Control Terminal

**Status: v1.0 single-node baseline accepted (November 11, 2026).** Platform: Raspberry Pi 5 (8 GB), Raspberry Pi Touch Display 2 (10-inch), Raspberry Pi OS 64-bit (Debian Trixie), RAK4631 Meshtastic radio.

## AEGIS Mesh Control — v1.0 acceptance

Local-only Flask dashboard bound to `127.0.0.1:5000`, run by `aegis-mesh.service`; Chromium kiosk renders the dashboard on the Pi's touchscreen.

**User-reported v1.0 reboot acceptance — 5/5 PASS:**
- Raspberry Pi boots and Termius/SSH reconnects without manual service intervention.
- Flask service starts automatically.
- USB-attached RAK4631 radio reconnects.
- Fresh Meshtastic telemetry is observed after reboot.
- Touchscreen dashboard/kiosk restores.

**Verified earlier acceptance:**
- v0.2–v0.6: system telemetry, RF Monitor scaffold, explicitly synthetic packet data and touch controls.
- v0.7: live local Meshtastic event route `/api/packets/live`; `AEGIS-MESH-01` appears on Live Radio; simulation on separate `/api/packets`. Local telemetry is not proof of over-the-air peer reception.
- v0.8: local node identity `AEGIS-MESH-01` / `AE01`, hardware `RAK4631`, firmware `2.7.15.567b8ea`, voltage and health fields from existing serial session; USB disconnect/reconnect and resumed telemetry verified.
- v0.9: service-process connection uptime, successful connection count, recovery count and connection timestamps. Controlled USB removal produced `ConnectionError` then `Serial device unavailable`; return to connected state incremented connections 1→2, recoveries 0→1, uptime restarted at 1 s and errors cleared.
- v1.0: entire single-node boot-to-live-monitoring path passed the five-check reboot acceptance above.

**Radio baseline:** Meshtastic Python CLI 2.7.11 (Python 3.13.5), US region, LONG_FAST preset, USB serial `/dev/ttyACM0` in observed tests. Flask 3.1.3. Runtime application: `/home/aegis/aegis-tct`.

### Included components

```text
src/
  app.py                 # Flask status, RF and packet-history APIs
  radio_manager.py       # one supervised serial session; identity, health and recovery state
  live_packet_store.py   # bounded, nonpersistent local event history
  packet_store.py        # separate synthetic demonstration history
  templates/
    index.html           # touchscreen/kiosk UI
requirements.txt
docs/
  build-journal.md
```

### Operational checks

```bash
systemctl is-active aegis-mesh.service
systemctl is-enabled aegis-mesh.service
curl -fsS http://127.0.0.1:5000/api/status | python3 -m json.tool
curl -fsS http://127.0.0.1:5000/api/packets/live | python3 -m json.tool
sudo journalctl -u aegis-mesh.service -n 60 --no-pager
```

**Scope / limits:** v1.0 is a **single local Meshtastic node monitor**. No second node or verified inter-node LoRa messaging; no peer receive RSSI/SNR measurements. A local POSITION event is not proof of a valid GPS fix. The supervisor has passed same-port `/dev/ttyACM0` reconnect tests, not serial-device renumbering or extensive stress/endurance. Health counters are process-local and reset on Flask restart. Live history is bounded in memory and is lost on restart. Explicitly retain these limitations in future reports.

**Future gated work:** fresh two-node RF reception only after access to an authorized second node; more robust USB device enumeration/recovery; optional endurance, battery and enclosure work; no wideband spectrum measurements without separate suitable hardware. Original bench photos and hardware evidence may still need upload.

**Engineering records:** [Detailed build journal](docs/build-journal.md) · [Reproduction guide](REPRODUCE.md) · [Issue #6](https://github.com/k41ju0x/Project-AEGIS/issues/6).

**Privacy/security:** Do not publish keys, GPS coordinates, raw message content, numerical node IDs, logs with secrets or host-specific private network details. Keep Flask bound to loopback until authenticated remote access is deliberately designed. The separate reproduction guide uses sanitized example paths; use the actual Pi paths when administering the deployed system.
