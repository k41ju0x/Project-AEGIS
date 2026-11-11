# AEG-002 — Verification Plan and Initial Bench Evidence
**Status (November 11, 2026):** Standalone RAK4631 USB, identity, telemetry, recovery and AEG-006 v1.0 integration accepted. AEG-002 remains open for fresh GNSS fix, OLED, Bluetooth pairing, battery endurance, enclosure and peer RF testing. No firmware flashing has been performed or required.

| Test ID | Requirement | Planned procedure | Evidence / criteria |
|---|---|---|---|
| TST-001 | REQ-001 | Flash correct supported firmware; cold boot twice | Version and serial/application screenshots; both boots succeed |
| TST-002 | REQ-002 | Check SKU, antenna matching, region settings before RF activity | Inspection sheet; compliance questions cleared |
| TST-003 | REQ-005 | Pair with compatible client; read back device settings | Screenshots with sensitive values redacted |
| TST-004 | REQ-003 | Exchange identified test messages both ways between controlled nodes | Send/receive times and delivery observed on both ends |
| TST-005 | REQ-004 | Charge using vendor-safe method and test representative workload | Voltage/battery log and measured hours, test profile included |
| TST-006 | REQ-006 | Reproduce settings and assembly using docs | Independent checklist of all steps |
| TST-007 | REQ-007 | Inspect enclosure, battery restraint, power-button/USB access | Pass/fail issues, images with sensitive metadata removed |
| TST-008 | REQ-003 | Repeat RF delivery trials in varied terrain under permitted conditions | Packet counts, locations generalized publicly, environment and antennas documented |

## Executed evidence — November 10–11, 2026

| Check | Result | Evidence |
|---|---|---|
| Kit arrival and partial assembly inventory | **PASS (initial)** | Kit and connector photos, LoRa/BLE/GNSS antenna leads installed; exact accessory SKU verification pending |
| USB radio detection | **PASS** | `/dev/ttyACM0` appeared on AEG-006 |
| Installed firmware identity | **PASS** | Meshtastic CLI 2.7.11 connected to RAK4631 firmware `2.7.15.567b8ea` |
| Region and modem readback | **PASS** | `lora.region: 1` (US), `lora.modem_preset: 0` (LONG_FAST) |
| Node naming | **PASS** | `AEGIS-MESH-01`, `AE01` read back |
| Receive subscription | **PASS (single-node)** | `TELEMETRY_APP` and `POSITION_APP` callbacks; not proof of peer messages or fresh GNSS lock |
| Device metrics parsing | **PASS** | 60-second test produced two `deviceMetrics` samples; final manager run parsed voltage 4.25 V and uptime 1872 s |
| Radio manager standalone runtime | **PASS (30 s)** | Connected, 1 node, 2 events, error null |
| Flask live integration and touchscreen | **PASS (AEG-006 v1.0)** | Live local telemetry and separate simulation, node identity, firmware and recovery counters verified in production Flask and physical kiosk |
| USB recovery and Pi reboot | **PASS** | Disconnection detected, supervisor reconnected, live telemetry resumed; full five-of-five reboot/kiosk acceptance reported for AEG-006 v1.0 |
| Fresh GNSS fix / OLED / BLE pairing | **NOT TESTED** | Next bench qualification tasks (no new hardware required) |
| Two-node messaging, battery, enclosure | **NOT TESTED** | Still open under relevant requirements |

**Interpretation of original TST-001:** Firmware identity and normal USB boot verified, but the original test specifically requires *flashing and two cold boots*, so **TST-001 remains incomplete**; do not silently convert installation detection into flashing acceptance.

[Detailed dated observed commands and outputs](build-log.md) · [AEG-006 integration journal](../tactical-control-terminal/docs/build-journal.md)

Do not publish exact private coordinates. Record obstacles, mounting elevation, antenna, settings, weather, and firmware when comparing RF tests.

## AEG-002 follow-up qualification order — after AEG-006 v1.0

1. **Fresh GNSS fix:** test outdoors with antenna attached, document acquisition success, satellites/fix quality when available, and no public coordinates. Keep the existing serial owner exclusive during any CLI inspection.
2. **OLED module:** verify actual SKU/slot/pinout before installing with all power disconnected; inspect for boot/screen operation.
3. **Bluetooth:** validate phone pairing, read-only node information and controlled handoff, avoiding simultaneous configuration writes with the Pi session.
4. **Sensor:** read module markings and confirm required telemetry support; do not assume an accelerometer reading from deviceMetrics.
5. **Deferred:** two-node message delivery / peer RSSI-SNR, protected pack polarity and battery endurance, rugged enclosure/antenna feedthrough and ingress tests.

AEG-006 v1.0 release acceptance does **not** imply AEG-002 field-ready acceptance. [AEG-006 release](../tactical-control-terminal/README.md).

## GNSS follow-up result — November 11, 2026

**PASS (internal GNSS position report):** An actual local `POSITION_APP` callback was observed at `2026-11-11T17:28:45+00:00`; privacy-safe monitoring reported 15 satellites, `location_source=LOC_INTERNAL`, and presence of coordinate fields. The user observed the event after initially receiving `gnss=None` while waiting for a position update. The OLED previously reported 6 satellites and was visually confirmed operating.

**Qualification:** `fix_type` and `fix_quality` were absent, so exact fix quality, 2D/3D classification, reported accuracy and real-world coordinate correctness have not been measured. Do not expose coordinate values in public logs. GNSS hardware/event integration is verified; precise location accuracy testing remains optional future validation.

## Bluetooth acceptance — November 11, 2026

**PASS (BLE pairing and connection):** User reports Meshtastic app on iPhone successfully paired to the RAK4631, and connection was good. Specific mobile-side configuration readbacks and reconnect persistence are not independently documented. Normal AEG-006 USB monitoring restoration after BLE handoff remains to be confirmed.
