# AEG-003 — Test and Acceptance Matrix

Updated: 2026-11-06. Status **Testing** as reported by project owner. A **Pass** means directly observed and supported by conversation; **Pending** means not yet verified.

| Test ID | Check | Status | Evidence / next action |
|---|---|---|---|
| T01 | Pi Zero 2 W boots Pwnagotchi 64-bit 2.9.5.8 | Pass | Boot and running process observed |
| T02 | Waveshare 2.13-inch V4 renders and refreshes | Pass | Face, uptime and status changed |
| T03 | Configured identity `aegis-pwn` shown | Pass | On-screen name seen |
| T04 | USB RNDIS detected on Windows | Pass | Ethernet 5 device present |
| T05 | SSH management connection | Pass | User restored and confirmed shell |
| T06 | PiSugar 3 standalone startup | Pass | Started without USB; short + long press |
| T07 | PiSugar charge reporting | Pass (basic) | Screen reported BAT 52%; accuracy not calibrated |
| T08 | Saved .pcap exists in configured directory | Pass (existence only) | `/etc/pwnagotchi/handshakes`; user reported file found |
| T09 | Capture imported and dissected in Wireshark | Pending | Check format, frame count and `eapol` in an authorized capture |
| T10 | Handshake integrity/completeness | Pending | Do not equate PWND counter with valid full handshake |
| T11 | Correct time, timezone and synchronization | Partial | Manually corrected to 2026-11-06 21:02 CST; `America/Chicago` set; `System clock synchronized: no`, NTP active but not synchronized; verify after reboot and when internet/time source available |
| T12 | Stable service over reboot and 30+ min | Pending | Earlier exit 1 followed by restart; inspect uptime and journal after reboot |
| T13 | PiSugar charging, cutoff and graceful shutdown | Pending | No forced discharges; test non-destructively with monitored power |
| T14 | Battery runtime | Pending | Log start/end percentages and uptime under repeatable loads |
| T15 | Secure browser dashboard access | Pass | Service active; bound to `127.0.0.1:8080`; dashboard required credentials and login succeeded over previously verified SSH tunnel (2026-11-06) |
| T16 | Bluetooth management (optional) | Not started | Verify supported phone tether implementation, protect remote access |
| T17 | Enclosure fitting and thermal clearance | Pending | Measure final physical stack before designing/printing |
| T18 | Sanitized public write-up and private evidence storage | In progress | Do not upload packet captures, home SSIDs, keys, clients/MACs |

## Suggested testing sequence
1. Verify clock: `date -Is` and `timedatectl status`; distinguish time-sync failure from retained old logs.
2. Inspect one already-saved **authorized** capture locally in Wireshark: count frames, check `eapol`, inspect 802.11 metadata. Do not publish the file or assume password access.
3. Verify health: `systemctl status pwnagotchi --no-pager -l` and `sudo tail -n 50 /etc/pwnagotchi/log/pwnagotchi.log`.
4. Measure battery endurance and confirm a safe shutdown path before using unattended.
5. Optionally enable secured web dashboard or phone management; then measure enclosure dimensions and photograph the final assembly.

## Acceptance threshold for Completed
Stable repeatable boot, display updates, safe standalone power and shutdown, correct timestamps, working management access, documented capture-storage behavior, and sanitized evidence in the build log. A recovered password or intrusive wireless interaction is **not** a completion requirement.

## Next phase scope — 2026-11-06
Owner selected display/personality customization, authenticated USB-only web UI, optional phone Bluetooth tether, PiSugar battery optimization and safe shutdown, and Wi-Fi research analysis. Implement sequentially: validate current web UI binding and authentication without opening public ports; back up and carefully change custom configuration; pair phone only after platform-specific tether documentation is checked; validate battery plugin's existing shutdown settings before any charge/discharge test. Preserve existing working USB address assignment. Firmware v2.9.5.8 defaults include `[ui.web]` enabled/port 8080/auth false and `[main.plugins.pisugarx]` lowpower_shutdown_level=10, but deployed effective settings need verification before asserting behavior.

| T19 | Custom AEGIS faces and personality | Partial | TOML validated, service active after restart, two facial expressions observed; complete set not individually verified |
| T20 | AEGIS web UI theme | Not started | Configure RGB accent after backup; retain localhost-only auth and SSH tunnel |
