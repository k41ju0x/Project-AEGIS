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

## Session 5 — 2026-11-06: web dashboard verified
- `sudo ss -ltnp | grep ':8080'` showed Pwnagotchi listening on `*:8080` (PID 931 at observation).
- From Windows, user successfully opened an SSH tunnel using `ssh -L 8080:127.0.0.1:8080 pi@<private-USB-Pi-IP>` and browsed `http://127.0.0.1:8080`.
- User confirmed **dashboard appears**. Browser access is verified, but authentication is not yet verified. Listening on wildcard address means potential exposure through any reachable Pi interface; inspect effective web configuration and restrict access/authenticate as appropriate.
- Next: inspect the `[ui.web]` settings in `/etc/pwnagotchi/config.toml` without publishing any password; verify auth and binding before making a backup and controlled change.

## Session 6 — 2026-11-06: authenticated dashboard validation
- Added `[ui.web]` override to `/etc/pwnagotchi/config.toml` with `enabled = true`, `address = "127.0.0.1"`, `port = 8080`, `auth = true`, and user-selected private credentials (never committed). Backup taken prior to edit; syntax validation returned `TOML syntax valid`.
- After `sudo systemctl restart pwnagotchi`, `systemctl status pwnagotchi --no-pager -l` showed `active (running)`, launched at 21:12:54 CST.
- `sudo ss -ltnp | grep ':8080'` confirmed listener `127.0.0.1:8080`, not a wildcard address.
- User verified dashboard demanded login and accepted configured credentials through the existing Windows SSH tunnel. **Web dashboard security test passed.**
- Process appeared with `--manual`; operational mode should be confirmed rather than assuming active wireless operation.
- Next: back up before display/personality customization; test changes incrementally, preserving accessible recovery via SSH.

## Session 7 — AEGIS face customization validation
- User added custom `[ui.faces]` configuration and verified it parses with `sudo python3`/`tomllib`. Reported **22 facial-state/configuration entries**; this includes possible non-expression keys and should not be interpreted as 22 unique visible expressions.
- `sudo systemctl restart pwnagotchi` completed and `systemctl is-active pwnagotchi` returned **active**.
- User observed **two facial expressions** so far; display-state rendering works but all custom expressions are not individually validated. Face selection is state-driven; no intrusive wireless activity should be induced merely for appearance tests.
- Next: inspect effective web theme configuration, back up, apply reversible AEGIS green accent theme, check secured localhost-only dashboard remains authenticated.

## Session 8 — AEGIS green dashboard theme verified
- Backed up config and added `[ui.web.theme]` RGB accent `159, 232, 112` (`#9FE870`).
- User confirmed the custom theme works and the authenticated dashboard remains accessible after applying changes.
- Existing binding to `127.0.0.1:8080` had previously been verified; no report of a new listener check during this milestone.
- Next priority: inspect PiSugar 3 low-battery shutdown configuration before making changes; then validate battery endurance and optional Bluetooth tethering.

## PiSugar 3 shutdown settings inspection — 2026-11-06
- On-device `/etc/pwnagotchi/default.toml` `[main.plugins.pisugarx]` defaults: `enabled=false`, `lowpower_shutdown=true`, `lowpower_shutdown_level=10`, `shutdown_delay=45`, `max_charge_voltage_protection=false`.
- Read-only inspection of custom `/etc/pwnagotchi/config.toml`: `enabled=True` explicitly; remaining four settings not overridden, thus expected to inherit defaults (pending effective runtime verification).
- Initial interpretation: plugin enabled and default low-power shutoff configured, but graceful shutdown and 45-second controller cutoff are **not yet behaviorally validated**. Avoid destructive deep-discharge test. Next: examine PiSugar initialization/event logs and later safely confirm shutdown behavior.

## Session 9 — PiSugar 3 detection warning (2026-11-06)
- PiSugar plugin confirmed enabled in custom configuration; firmware default low-power shutdown threshold 10% and shutdown delay 45 seconds identified.
- User log excerpt from 21:27–21:29 CST repeatedly reports `No PiSugar device was found. Please check if the PiSugar device is powered on.` and `[PiSugarX] PiSugar is not ready`.
- Important correction: earlier battery-powered startup and the displayed 52% battery reading establish prior battery use/reporting, **not reliable current I²C communication or a functioning low-battery safety cutoff**.
- PiSugar official documentation warns that USB-connected Pi may illuminate PiSugar LEDs even if battery controller is not turned on. Other possible cause is intermittent pogo contact on underside GPIO solder pads.
- Next read-only tests: `ls -l /dev/i2c*` and `sudo i2cdetect -y 1`. PiSugar 3 expected I²C addresses `0x57` and `0x68`; do not adjust hardware under power. If not available, check PiSugar power-on sequence (short then long press) and contact only after safe shutdown.
- Reference: https://docs.pisugar.com/docs/product-wiki/pwnagotchi/intro ; https://docs.pisugar.com/docs/product-wiki/battery/faq

