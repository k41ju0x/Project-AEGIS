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
- [ ] Complete end-to-end documentation lifecycle for first build (AEG-006 v0.6 validated; original photos, full build evidence and radio integration pending)

[Engineering handbook](docs/README.md) · [Tracking board](https://github.com/users/k41ju0x/projects/3/views/1)

## Current engineering checkpoint — November 11, 2026
- **AEG-006:** Raspberry Pi 5 and 10-inch touchscreen functional; AEGIS Mesh Control **v0.6 UI remains deployed** and touchscreen-tested with explicit synthetic packet data. A **partial v0.7 Flask backend integration is now running under systemd** and returned real radio `connected` state and telemetry on port 5000. Kiosk visual status and live packet view are still pending; local tested app/manager code is not yet published in GitHub. [Project README](projects/tactical-control-terminal/README.md) · [Build journal](projects/tactical-control-terminal/docs/build-journal.md) · [Issue #6](https://github.com/k41ju0x/Project-AEGIS/issues/6).
- **AEG-002:** Kit **received November 10**; LoRa/BLE/GNSS antenna setup inspected, USB `/dev/ttyACM0` detected, RAK4631 firmware 2.7.15 identified, US region / LONG_FAST and node names configured, live local telemetry/position events and Python connection manager verified. OLED, BLE pairing, GNSS fix, enclosure/battery tests and two-node messaging remain pending. [Project README](projects/meshtastic/README.md) · [Execution issue #5](https://github.com/k41ju0x/Project-AEGIS/issues/5).
- **Documentation:** Detailed November 10–11 integration and error/recovery journals published. Some original build photographs are already embedded; new RAK4631 photos still require uploading. Do not claim multi-node over-the-air reception, Flask v0.7 deployment or wideband RF spectrum measurements.
