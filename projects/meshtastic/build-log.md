# AEG-002 — Build Log

## 2026-10-26 — Battery and enclosure candidates selected
**Goal:** Support rugged enclosure and 48h endurance, with 24h verified fallback.

**Research:** Hammond 1554F2GYCL clear-lid 120×90×60mm IP-rated empty enclosure ($13.83 listed) and Adafruit #353 protected 3.7V 6600mAh pack, 69×54×18mm ($24.50 listed). No custom OLED window needed.

**Why:** Clear lid minimizes seal penetrations; protected higher-capacity pack gives 110mA theoretical average-current allowance over 48h assuming 80% usability (220mA for 24h).

**Unknown:** Battery pack polarity vs RAK19007, interior usable dimensions, radio antenna bulkhead match, exact RAK configured kit cost and actual system current/charge time.

**Observed:** Documentation only. No hardware procured or tested. Case manufacturer's empty-box rating does not certify modified build.

**Next:** Verify vendor cart, pinout and CAD interior before ordering.

## 2026-10-26 — RAK4631 architecture selected
Requirements captured: rugged, GPS, screen, 48h preferred, open-ended $250+ budget; RAK4631 and RAK19007 platform accepted.

## 2026-10-26 — Planning baseline
Established initial charter, risks, research shortlist and tests.

## 2026-10-29 — RAK4631 starter kit ordered
I ordered one WisBlock RAK4631/RAK19007 starter kit with US915 hardware selection, OLED, RAK12501 GNSS and RAK1904 sensor configuration. Recorded checkout price: $56.30 before import fees and 14–20-day shipping estimate. Physical receipt, actual included parts and functional test **not yet verified**. Previous 'no hardware procured' statements above describe the earlier October 26 planning state only.

**Next:** Inventory on arrival; photograph actual parts; confirm correct antenna, region and safe connection before powering or flashing.

## 2026-11-10 — Delivered hardware inventoried and antennas connected

**Observed:** One previously ordered RAK4631/R​AK19007 starter kit arrived and was unpacked for inspection. Inventory photographs show WisBlock base and core, GNSS module, separate OLED, antenna leads (902–928 MHz PCB LoRa, BLE, ceramic GNSS), alternate rubber antenna with SMA adapter and mounting hardware. **Not all small module SKU markings are readable in photographs**; inventory of the accelerometer and exact OLED subvariant remains to be rechecked. The OLED was **not mounted** and no soldering was performed.

With USB power disconnected, the LoRa, BLE and GNSS antennas were attached to their designated RF connectors. The alternate rubber LoRa antenna and SMA adapter were not used. Final miniature connector engagement should be inspected visually before further handling; photos cannot prove a positive snap fit.

**Boundary:** One node received; external rechargeable pack, Hammond enclosure and a second node were **not purchased or tested** as part of this hardware arrival.

## 2026-11-10 to 2026-11-11 — RAK4631 first USB serial and firmware validation

The Raspberry Pi 5 Tactical Control Terminal (AEG-006) recognized the USB-connected RAK4631 at `/dev/ttyACM0`. The Python virtual environment at `~/aegis-tct/.venv` contained Meshtastic CLI **2.7.11**.

```bash
lsusb
ls -l /dev/ttyACM* /dev/ttyUSB* 2>/dev/null
cd ~/aegis-tct
source .venv/bin/activate
meshtastic --version
meshtastic --port /dev/ttyACM0 --info
```

**Observed:** CLI connected (`Connected to radio`), **RAK4631**, installed firmware **2.7.15.567b8ea**, role `CLIENT`, and **1 known node (self)**. No firmware flashing was needed or performed: the delivered unit was already running Meshtastic.

### Region readback, configuration and node identity

```bash
meshtastic --port /dev/ttyACM0 --get lora.region
# Initially: lora.region: 0 (UNSET)
meshtastic --port /dev/ttyACM0 --set lora.region US
# Observed setting/writing messages
meshtastic --port /dev/ttyACM0 --get lora.region
# After change: lora.region: 1 (US)
meshtastic --port /dev/ttyACM0 --get lora.modem_preset
# Observed: lora.modem_preset: 0 (LONG_FAST)
meshtastic --port /dev/ttyACM0 --set-owner "AEGIS-MESH-01"
meshtastic --port /dev/ttyACM0 --set-owner-short "AE01"
meshtastic --port /dev/ttyACM0 --info
```

**Observed:** long name `AEGIS-MESH-01` and short name `AE01` verified. The region is US and modem preset LONG_FAST. An isolated `termios.error: (5, 'Input/output error')` occurred while closing a CLI readback session; a subsequent reconnect worked and the USB path remained present. USB re-enumeration was suggested but not proved by a kernel trace.

