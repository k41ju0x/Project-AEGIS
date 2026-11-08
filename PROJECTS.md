# Project AEGIS — Canonical Project Registry

**Updated November 8, 2026.** This is the **single authoritative project-number registry**. [Future Ideas](FUTURE-IDEAS.md) is the detailed archive; the [main README](README.md) is a short index. The GitHub Project board is for active/approved work only, not every numbered idea.

## Canonical IDs

| ID | Initiative | Status | Reference |
|---|---|---|---|
| AEG-001 | Project NEXUS | Existing home lab, separate | [Project NEXUS](https://github.com/k41ju0x/Project-NEXUS) · [#1](https://github.com/k41ju0x/Project-AEGIS/issues/1) |
| AEG-002 | Meshtastic — RAK4631 | Awaiting kit/integration | [Planning #2](https://github.com/k41ju0x/Project-AEGIS/issues/2) · [Build #5](https://github.com/k41ju0x/Project-AEGIS/issues/5) |
| AEG-003 | Pwnagotchi | **Build operational; remaining acceptance limitations documented** | [Overview](projects/pwnagotchi/README.md) · [#3](https://github.com/k41ju0x/Project-AEGIS/issues/3) |
| **AEG-004** | **Portable LattePanda Remote Access Device** | Parked; consolidated project | [Scope](projects/remote-access-device/README.md) · [#4](https://github.com/k41ju0x/Project-AEGIS/issues/4) |
| AEG-005 | ESP32 Marauder Lab | Parked | [Scope](projects/esp32-marauder/README.md) |
| AEG-006 | Tactical Control Terminal | Hardware/dashboard built; radio integration pending | [Overview](projects/tactical-control-terminal/README.md) · [#6](https://github.com/k41ju0x/Project-AEGIS/issues/6) |
| AEG-007 | RFID/NFC Security Lab | Parked | [Notes](projects/rfid-nfc/README.md) |
| AEG-008 | OpenWrt Rogue AP / DIY Wi-Fi Pineapple Lab | Parked | [Notes](projects/openwrt-rogue-ap/README.md) |
| AEG-009 | Custom Reconnaissance Toolkit | Parked | [Notes](projects/custom-recon-toolkit/README.md) |
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
2. **AEG-004** is the single Portable LattePanda Remote Access Device; **AEG-005** is ESP32 Marauder and **AEG-010** is ESP32 GPS Wardriver. They are three distinct project concepts.
3. Preserve existing distinct assignments: AEG-002 = Meshtastic, AEG-006 = Tactical Control Terminal, AEG-016 = Sentinel; AEG-007–AEG-017 remain the same aside from the newly assigned AEG-010.
4. **Next new project: AEG-021**. IDs AEG-001 through AEG-020 are now continuously assigned. Keep historical project names as annotations rather than as competing ID records.
5. GitHub issue numbers and project numbers are different namespaces. For example, **issue #5 is an AEG-002 task**, not Project AEG-005.
6. Numbered and *Parked* does **not** mean approved, funded or placed on the [Project AEGIS board](https://github.com/users/k41ju0x/projects/3/views/1).
7. Project NEXUS and APEX remain separate platforms and repositories/efforts; APEX has no new AEG ID assigned by this reconciliation.

## Current focus

I have built and validated the core **AEG-003 Pwnagotchi** hardware and software, with documented deferred battery-cutoff, Bluetooth-interruption and handshake-completeness checks. I will next focus on the ordered **AEG-002 RAK4631** kit and its live integration with **AEG-006** when hardware arrives. **AEG-016** remains deferred. I am not approving additional purchases or backlog builds by numbering these ideas.

## Documentation

- [AEG-003 build journal](projects/pwnagotchi/docs/build-journal.md) · [test matrix](projects/pwnagotchi/docs/test-matrix.md)
- [Future Ideas Backlog](FUTURE-IDEAS.md)
- [Secondary registry compatibility pointer](projects/PROJECT-REGISTRY.md)
