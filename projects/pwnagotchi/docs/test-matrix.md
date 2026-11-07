# AEG-003 — Test and Acceptance Matrix

**Last documented session:** 2026-11-06 (Central Time)  
**Project phase:** Testing  
I mark **Pass** only when I observed the behavior; **Partial** when a prerequisite passed but final acceptance remains open; **Deferred** when I chose not to repeat a test this session. An intermittent failure remains documented even if a later reboot restored service.

| Test | Check | Status | My evidence / follow-up |
|---|---|---|---|
| T01 | Pwnagotchi firmware boot | Pass | I booted jayofelony 64-bit v2.9.5.8 on Pi Zero 2 W |
| T02 | Waveshare V4 display | Pass | I observed faces, uptime, and status updating |
| T03 | Identity | Pass | The screen showed `aegis-pwn` |
| T04 | USB RNDIS | Pass | Windows detected the USB network device |
| T05 | USB SSH | Pass | I connected to the Pi using my established private USB link |
| T06 | PiSugar standalone power | Pass | I booted on PiSugar without USB after its short/long button sequence |
| T07 | PiSugar battery telemetry | Pass (live display) | I observed initial BAT 52% and subsequently saw data in the PiSugarX dashboard; an earlier I/O error was recorded |
| T08 | Saved capture exists | Pass (existence only) | I found a .pcap in `/etc/pwnagotchi/handshakes/` |
| T09 | PCAPNG structural and packet record validation | Pass (structural only) | I checked all nine PCAPNG block structures: 9/9 pass, 439 packet-bearing blocks in seven files, two files have zero packets; frame-level Wireshark dissection remains pending |
| T10 | Handshake completeness | Pending | `PWND 1` does not prove a complete four-way handshake |
| T11 | Clock and timezone | Partial | I manually corrected to America/Chicago; automatic NTP sync unverified |
| T12 | Service stability and reboot recovery | Partial — 10+ minute USB-powered check passed | I observed 14-minute OS uptime, active Pwnagotchi, and unchanged NRestarts=1 since 09:03:52; extended runtime and battery-only stability not established |
| T13 | PiSugar automatic low-battery shutdown/cutoff | Deferred | Firmware defaults specify 10% / 45 seconds; I have not tested real cutoff behavior |
| T14 | Battery endurance | Deferred | I chose not to repeat a timed standalone runtime test |
| T15 | Authenticated localhost-only dashboard | Pass | I confirmed auth and listener `127.0.0.1:8080` with an SSH tunnel |
| T16 | Bluetooth phone management | Pass | I used iPhone Termius SSH over Bluetooth PAN |
| T17 | Enclosure fit / clearance | Pending | Final dimensions and custom printed case are not validated |
| T18 | Public-document sanitization | Pass (current revision) | I reviewed docs to exclude real device addresses, personal network names, credentials and raw captures |
| T19 | AEGIS facial expressions | Partial | Configuration parsed, service active and two expressions observed; full set untested |
| T20 | Green dashboard theme | Pass | I confirmed RGB 159/232/112 (#9FE870) displays correctly |
| T21 | iPhone pair and trust | Pass | BlueZ showed Paired/Bonded/Trusted yes |
| T22 | Bluetooth PAN manual activation | Pass | My existing NetworkManager profile activated; `bnep0` received an IPv4 lease |
| T23 | iPhone SSH and browser tunnel | Pass | I used Termius SSH and opened my secure dashboard in Safari |
| T24 | Auto-reconnect after Bluetooth interruption | Deferred — known failure | Auto-reconnect failed in tests even after enabling NetworkManager autoconnect; I did not repeat the test after the recovery reboot |
| T25 | Controller/PAN recovery after reboot | Pass | After BlueZ hardware/HCI reset errors, I rebooted and remote management worked again |
| T26 | Alfa AWUS036ACM pre-purchase compatibility | Partial | I verified `mt76x2u` and required firmware on current kernel; hardware, OTG power and monitor mode not yet tested |

## Completion criteria

To call this project **Completed**, I will document repeatable boot/display behavior, a safe and tested shutdown path or explicitly accepted risk, accurate timestamps, authenticated management, authorized capture handling, and enclosure/power constraints. Password recovery or intrusive wireless activity is not a completion criterion.

## Notes on deferred checks

I consciously deferred battery endurance and an additional Bluetooth toggle test at the close of this session. **The initial failure remains a known limitation** until I demonstrate unattended recovery under repeatable conditions. I will retain USB SSH as a recovery method during future Alfa and networking modifications.

See the [build journal](build-journal.md) for my exact executed commands, observed results, and sanitized substitutes for private parameters.

| T27 | Manual safe shutdown and return to service | Pass | I ran `sudo shutdown -h now`, restarted the Pi, reconnected through Termius, confirmed `pwnagotchi` active and approximately one-minute uptime; PiSugar automatic low-battery cutoff remains untested |

| T28 | e-Paper live rendering after manual shutdown/restart | Pass | I captured two photos showing `aegis-pwn`, two different facial expressions, and changed screen messages after restarting; private PAN address is excluded from public docs; the on-screen uptime counter was 00:00:00 in both photographs |

| T29 | Live USB-to-PiSugar transition and 10-minute battery stability | Pass | I unplugged USB around 09:19 and remained battery-powered through 09:31:43 (12+ minutes); OS uptime 28 minutes, `throttled=0x0`, Pwnagotchi active, `NRestarts=1` unchanged; no observed reboot |
