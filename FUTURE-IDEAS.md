# 🧭 Project AEGIS — Future Ideas Backlog

**Updated:** November 8, 2026  
**Status:** Parked / research ideas only. Number assignment is **not** approval to build, purchase hardware, or add a GitHub Projects board card.

## Numbering policy

- **One canonical AEG ID per distinct project.** An ID is permanent once assigned; renaming a project does not create a new ID.
- **AEG-004** is the single Portable LattePanda Remote Access Device. Its hardware platform is **LattePanda**.
- **AEG-005** is the ESP32 Marauder Lab and **AEG-010** is the ESP32 GPS Wardriver. These are independent parked projects.
- **AEG-001 through AEG-020 are now assigned continuously.** Distinct existing projects retain their identities, especially AEG-002 Meshtastic, AEG-006 Tactical Control Terminal, and AEG-016 Sentinel.
- The three remaining ideas occupy **AEG-018–AEG-020**. The authoritative source for IDs and status is [PROJECTS.md](PROJECTS.md). GitHub **issue numbers** are not project IDs: for example, issue #5 belongs to **AEG-002**.
- Project NEXUS and APEX stay architecturally separate; APEX is not assigned a new AEG number here.

## Registered projects — current and previously approved concepts

| AEG ID | Canonical name | Status | Notes |
|---|---|---|---|
| AEG-001 | Project NEXUS | Existing / separate | Home-lab repository; review tracked in [issue #1](https://github.com/k41ju0x/Project-AEGIS/issues/1) |
| AEG-002 | Meshtastic — RAK4631 | Hardware ordered | Planning [#2](https://github.com/k41ju0x/Project-AEGIS/issues/2), build [#5](https://github.com/k41ju0x/Project-AEGIS/issues/5) |
| AEG-003 | Pwnagotchi | Operational build; acceptance follow-ups documented | [Issue #3](https://github.com/k41ju0x/Project-AEGIS/issues/3) · [Build journal](projects/pwnagotchi/docs/build-journal.md) |
| **AEG-004** | **Portable LattePanda Remote Access Device** | **Parked** | Portable headless\/GUI remote administration and assessment device; [issue #4](https://github.com/k41ju0x/Project-AEGIS/issues/4) |
| **AEG-005** | **ESP32 Marauder Lab** | Parked | [Scope](projects/esp32-marauder/README.md) |
| AEG-006 | Tactical Control Terminal | Built; live Meshtastic integration pending | [Issue #6](https://github.com/k41ju0x/Project-AEGIS/issues/6) |
| AEG-007 | RFID/NFC Security Lab | Parked | [Notes](projects/rfid-nfc/README.md) |
| AEG-008 | OpenWrt Rogue AP / DIY Wi-Fi Pineapple Lab | Parked | GL.iNet/OpenWrt controlled assessment and defenses; [notes](projects/openwrt-rogue-ap/README.md) |
| AEG-009 | Custom Reconnaissance Toolkit | Parked | [Notes](projects/custom-recon-toolkit/README.md) |
| **AEG-010** | **ESP32 GPS Wardriver** | Parked | [Scope](projects/esp32-gps-wardriver/README.md) |
| AEG-011 | Ethernet Assessment Appliance | Parked | LAN Turtle / Shark Jack-inspired authorized research; [notes](projects/ethernet-assessment-appliance/README.md) |
| AEG-012 | Evil Twin Defense Lab | Parked | [Notes](projects/evil-twin-defense/README.md) |
| AEG-013 | Web Application Security Lab | Parked | [Notes](projects/web-app-security/README.md) |
| AEG-014 | IoT Security Research Platform | Parked | [Notes](projects/iot-security/README.md) |
| AEG-015 | Flipper Zero Development Lab | Parked | [Notes](projects/flipper-development/README.md) |
| AEG-016 | AEGIS Sentinel — Desktop AI Companion | Deferred; hardware received | [Notes](projects/aegis-sentinel/README.md) |
| AEG-017 | Pico Ducky / HID Research | Parked | [Notes](projects/pico-ducky/README.md) |
| **AEG-018** | **Dedicated Wireless Analysis Station** | Parked | Portable Wi-Fi/BLE observation and diagnostics |
| **AEG-019** | **Standalone Network Diagnostics Console** | Parked | Touchscreen or headless network-health, DNS and interface diagnostics |
| **AEG-020** | **AEGIS Project Telemetry Integrations** | Parked | Read-only status summaries across separate AEGIS systems |

## Consolidated remote access scope — AEG-004

My **AEG-004 Portable LattePanda Remote Access Device** will be a portable, primarily headless authorized assessment/administration device, with a GUI available when needed. It is the single planned LattePanda remote-access device. Potential future design research includes Kali on local storage, WireGuard or authenticated reverse-SSH, reliable recovery, logging, defensive detection testing, cooling and an external battery option. The previous eight-hour battery target is a **design goal, not a validated specification**.

I am not planning a second remote-access platform. The newly assigned AEG-005 ESP32 Marauder and AEG-010 ESP32 GPS Wardriver are separate parked concepts. I will not buy additional hardware until this parked project's scope and budget are explicitly approved.

## Backlog management rules

1. Record the AEG number **when an idea is first registered**; consult [PROJECTS.md](PROJECTS.md) first.
2. Assign each distinct idea exactly one unique ID. The next unused number is **AEG-021**; maintain the consecutive sequence for future registrations.
3. A numbered idea may stay *Parked* indefinitely. Do **not** automatically create an issue, board card, branch, or purchase request merely because it has a number.
4. Prefer combining overlapping objectives into one project before assigning another ID. Keep redirects for historical links.
5. Perform active research only on owned/explicitly authorized systems, and publish sanitized engineering evidence.
6. Do not renumber AEG-002 or AEG-006, and keep Project NEXUS separate from APEX.

## Current execution focus

- **AEG-003:** Working Pwnagotchi build; capture, power and wireless-management acceptance findings are documented, including deferred items.
- **AEG-002 + AEG-006:** Resume RAK4631 inventory, firmware validation and Tactical Control Terminal live integration when the ordered kit arrives.
- **AEG-016:** Hardware received; companion build deferred.
- **AEG-004, AEG-005, AEG-007–AEG-015 and AEG-017–AEG-020:** Parked, without new procurement or GitHub Project board items.