## Offline I²C diagnostic blocker — 2026-11-06
- `/dev/i2c-1` and `/dev/i2c-2` exist (Linux I²C device nodes available).
- `sudo i2cdetect -y 1` unavailable: `i2cdetect: command not found`.
- `sudo apt update` and `sudo apt install -y i2c-tools` failed with `Temporary failure resolving deb.debian.org` and `archive.raspberrypi.com`. USB SSH connectivity does not establish internet access; apt's 'All packages are up to date' message is based on stale/previous indexes, not a successful fetch.
- No i2c-tools installed; avoid changing known-working USB IP settings solely for this diagnostic.
- Next: inspect whether existing Pwnagotchi Python venv has `smbus2` or `smbus`; if available, perform targeted read-only test of expected PiSugar controller addresses. Battery device remains powered on per user correction.

## Session 10 — PiSugar I²C address detection (2026-11-06)
- Existing Python virtual environment contains both `smbus2` and `smbus` despite `i2c-tools` being unavailable offline.
- A targeted SMBus read of I²C bus 1 returned `[DETECTED] 0x57 - PiSugar battery controller` and `[DETECTED] 0x68 - PiSugar RTC`.
- This confirms both expected I²C addresses responded to read probes, reducing likelihood of a fully disconnected battery controller or missing I²C bus. It does **not** confirm reliable PiSugarX plugin connectivity or the low-power shutdown behavior.
- Next: inspect latest PiSugar plugin log entries and whether a PiSugar management systemd service exists, before performing service restarts or hardware changes.

## Session 11 — PiSugar 3 plugin recovered (2026-11-06)
- After repeated logs saying `No PiSugar device was found` and `[PiSugarX] PiSugar is not ready` through 21:31:20 CST, log shows `PiSugar3 is connected` at 21:31:25.664 and `PiSugar3 is ready` at 21:31:26.670 CST.
- `systemctl list-units --all --type=service | grep -i pisugar` returned no matching standalone service; plugin operation may be embedded in Pwnagotchi process.
- Combined with prior I²C probe detecting addresses `0x57` and `0x68`, this confirms successful software connection at least once. Sustained connectivity, current battery gauge, charging, graceful shutdown, and controller power cutoff are not yet verified.
- Next: review subsequent logs for reconnection errors and observe current battery percentage. Do not deep-discharge merely to test low-voltage cutoff.

## Session 12 — quiet application log after I²C read error (2026-11-06)
- User verified `date` at `2026-11-06 21:41:16 CST`; `systemctl is-active pwnagotchi` returned `active`.
- `journalctl -u pwnagotchi --since "5 minutes ago" --no-pager -n 40` returned `-- No entries --` (not independently evidence of a fault).
- Application log last modified at `2026-11-06 21:31:46.979999313 -0600`, approximately 9.5 minutes before observation. Its final entry was `[ERROR] ... read error[Errno 5] Input/output error`, following initial PiSugar3 connected/ready messages.
- Diagnosis remains open: systemd active, but unknown whether Pwnagotchi and PiSugar telemetry are continuing normally, whether application logging is simply quiet, or whether battery polling stalled. Next check process/thread state, available logs, and currently displayed BAT percentage before altering services.

## Session 13 — process-level validation (2026-11-06)
- User reports `ps` showing Bettercap PID 607, PwnGrid PID 850, Pwnagotchi launcher PID 9765, Python PID 9768 (`/opt/.pwn/bin/pwnagotchi --manual`), all running.
- `systemctl status pwnagotchi` confirms `Active: active (running)` since 21:26:01 CST, 18 tasks, Python process present. This establishes process/service liveness, not PiSugar sensor thread health.
- Battery telemetry remains unverified after last recorded plugin `read error[Errno 5]`. Next: inspect newest log timestamp, filtered PiSugar errors, Python thread count, and current WAVESHARE `BAT` percentage without changing service or USB network.