### Initial live telemetry and position event observations

```bash
meshtastic --port /dev/ttyACM0 --listen
# Ctrl+C to stop and release serial port
```

The CLI decoded `TELEMETRY_APP` and `POSITION_APP` events from the connected device. Example `--info` metrics included battery sentinel 101 (USB/external power), voltage 4.243 V, uptime 209 s, channel utilization 0.0% and TX airtime utilization 0.046944443%.

A Python PubSub + `SerialInterface(devPath="/dev/ttyACM0")` 30-second standalone test passed: `[CONNECTED]`, node count 1, `TELEMETRY_APP` (4.253 V; uptime 365 s) and `POSITION_APP`, followed by clean completion. **These events can originate from the local node; they do not demonstrate reception from a separate mesh peer or accurate fresh GPS lock.** No precise coordinates, private keys or node IDs are published.

## 2026-11-11 — Dedicated radio-manager prototype and telemetry parsing

A new local `~/aegis-tct/src/radio_manager.py` was implemented for v0.7 development. It uses a background thread, Meshtastic serial interface, PubSub receive/lost callbacks, lock-protected state snapshot, limited safe telemetry fields and 5-second retry attempts. **This source file still resides on the Pi and is NOT yet committed to GitHub.**

First 30-second radio-manager run: `connected: true`, `node_count: 1`, `packets_observed: 2`; `device_metrics: {}` in the snapshots. A separate 60-second event-shape test verified `decoded.telemetry.deviceMetrics` twice:

```text
batteryLevel=101 voltage=4.241 uptimeSeconds=1627 channelUtilization=0.0 airUtilTx=0.06586111
batteryLevel=101 voltage=4.229 uptimeSeconds=1812 channelUtilization=0.0 airUtilTx=0.08477777
```

A defensive code change avoids overwriting existing metrics with empty telemetry. A manual edit introduced mixed tabs/spaces and then missing indentation, resulting in `TabError` (line 77) and `IndentationError` (line 78). A focused repair restored the indentation, `python -m py_compile src/radio_manager.py` passed, and the 30-second test was repeated successfully:

```text
INFO: Connecting to /dev/ttyACM0
INFO: Meshtastic connection established
connected: true
node_count: 1
packets_observed: 2
last_event.type: POSITION_APP
device_metrics: {batteryLevel: 101, voltage: 4.25, uptimeSeconds: 1872,
                 channelUtilization: 0.0, airUtilTx: 0.08477777}
error: null
Radio test finished.
```

The in-memory telemetry and event counter are **live standalone API-derived measurements**, not yet integrated with the production Flask kiosk. The dashboard continues running **v0.6** with simulated events and an intentionally hardcoded `radio_status: not_connected`. The single actual radio does not establish two-node messaging, battery endurance, BLE, OLED function or enclosure durability. The detailed debugging procedure and service inspection are in the [AEG-006 engineering journal](../tactical-control-terminal/docs/build-journal.md).

**Next:** inspect `app.py` routes; connect a single serial-owning radio manager to Flask; segregate synthetic/live histories; test disconnect/reconnect, reboot and kiosk display; copy exact tested local `radio_manager.py` into the repo; independently validate two-node communication when a second authorized node is available.

## 2026-11-11 — AEG-006 v1.0 integration and AEG-002 next steps

The RAK4631 is now the **tested local radio** in the AEG-006 AEGIS Mesh Control **v1.0 single-node baseline**, which passed physical Pi reboot acceptance 5/5: SSH recovery, automatic Flask startup, serial radio reconnection, new local telemetry, kiosk restoration. Live local event source `AEGIS-MESH-01` appears on the touchscreen. Node hardware/identity/firmware (`RAK4631`, `AEGIS-MESH-01`, `AE01`, `2.7.15.567b8ea`) were verified through production Flask. USB removal triggered connection-loss and unavailable-device errors; auto-reconnect and live telemetry recovery passed. v0.9 diagnostics verified successful-connection count 1→2, recovery count 0→1, uptime reset to 1s, and cleared error. The source snapshot is in GitHub tag `aeg-006-v1.0`.

**AEG-002 remaining qualification:** get a **fresh satellite/GNSS fix** (previous `POSITION_APP` alone is not proof), verify and install OLED module safely, test BLE phone pairing, confirm optional sensor SKU. Peer LoRa messages and real peer RSSI/SNR are untested because only one node is owned. Protected battery pack, capacity/endurance and enclosure remain unpurchased proposals. Keep the already working CLIENT/US/LONG_FAST configuration and avoid competing serial sessions with `aegis-mesh.service`.

[Full v1.0 AEG-006 acceptance](../tactical-control-terminal/docs/build-journal.md).
