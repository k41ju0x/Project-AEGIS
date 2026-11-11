# AEG-002 — Verification Plan and Initial Bench Evidence
**Status (November 11, 2026):** Partial USB and telemetry acceptance executed. No firmware flashing, battery endurance, OLED, BLE pairing, enclosure, fresh GNSS-fix or peer-to-peer RF acceptance has been demonstrated.

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
| Radio manager standalone runtime | **PASS (30 s)** | Connected, 1 node, 2 events, error null; reconnection under real USB unplug still untested |
| Flask v0.7 live integration | **NOT STARTED** | v0.6 API still reports `not_connected` despite serial candidate |
| Two-node messaging, OLED, battery, enclosure | **NOT TESTED** | Still open under relevant requirements |

**Interpretation of original TST-001:** Firmware identity and normal USB boot verified, but the original test specifically requires *flashing and two cold boots*, so **TST-001 remains incomplete**; do not silently convert installation detection into flashing acceptance.

[Detailed dated observed commands and outputs](build-log.md) · [AEG-006 integration journal](../tactical-control-terminal/docs/build-journal.md)

Do not publish exact private coordinates. Record obstacles, mounting elevation, antenna, settings, weather, and firmware when comparing RF tests.
