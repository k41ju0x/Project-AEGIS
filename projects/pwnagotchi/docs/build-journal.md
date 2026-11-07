# AEG-003 — Pwnagotchi Build Journal

**Project phase:** Testing (user moved board item on 2026-11-06)  
**Hardware:** Raspberry Pi Zero 2 W (soldered 40-pin GPIO), Waveshare 2.13-inch e-Paper HAT V4, PiSugar 3 1200mAh, SanDisk 32GB microSD  
**Host:** Windows 11  
**Scope:** Owned or explicitly authorized wireless networks only. Raw captures, client MACs, SSIDs, credentials and private infrastructure details are excluded from the public repository.

## Session 1 — 2026-11-06: firmware and first boot
1. Installed Raspberry Pi Imager on Windows 11.
2. Selected jayofelony community image `pwnagotchi-64bit-2.9.5.8.img.xz`: https://github.com/jayofelony/pwnagotchi/releases/tag/v2.9.5.8
3. Flashed the 32GB microSD via Imager using **Use custom**. Windows ejected the device; reinserting exposed the FAT `bootfs` partition. Do not format Linux partitions when Windows prompts.
4. Created `bootfs/config.toml` and verified its contents via PowerShell `Get-Content`. Configuration included `main.name = "aegis-pwn"`, `ui.display.type = "waveshare_4"`, `main.plugins.pisugarx.enabled = true`, and a lab whitelist. **Do not commit real SSIDs or credentials.**
5. Mounted e-Paper HAT onto 40-pin header with power disconnected; checked GPIO alignment visually. First boot rendered `aegis-pwn` and animated face; uptime and on-screen status advanced, confirming display refresh and application operation.

## Session 2 — 2026-11-06: USB access and battery
1. Windows initially enumerated Pi gadget as serial COM3; later recognized it as **Raspberry Pi USB Remote NDIS Network Device** under **Ethernet 5**.
2. Verified SSH access over the point-to-point USB network. **Actual working IP addresses omitted** from public journal; keep them in private operational notes. Initial troubleshooting mistakenly assumed community default addresses and briefly disrupted the host adapter; restoring previously working addresses re-established SSH. Do not overwrite a verified network configuration simply to match examples.
3. Shut down through SSH before installing PiSugar 3 under the Zero 2 W. Mounted with supplied hardware and aligned pogo contacts.
4. PiSugar 3 required **short press followed by long press** to boot the Raspberry Pi without USB. The e-Paper screen resumed and displayed **BAT 52%**. This validates a battery-powered boot and initial charge telemetry; it does not establish endurance, charging behavior, low-battery shutdown or measurement accuracy.

## Session 3 — 2026-11-06: handshake artifact and logs
1. Display reported `PWND 1` for a nearby network. This is an application capture notification, **not** proof of access, password recovery, or a complete/valid four-way handshake.
2. Initial searches of `/home/pi/handshakes` and `/root/handshakes` showed that those paths did not exist.
3. `systemctl status pwnagotchi --no-pager -l` showed **active (running)** after one earlier failed start and systemd restart. Running process used `/opt/.pwn/bin/python3 /opt/.pwn/bin/pwnagotchi`.
4. Configuration `/etc/pwnagotchi/default.toml` identifies `/etc/pwnagotchi/handshakes` as the actual capture location. Application log at `/etc/pwnagotchi/log/pwnagotchi.log` confirms capture initialization and events with `handshakes=1`.
5. User subsequently confirmed a **.pcap file exists** at the configured capture location. Packet contents and handshake completeness have **not** yet been analyzed or validated.
6. Wireshark installed on Windows for offline analysis; successful import, EAPOL packet inspection, and any transfer of the file are **not yet confirmed**.
7. Device timestamps show **2026-08-18**, inconsistent with the actual build session date **2026-11-06**. Clock and timezone synchronization require verification before timeline or capture timestamps are relied upon.

## Useful read-only verification commands
```bash
systemctl status pwnagotchi --no-pager -l
sudo ls -lah /etc/pwnagotchi/handshakes/
sudo grep -n 'handshakes' /etc/pwnagotchi/default.toml
sudo tail -n 50 /etc/pwnagotchi/log/pwnagotchi.log
date -Is
timedatectl status
```

## Current assessment
**Verified:** OS boots; application and e-Paper display refresh; USB RNDIS and SSH worked; PiSugar 3 can power device standalone; battery percentage visible; a .pcap file exists; Wireshark installed on Windows.  
**Pending:** capture validation and permissions, time synchronization, battery endurance and safe shutdown, charging test, authenticated web UI, optional Bluetooth management, mechanical enclosure, and final test evidence.

**Safety:** No deauthentication or active association is needed for initial validation. Keep such behavior disabled unless operating in a specifically authorized, isolated test setting. Do not publish capture files or credentials.

## Session 4 — 2026-11-06: clock correction and next-stage selection
- Before intervention, `date -Is` reported `2026-08-18T19:12:03+01:00`; timezone `Europe/London`; NTP active but clock not synchronized.
- Applied `sudo timedatectl set-timezone America/Chicago`, and manually set UTC using the Windows 11 host over established USB SSH. Subsequent `date -Is`: **`2026-11-06T21:02:06-06:00`**, Central Standard Time. `timedatectl status`: timezone America/Chicago, **System clock synchronized: no**, NTP service active, no RTC. Thus date/time corrected manually, **automatic time sync remains unverified**. No service restart or reboot validation yet.
- Owner selected next feature work: customized display and personality, secure web dashboard, optional Bluetooth phone management, PiSugar low battery shut down and runtime, wireless telemetry/session statistics, plugin and log review. Priority is secure web dashboard inspection followed by controlled configuration updates and battery safeguards. Do not assume changing the software clock retroactively corrects prior PCAP timestamps.
