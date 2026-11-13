# Project AEGIS — Canonical Project Registry

**Updated November 11, 2026.** This is the **single authoritative project-number registry**. [Future Ideas](FUTURE-IDEAS.md) is the detailed archive; the [main README](README.md) is a short index. The GitHub Project board is for active/approved work only, not every numbered idea.

## Canonical IDs

| ID | Initiative | Status | Reference |
|---|---|---|---|
| AEG-001 | Project NEXUS | Existing home lab, separate | [Project NEXUS](https://github.com/k41ju0x/Project-NEXUS) · [#1](https://github.com/k41ju0x/Project-AEGIS/issues/1) |
| AEG-002 | Meshtastic — RAK4631 | Kit received; USB, firmware, US/LONG_FAST, live local telemetry verified; peer testing pending | [Planning #2](https://github.com/k41ju0x/Project-AEGIS/issues/2) · [Build #5](https://github.com/k41ju0x/Project-AEGIS/issues/5) |
| AEG-003 | Pwnagotchi | **Completed (November 7, 2026); deferred follow-ups documented** | [Overview](projects/pwnagotchi/README.md) · [#3](https://github.com/k41ju0x/Project-AEGIS/issues/3) |
| **AEG-004** | **Portable LattePanda Remote Access Device** | Original Sigma 32GB SSD + Wi-Fi bundle ordered; awaiting shipment | [Scope](projects/remote-access-device/README.md) · [#4](https://github.com/k41ju0x/Project-AEGIS/issues/4) |
| AEG-005 | ESP32 Marauder Lab | Parked | [Scope](projects/esp32-marauder/README.md) |
| AEG-006 | Tactical Control Terminal | v1.0 single-node monitor accepted: live telemetry, touchscreen, reboot recovery and v0.9 USB reliability verified | [Overview](projects/tactical-control-terminal/README.md) · [#6](https://github.com/k41ju0x/Project-AEGIS/issues/6) |
| AEG-007 | RFID/NFC Security Lab | Parked | [Notes](projects/rfid-nfc/README.md) |
| AEG-008 | OpenWrt Rogue AP / DIY Wi-Fi Pineapple Lab | Parked | [Notes](projects/openwrt-rogue-ap/README.md) |
| AEG-009 | Custom Reconnaissance Toolkit | In Progress — v0.1 requirements and Kali lab preparation; implementation pending | [Notes](projects/custom-recon-toolkit/README.md) |
| AEG-010 | ESP32 GPS Wardriver | Parked | [Scope](projects/esp32-gps-wardriver/README.md) |
| AEG-011 | Ethernet Assessment Appliance | Parked | [Notes](projects/ethernet-assessment-appliance/README.md) |
| AEG-012 | Evil Twin Defense Lab | Parked | [Notes](projects/evil-twin-defense/README.md) |
| AEG-013 | Web Application Security Lab | Parked | [Notes](projects/web-app-security/README.md) |
| AEG-014 | IoT Security Research Platform | Parked | [Notes](projects/iot-security-research/README.md) |
| AEG-015 | Flipper Zero Development Lab | Parked | [Notes](projects/flipper-development/README.md) |
| AEG-016 | AEGIS Sentinel — Desktop AI Companion | Deferred; hardware received | [Notes](projects/aegis-sentinel/README.md) |
| AEG-017 | Pico Ducky / HID Research | Parked | [Notes](projects/pico-ducky/README.md) |
| AEG-018 | Dedicated Wireless Analysis Station | Parked | [Future ideas](FUTURE-IDEAS.md) |
| AEG-019 | Standalone Network Diagnostics Console | Parked | [Future ideas](FUTURE-IDEAS.md) |
| AEG-020 | AEGIS Project Telemetry Integrations | Parked | [Future ideas](FUTURE-IDEAS.md) |

## Rules that prevent collisions

1. Every distinct concept gets **one permanent ID** on registration, even while parked.
2. GitHub issue numbers and project numbers are different namespaces. For example, **issue #5 is an AEG-002 task**, not Project AEG-005.
3. Numbered and *Parked* does **not** mean approved, funded or placed on the [Project AEGIS board](https://github.com/users/k41ju0x/projects/3/views/1).
4. Project NEXUS and APEX remain separate platforms and repositories/efforts; APEX has no new AEG ID assigned by this reconciliation.

## Current focus

I completed **AEG-003 Pwnagotchi** on November 7, 2026, with documented deferred battery-cutoff, Bluetooth-interruption and handshake-completeness checks. Current engineering work is on the **received AEG-002 RAK4631** kit and **AEG-006**. AEG-006 v1.0 single-node baseline has passed live node telemetry, UI, USB recovery and reboot acceptance; multi-node reception remains open as a separate future capability. **AEG-016** remains deferred. AEG-004 Sigma hardware was ordered November 8, 2026; assembly and testing are pending shipment. This does not authorize other backlog purchases.

## Documentation

- [AEG-002 hardware receipt, configuration and telemetry build log](projects/meshtastic/build-log.md) · [test status](projects/meshtastic/test-plan.md)
- [AEG-006 v1.0 single-node engineering journal](projects/tactical-control-terminal/docs/build-journal.md)

- [AEG-003 build journal](projects/pwnagotchi/docs/build-journal.md) · [test matrix](projects/pwnagotchi/docs/test-matrix.md)
- [Future Ideas Backlog](FUTURE-IDEAS.md)
- [Secondary registry compatibility pointer](projects/PROJECT-REGISTRY.md)
