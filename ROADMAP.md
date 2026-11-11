# Project Aegis Roadmap

## Phase 1 — Foundation
- [x] Create Project Aegis repository
- [x] Register existing Project NEXUS home lab
- [x] Create GitHub Projects board and add four project issues (validated during project setup)
- [x] Configure table fields (validated during project setup)
- [x] Publish handbook, reusable templates and publication safety guidelines
- [ ] Independently review board option names and assignments in GitHub UI

## Phase 2 — Project intake
- [x] Confirm Meshtastic requirements, radio platform, and hardware budget (RAK4631 kit selected, delivered November 10 and initially bench-tested)
- [ ] Inventory existing Pwnagotchi assets
- [ ] Define authorized requirements for remote access hardware
- [ ] Record current NEXUS progress and next milestone

## Phase 3 — Engineering
- [ ] Populate architecture, bill of materials and test plan for active projects
- [ ] Create separate engineering repositories as needed
- [ ] Complete full documentation/photo evidence lifecycle for AEG-006 (v1.0 single-node functionality accepted; original photo register and additional evidence remain open)

[Engineering handbook](docs/README.md) · [Tracking board](https://github.com/users/k41ju0x/projects/3/views/1)

## Current engineering checkpoint — November 11, 2026
- **AEG-006:** AEGIS Mesh Control **v1.0 single-node baseline accepted**. Physical Pi reboot test passed 5/5: boot and SSH reconnect, automatic Flask startup, RAK4631 USB reconnect, fresh live telemetry, and touchscreen kiosk restoration. v0.9 recovery counters and uptime reset previously verified under unplug/replug. [Project README](projects/tactical-control-terminal/README.md) · [Build journal](projects/tactical-control-terminal/docs/build-journal.md) · [Issue #6](https://github.com/k41ju0x/Project-AEGIS/issues/6).
- **AEG-002:** RAK4631 local radio integrated with AEG-006: firmware 2.7.15.567b8ea, US/LONG_FAST, AEGIS-MESH-01/AE01 and telemetry verified. Two-node peer LoRa messaging, valid GNSS fix, OLED, battery/endurance and enclosure remain separate unverified follow-ups.
- **Scope:** v1.0 is the stable **single-node** monitor, not a finished mesh network, validated peer RF RSSI/SNR receiver, or spectrum analyzer. Photos, long-duration reliability and USB port-renumbering remain to be addressed separately.
