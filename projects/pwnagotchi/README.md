# AEG-003 — Pwnagotchi

**Phase:** Operational build with outstanding acceptance limitations documented below.  
**Build date:** November 6, 2026 (America/Chicago)  
**Purpose:** My portable, battery-powered wireless-security research platform for networks I own or am authorized to assess.

## My build

| Item | Specification |
|---|---|
| Computer | Raspberry Pi Zero 2 W with soldered GPIO header |
| Display | Waveshare 2.13-inch e-Paper HAT V4 |
| Battery | PiSugar 3, 1200 mAh |
| Storage | SanDisk 32 GB microSD |
| Firmware | jayofelony Pwnagotchi 64-bit v2.9.5.8 |
| Host machine | Windows 11 |
| Hostname / on-screen identity | `aegis-pwn` |

I flashed the community firmware with Raspberry Pi Imager, assembled the e-Paper display and PiSugar battery, and confirmed the face and device status render correctly. PiSugar powered the Pi without USB and initially displayed **BAT 52%**. I verified nine stored PCAPNG files and structurally parsed all nine; seven contained 439 packet-bearing blocks in total. WPA handshake completeness has **not** been established.

## What I built and verified

- **USB recovery:** Windows recognizes the Raspberry Pi USB RNDIS device, and I can manage the Pi over SSH. My private USB subnet is deliberately not published.
- **Secure dashboard:** I configured Pwnagotchi's web interface to bind only to loopback (`127.0.0.1:8080`) with authentication. I access it through an SSH local port forward.
- **AEGIS personality:** I configured custom facial expressions (two visibly observed) and the AEGIS green web-theme accent (`#9FE870`).
- **Battery instrumentation:** I enabled PiSugarX, verified that the battery-controller and RTC I²C addresses respond, and viewed live telemetry in the plugin dashboard.
- **iPhone management:** I paired/trusted my iPhone, activated a Bluetooth PAN profile, connected with Termius SSH, and opened the authenticated dashboard from Safari over a Termius SSH forward.
- **Bluetooth recovery:** I diagnosed BlueZ/HCI controller errors during interrupted tethering. A controlled reboot restored iPhone connectivity and management.
- **Dual-radio expansion:** I considered the Alfa AWUS036ACM and verified software prerequisites, but subsequently decided it is **not required** for this build because Bluetooth provides management connectivity. No Alfa hardware was integrated.

## What remains open

- I completed a 12+ minute PiSugar battery-only stability check with no observed new restarts or undervoltage flags. Longer endurance and an additional Bluetooth interruption test remain deferred.
- Automatic shutdown at the inherited PiSugar 10% threshold and 45-second cutoff has **not** been behaviorally verified.
- Bluetooth tethering after a transient radio interruption previously failed to reconnect automatically; it later worked after a reboot. I have not claimed the intermittent failure is resolved.
- Timezone and clock were corrected manually to Central Time, but automatic time synchronization remains unverified.
- PCAPNG basic structural parsing passed; WPA handshake completeness, extended reliability, and enclosure design remain future acceptance items.

I consider the operational build complete; unresolved formal acceptance tests remain documented until I explicitly close or accept them. See my [chronological build journal and command record](docs/build-journal.md) and [test matrix](docs/test-matrix.md).

## Data-handling and reproducibility policy

I document actual command syntax with generic placeholders where necessary. **I do not publish** private USB/Bluetooth IP addresses, Bluetooth MAC addresses, personal device names, actual Wi-Fi SSIDs, passwords, SSH keys, or raw capture files. Loopback `127.0.0.1` and standard I²C addresses are included because they are non-sensitive technical constants.

### References

- [jayofelony Pwnagotchi v2.9.5.8](https://github.com/jayofelony/pwnagotchi/releases/tag/v2.9.5.8)
- [PiSugar Pwnagotchi documentation](https://docs.pisugar.com/docs/product-wiki/pwnagotchi/intro)
