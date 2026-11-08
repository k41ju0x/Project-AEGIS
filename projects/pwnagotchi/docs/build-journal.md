# AEG-003 — Pwnagotchi Build Journal

**Project phase:** Complete

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
5. I subsequently confirmed a **.pcap file exists** at the configured capture location. Packet contents and handshake completeness have **not** yet been analyzed or validated.
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
- I selected next feature work: customized display and personality, secure web dashboard, optional Bluetooth phone management, PiSugar low battery shut down and runtime, wireless telemetry/session statistics, plugin and log review. Priority is secure web dashboard inspection followed by controlled configuration updates and battery safeguards. Do not assume changing the software clock retroactively corrects prior PCAP timestamps.

## Session 5 — 2026-11-06: web dashboard verified
- `sudo ss -ltnp | grep ':8080'` showed Pwnagotchi listening on `*:8080` (PID 931 at observation).
- From Windows, I successfully opened an SSH tunnel using `ssh -L 8080:127.0.0.1:8080 pi@<PRIVATE_USB_IPV4>` and browsed `http://127.0.0.1:8080`.
- I confirmed **dashboard appears**. Browser access is verified, but authentication is not yet verified. Listening on wildcard address means potential exposure through any reachable Pi interface; inspect effective web configuration and restrict access/authenticate as appropriate.
- Next: inspect the `[ui.web]` settings in `/etc/pwnagotchi/config.toml` without publishing any password; verify auth and binding before making a backup and controlled change.

## Session 6 — 2026-11-06: authenticated dashboard validation
- Added `[ui.web]` override to `/etc/pwnagotchi/config.toml` with `enabled = true`, `address = "127.0.0.1"`, `port = 8080`, `auth = true`, and my selected private credentials (never committed). Backup taken prior to edit; syntax validation returned `TOML syntax valid`.
- After `sudo systemctl restart pwnagotchi`, `systemctl status pwnagotchi --no-pager -l` showed `active (running)`, launched at 21:12:54 CST.
- `sudo ss -ltnp | grep ':8080'` confirmed listener `127.0.0.1:8080`, not a wildcard address.
- I verified dashboard demanded login and accepted configured credentials through the existing Windows SSH tunnel. **Web dashboard security test passed.**
- Process appeared with `--manual`; operational mode should be confirmed rather than assuming active wireless operation.
- Next: back up before display/personality customization; test changes incrementally, preserving accessible recovery via SSH.

## Session 7 — AEGIS face customization validation
- I added custom `[ui.faces]` configuration and verified it parses with `sudo python3`/`tomllib`. Reported **22 facial-state/configuration entries**; this includes possible non-expression keys and should not be interpreted as 22 unique visible expressions.
- `sudo systemctl restart pwnagotchi` completed and `systemctl is-active pwnagotchi` returned **active**.
- I observed **two facial expressions** so far; display-state rendering works but all custom expressions are not individually validated. Face selection is state-driven; no intrusive wireless activity should be induced merely for appearance tests.
- Next: inspect effective web theme configuration, back up, apply reversible AEGIS green accent theme, check secured localhost-only dashboard remains authenticated.

## Session 8 — AEGIS green dashboard theme verified
- Backed up config and added `[ui.web.theme]` RGB accent `159, 232, 112` (`#9FE870`).
- I confirmed the custom theme works and the authenticated dashboard remains accessible after applying changes.
- Existing binding to `127.0.0.1:8080` had previously been verified; no report of a new listener check during this milestone.
- Next priority: inspect PiSugar 3 low-battery shutdown configuration before making changes; then validate battery endurance and optional Bluetooth tethering.

## PiSugar 3 shutdown settings inspection — 2026-11-06
- On-device `/etc/pwnagotchi/default.toml` `[main.plugins.pisugarx]` defaults: `enabled=false`, `lowpower_shutdown=true`, `lowpower_shutdown_level=10`, `shutdown_delay=45`, `max_charge_voltage_protection=false`.
- Read-only inspection of custom `/etc/pwnagotchi/config.toml`: `enabled=True` explicitly; remaining four settings not overridden, thus expected to inherit defaults (pending effective runtime verification).
- Initial interpretation: plugin enabled and default low-power shutoff configured, but graceful shutdown and 45-second controller cutoff are **not yet behaviorally validated**. Avoid destructive deep-discharge test. Next: examine PiSugar initialization/event logs and later safely confirm shutdown behavior.

## Session 9 — PiSugar 3 detection warning (2026-11-06)
- PiSugar plugin confirmed enabled in custom configuration; firmware default low-power shutdown threshold 10% and shutdown delay 45 seconds identified.
- My log excerpt from 21:27–21:29 CST repeatedly reports `No PiSugar device was found. Please check if the PiSugar device is powered on.` and `[PiSugarX] PiSugar is not ready`.
- Important correction: earlier battery-powered startup and the displayed 52% battery reading establish prior battery use/reporting, **not reliable current I²C communication or a functioning low-battery safety cutoff**.
- PiSugar official documentation warns that USB-connected Pi may illuminate PiSugar LEDs even if battery controller is not turned on. Other possible cause is intermittent pogo contact on underside GPIO solder pads.
- Next read-only tests: `ls -l /dev/i2c*` and `sudo i2cdetect -y 1`. PiSugar 3 expected I²C addresses `0x57` and `0x68`; do not adjust hardware under power. If not available, check PiSugar power-on sequence (short then long press) and contact only after safe shutdown.
- Reference: https://docs.pisugar.com/docs/product-wiki/pwnagotchi/intro ; https://docs.pisugar.com/docs/product-wiki/battery/faq

## Offline I²C diagnostic blocker — 2026-11-06
- `/dev/i2c-1` and `/dev/i2c-2` exist (Linux I²C device nodes available).
- `sudo i2cdetect -y 1` unavailable: `i2cdetect: command not found`.
- `sudo apt update` and `sudo apt install -y i2c-tools` failed with `Temporary failure resolving deb.debian.org` and `archive.raspberrypi.com`. USB SSH connectivity does not establish internet access; apt's 'All packages are up to date' message is based on stale/previous indexes, not a successful fetch.
- No i2c-tools installed; avoid changing known-working USB IP settings solely for this diagnostic.
- Next: inspect whether existing Pwnagotchi Python venv has `smbus2` or `smbus`; if available, perform targeted read-only test of expected PiSugar controller addresses. Battery device remains powered on per I correction.

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
- I verified `date` at `2026-11-06 21:41:16 CST`; `systemctl is-active pwnagotchi` returned `active`.
- `journalctl -u pwnagotchi --since "5 minutes ago" --no-pager -n 40` returned `-- No entries --` (not independently evidence of a fault).
- Application log last modified at `2026-11-06 21:31:46.979999313 -0600`, approximately 9.5 minutes before observation. Its final entry was `[ERROR] ... read error[Errno 5] Input/output error`, following initial PiSugar3 connected/ready messages.
- Diagnosis remains open: systemd active, but unknown whether Pwnagotchi and PiSugar telemetry are continuing normally, whether application logging is simply quiet, or whether battery polling stalled. Next check process/thread state, available logs, and currently displayed BAT percentage before altering services.

## Session 13 — process-level validation (2026-11-06)
- I checked `ps` and confirmed Bettercap, PwnGrid, Pwnagotchi launcher and Python processes were running (`/opt/.pwn/bin/pwnagotchi --manual`). PIDs are transient and omitted.
- `systemctl status pwnagotchi` confirms `Active: active (running)` since 21:26:01 CST, 18 tasks, Python process present. This establishes process/service liveness, not PiSugar sensor thread health.
- Battery telemetry remains unverified after last recorded plugin `read error[Errno 5]`. Next: inspect newest log timestamp, filtered PiSugar errors, Python thread count, and current WAVESHARE `BAT` percentage without changing service or USB network.

## Session 14 — Live PiSugarX telemetry visible (2026-11-06)
- Although application log remained at a one-off `[Errno 5] Input/output error` after `PiSugar3 is ready`, I opened the PiSugarX dashboard over the existing SSH tunnel and reported **all fields display data**.
- This supplies direct evidence that the plugin can retrieve and present battery-controller telemetry. I²C battery address 0x57 and RTC address 0x68 previously responded.
- Current status: PiSugarX telemetry **Pass (visible)**; long-term polling stability, charging behavior, safe shutdown at the inherited 10% threshold, and 45-second cutoff remain **unverified**. No forced deep-discharge test performed.
- Next: preserve working settings; proceed to Bluetooth tethering after confirming phone OS, since pairing/network configuration differs for Android and iOS.

## Alfa AWUS036ACM firmware prerequisite check — 2026-11-06
- I confirmed firmware searches found `/lib/firmware/mt7662_rom_patch.bin`, `/lib/firmware/mediatek/mt7662_rom_patch.bin`, `/lib/firmware/mt7662.bin`, and `/lib/firmware/mediatek/mt7662.bin`.
- Together with `modinfo mt76x2u` on kernel `6.18.39+rpt-rpi-v8`, this verifies the planned Alfa AWUS036ACM / MT7612U software driver and required firmware are present.
- **This is a prerequisite check, not hardware/monitor-mode acceptance.** Adapter not yet acquired/connected; device detection, actual monitor mode, Bettercap handoff, USB-OTG connection, PiSugar power capacity and remote management via onboard Wi-Fi still pending.
- Preferred design: USB Alfa for authorized monitoring, onboard Pi Wi-Fi for home LAN SSH/dashboard, preserve USB-gadget recovery until migration passes.

## Next milestone — Bluetooth remote management (2026-11-06)
- I intends to order Alfa AWUS036ACM for future dedicated monitor-mode use; **order not yet confirmed placed**. Firmware and driver prerequisites previously verified.
- Work continues on AEG-003 without waiting for adapter. Next goal: Bluetooth phone management as an alternate transport, preserving proven USB SSH recovery and existing Pwnagotchi settings.
- Initial non-destructive checks requested: `bluetoothctl list`, `sudo systemctl status bluetooth --no-pager -l`, `sudo rfkill list`. Phone OS not yet determined; pairing/PAN setup to be tailored after basic service inspection.

## Bluetooth controller readiness — 2026-11-06
- `bluetoothctl list` found controller `<PWNAGOTCHI_BLUETOOTH_MAC>` named `aegis-pwn` (MAC omitted from public build notes).
- `systemctl status bluetooth` returned Bluetooth service enabled and active, daemon BlueZ 5.82, management interface initialized, SDP server started.
- `rfkill list`: `hci0` Bluetooth soft/hard blocks both `no`; `phy0` WLAN soft/hard blocks both `no`.
- Service log timestamps start 2026-08-18, reflecting previously corrected system clock; configuration directory mode warning did not stop daemon startup.
- Bluetooth readiness **passed**, but pairing, Bluetooth PAN/network configuration, and phone-side management not yet tested. Next read-only `bluetoothctl show`; identify the phone OS to select correct networking approach. Preserve USB SSH recovery.

## Bluetooth pairing readiness — 2026-11-06
- `bluetoothctl show`: controller alias/name `aegis-pwn`, `Powered: yes`, `PowerState: on`, `Discoverable: no`, `Pairable: no`, `Discovering: no`, supports central and peripheral roles.
- Hardware and BlueZ operational; device intentionally not currently pairing or advertising. Bluetooth pairing and PAN/SSH transport **not yet configured or tested**. Temporary pairable/discoverable mode should be enabled only during actual pairing, and disabled afterwards.
- USB management SSH remains recovery path. At that point I had not yet selected the phone OS (Android/iPhone) to decide Bluetooth networking and verify PAN/tethering support before changes.

## iPhone Bluetooth pairing completed — 2026-11-06
- I checked `bluetoothctl` and confirmed **Paired: yes** and **Trusted: yes** for my iPhone. Do not publish device Bluetooth address in the public repo.
- Controller powered, service healthy, no rfkill blocks previously confirmed. Pairing milestone passed; Bluetooth PAN, IP, and SSH from the phone remain untested.
- Recommended temporary discoverability/pairability OFF after pairing; preserve USB-gadget SSH for recovery.
- Next diagnostic: inspect shape/enablement of firmware's `[main.plugins.bt-tether]` in default and custom TOML without printing secrets; list NetworkManager connections and `bnep0` if present. Configure only after identifying installed schema and avoid weakening `127.0.0.1:8080` authenticated dashboard binding.

## iPhone Bluetooth PAN profile discovered — 2026-11-06
- `bt-tether` settings inspected using Python TOML parser: plugin enabled in custom config and disabled in defaults, default/custom key sets include `auto_reconnect`, `fast_dhcp`, reconnect intervals/status display options. `devices` subtable absent in both; do not assume per-device TOML profile necessary.
- `nmcli -f NAME,TYPE,DEVICE connection show` showed `USB Gadget (shared)` active on `usb0`, loopback, inactive Bluetooth profile for paired iPhone (`<IPHONE_BLUETOOTH_PROFILE>`), and inactive `USB Gadget (client)`.
- `ip -br addr show bnep0`: interface does not exist, confirming PAN not presently active.
- Relevant upstream issue jayofelony/pwnagotchi #387 notes paired iPhones may not activate PAN automatically and suggests `sudo nmcli connection up "<iPhone Network>"` over existing USB recovery, followed by `ip -br addr show bnep0`, active NetworkManager profile and route check.
- Next: I will manually activate their existing Bluetooth profile while iPhone Personal Hotspot enabled; inspect result before enabling autoconnect or changing routes. No new connection or credential modifications yet.

## iPhone Bluetooth PAN activated successfully — 2026-11-06
- With my paired/trusted iPhone's Personal Hotspot enabled, I ran `sudo nmcli connection up "<IPHONE_BLUETOOTH_PROFILE>"` and NetworkManager responded: `Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/3)`.
- I checked the assigned PAN IP, active connection and routes. I kept the exact address private; successful iPhone-initiated SSH was verified in a later step.
- Status: **Bluetooth PAN activation passed**; direct SSH from iPhone, SSH-tunneled authenticated web dashboard, reconnection after reboot, and coexistence with USB recovery still need testing.
- Next: read `ip -4 -br addr show bnep0`; attempt SSH from iPhone with actual Bluetooth IP and existing credentials, preserving localhost-only dashboard binding and USB recovery.

## Bluetooth IPv4 address assigned — 2026-11-06
- I verified `ip -4 -br addr show bnep0` returned `bnep0 UNKNOWN [private Bluetooth PAN IPv4]/28` after activating existing paired iPhone PAN profile.
- IP assignment **passed**; interface UNKNOWN does not independently signify failure for Bluetooth PAN interfaces. iPhone-initiated SSH to port 22 at Bluetooth PAN IPv4 and dashboard SSH port-forward are **not yet tested**.
- Next: with iPhone Bluetooth and Personal Hotspot enabled and USB SSH preserved, connect with iOS SSH client using existing account; verify hostname `aegis-pwn`. Afterwards test authenticated dashboard via SSH localhost forward, keeping existing `127.0.0.1:8080` bind.
- I keep the actual Bluetooth-subnet address in private notes, not the public repository.

## iPhone direct SSH over Bluetooth — 2026-11-06
- I successfully connected from iPhone Termius to `aegis-pwn` via the established Bluetooth PAN and reports interactive control of Pwnagotchi.
- **Direct iPhone Bluetooth SSH acceptance: PASSED.** This establishes management access without relying on the Windows USB connection for the client session.
- I preserved USB SSH as my recovery path. At this stage, the localhost-only authenticated dashboard had not yet been tested through an iPhone tunnel; I later verified that access.
- Next: test whether iOS Termius supports local port forwarding to the authenticated local dashboard; do not rebind web UI to 0.0.0.0. Later test reconnect behavior after phone leaves range and returns.

## iPhone authenticated dashboard via Bluetooth SSH tunnel — 2026-11-06
- I confirmed Termius on iPhone successfully establishes SSH port forwarding over existing Bluetooth PAN, and the Pwnagotchi authenticated dashboard opens in Safari via local forwarded `127.0.0.1:8080`.
- **PASS:** I confirmed direct iPhone SSH, Bluetooth networking, SSH local forwarding and dashboard access. I kept the HTTP listener restricted to Pwnagotchi's loopback interface.
- Outstanding reliability acceptance: reconnect after iPhone leaves Bluetooth range, reconnect after Pi reboot, and confirm SSH tunnel availability after iOS background suspension; PiSugar automatic low-battery shutdown remains separately untested.

## iPhone Bluetooth reconnection failure — 2026-11-06
- I interrupted iPhone Bluetooth after verifying Termius SSH + SSH-tunneled Safari dashboard and reports **Bluetooth PAN does not automatically reconnect**.
- Previous direct SSH/dashboard success remains passed. **Reconnection reliability test failed**; not the same as initial pairing/activation.
- Firmware `bt-tether` enabled; existing NetworkManager Bluetooth profile `<IPHONE_BLUETOOTH_PROFILE>` previously activated using `nmcli connection up`.
- Next safe checks with USB SSH retained: re-enable iPhone Bluetooth + Personal Hotspot, manually reactivate existing profile, inspect `nmcli -g connection.autoconnect connection show "<IPHONE_BLUETOOTH_PROFILE>"` and set `connection.autoconnect yes` if false, inspect effective `[main.plugins.bt-tether]` `auto_reconnect`, retry with phone ready. Do not remove pairings, reset USB gadget, or change Pwnagotchi monitor interface. Note iPhone tether availability/backoff and potential reconnect delay.
- Reference: jayofelony/pwnagotchi issue #387 documents NetworkManager `connection.autoconnect yes` workaround.

## iPhone PAN autoconnect configuration fixed — 2026-11-06
- I manually reactivated iPhone Bluetooth profile successfully via `sudo nmcli connection up "<IPHONE_BLUETOOTH_PROFILE>"`.
- I found NetworkManager's profile had `connection.autoconnect=no` and changed it to `yes` via `sudo nmcli connection modify "<IPHONE_BLUETOOTH_PROFILE>" connection.autoconnect yes` and verified `yes`.
- Firmware's `bt-tether` config is enabled (`config.toml enabled=True`); auto_reconnect=True in default and custom files; reconnect_interval=60 s, reconnect_failure_cooldown=300 s.
- Likely mismatch resolved at configuration level; **automatic reconnection has not yet been retested or passed**. Next test: disable/re-enable iPhone Bluetooth with hotspot active, watch `nmcli connection show --active` and `ip -4 -br addr show bnep0` without manual `nmcli connection up`; confirm Termius SSH and forwarded dashboard after restoration.

## Bluetooth PAN autoconnect retest failed despite both settings — 2026-11-06
- I found the iPhone Bluetooth connection still **did not return automatically** after toggling Bluetooth off/on; manual `sudo nmcli connection up "<IPHONE_BLUETOOTH_PROFILE>"` was again required via USB SSH.
- NetworkManager profile `connection.autoconnect=yes` and Pwnagotchi bt-tether `auto_reconnect=true` (60-s interval, 300-s cooldown) had already been confirmed. Therefore configuration switches alone did not resolve issue.
- Upstream jayofelony/pwnagotchi issue #387 documents PAN activation failures and issue #604 (Aug 2026) documents some iOS Bluetooth reconnection failures; not proof of same root cause.
- Next diagnostic while PAN disconnected and before another manual activation: inspect recent `bt-tether`/Bluetooth/reconnect logs from `/etc/pwnagotchi/log/pwnagotchi.log` and `journalctl -u NetworkManager --since "10 minutes ago"` to determine which layer is failing. Preserve working USB-gadget SSH and paired iPhone. If no automatic connection attempts, consider scoped periodic reconnection helper with bounded retries, only for inactive PAN and no changes to monitor-mode Wi-Fi.

## Bluetooth PAN log root-cause investigation — 2026-11-06 late session
- I captured bt-tether and NetworkManager log excerpts (my diagnostic paste; do not publish Bluetooth MAC or private network IP).
- `bt-tether` at 23:01:40 detected drop, 23:01:47 NAP ready; 23:01:48 reports DBus NAP connection successful, PAN interface bnep0 active, and Bluetooth link reconnected.
- Simultaneously NetworkManager at 23:01:39–23:01:43 repeatedly attempted iPhone profile activation, failed `org.bluez.Error.Failed: Input/output error` / `bluetooth-failed`.
- Manual `nmcli connection up` at 23:06:03 succeeded; by 23:06:05 DHCPv4 lease, IPv4/IPv6 routes and DNS and NM active connection all established.
- Hypothesis: competition/race between bt-tether BlueZ NAP management and NetworkManager autoactivation, or PAN established without NM IP configuration. Not proven; do not disable or add reconnect mechanism without verifying state when plugin reports connected but management fails.
- Next test while disconnected from iPhone management but USB SSH preserved: inspect `nmcli -f DEVICE,TYPE,STATE,CONNECTION device status`, `nmcli -f NAME,TYPE,DEVICE connection show --active`, `ip -4 -br addr show bnep0` and `ip -4 route show dev bnep0`. Compare Bluetooth NAP plugin state against network layer. Additional observation: plugin upgrade entries around 23:07 are noted but no conclusions drawn.

## Bluetooth PAN reconnection state — post-interruption inspection (2026-11-06)
- Following unattended Bluetooth reconnection attempt, I observed `nmcli device status`: USB gadget `usb0` connected, loopback connected, `wlan0` unavailable (Pwnagotchi monitor configuration), no Bluetooth interface.
- `nmcli connection show --active`: only USB gadget and loopback. `ip -4 -br addr show bnep0`: device does not exist; `ip -4 route show dev bnep0`: cannot find device.
- This proves **PAN network interface absent at inspection time**, not merely DHCP without an address. Previous logs demonstrated bt-tether NAP connection on a prior attempt and NetworkManager auto-activation I/O errors; current Bluetooth link connection state has not yet been inspected.
- Next safe read-only check: `bluetoothctl devices Connected` / selected iPhone `bluetoothctl info` for Connected/Paired/Trusted and `journalctl -u bluetooth -u NetworkManager --since '5 minutes ago'` for BlueZ/NM failure. Keep USB recovery and avoid changing networking or forcing duplicate reconnect mechanisms until link state known.

## Bluetooth controller powered off during reconnection failures — 2026-11-06
- After BlueZ NAP errors `org.bluez.Error.NotReady: br-connection-adapter-not-powered` and bt-tether paused reconnection after five failed attempts, I checked `bluetoothctl show`: `Powered: no`, `PowerState: on`, `Discoverable: no`, `Pairable: yes`.
- `rfkill list bluetooth` showed `hci0` with soft block `no` and hard block `no`.
- BlueZ adapter `Powered: no` is consistent with the observed connection failure; exact cause of controller power state change remains unknown. Contrasting `PowerState: on` should not be treated as overriding `Powered: no`.
- Next non-destructive test with USB SSH intact: `sudo bluetoothctl power on`, re-check `Powered`, connected-device list and `bnep0`; avoid manual `nmcli connection up` until automatic response assessed. Investigate if controller turns off again; don't mark reconnection passed yet.

## Bluetooth controller refuses power-on — 2026-11-06
- After `bluetoothctl show` showed `Powered: no` and `PowerState: on`, I attempted `sudo bluetoothctl power on`.
- BlueZ emitted controller `PowerState: off-enabling` then `Failed to set power on: org.bluez.Error.Failed`; subsequent `show` remained `Powered: no`, `PowerState: on`.
- Earlier `rfkill` check indicated no soft/hard blocks and Bluetooth pairing remained intact. Root cause uncertain: BlueZ vs controller/firmware/transport initialization or competing management.
- Next non-destructive diagnostics requested: `sudo dmesg -T | grep -iE 'bluetooth|hci0|brcm|firmware|uart|timeout' | tail -n 50`, `sudo journalctl -u bluetooth --no-pager -n 40`, `systemctl is-active bluetooth`, `systemctl is-active hciuart`. Do not re-pair, change Wi-Fi/USB configuration, or create persistent restart services until logs evaluated. Maintain USB SSH recovery.

## Bluetooth HCI controller reset timeouts — 2026-11-06
- my `dmesg` after iPhone PAN reconnection failure shows Broadcom BCM43430B0 driver/firmware initializing at boot on UART `serial0-0`, then `Bluetooth: hci0: hardware error 0x00` at 23:09:08 and repeated `Opcode 0x0c03 failed: -110` (HCI reset timeouts) at 23:09:10, 23:09:12, and 23:19:36.
- bluetoothd service active; its journal records bnep0 disconnect 23:09 and later `Failed to set mode: Authentication Failed (0x05)` at 23:19. I observed `systemctl is-active hciuart` returns inactive. Because kernel `hci_uart_bcm serial0-0` already detected controller, inactive hciuart alone does not establish a misconfiguration; do not enable legacy hciuart or change UART overlays without further evidence.
- BlueZ controller earlier `Powered: no` despite no rfkill blocks; `sudo bluetoothctl power on` returned `org.bluez.Error.Failed`.
- Diagnosis: kernel/controller HCI reset timeout, not just PAN DHCP. Proposed one clean `sudo reboot` while USB recovery and adequate power are maintained, then verify `bluetoothctl show`, fresh kernel HCI errors, and whether iPhone PAN auto-reconnects without manual `nmcli connection up`. Actual outcome **pending**. No hardware resets, pairing deletion or boot firmware changes performed.

## Bluetooth connection recovered after controlled reboot — 2026-11-06
- Following Broadcom HCI reset timeouts and failed BlueZ controller power-on, I rebooted and confirmed **my iPhone reconnected**.
- This suggests reboot recovered controller/link connectivity. At this point in the session I had not yet verified the full post-reboot management path; I subsequently confirmed iPhone connectivity and remote access. Mark full PAN auto-reconnection and management tests **pending verification**, not passed.
- Next checks: `bluetoothctl show | grep 'Powered:'`, `nmcli -f NAME,TYPE,DEVICE connection show --active`, `ip -4 -br addr show bnep0`; verify Termius and Safari dashboard without manually activating NM.

## Bluetooth post-reboot recovery verified — 2026-11-06
- After controlled reboot following Broadcom Bluetooth HCI reset timeouts, I confirmed **iPhone connectivity and remote access work again** following requested verification of controller, NetworkManager PAN interface, Termius SSH and web dashboard.
- Acceptance: recovery after reboot **Passed**. Earlier failure to reconnect unattended after temporarily turning iPhone Bluetooth off/on remains a separate **open reliability issue**. A single post-reboot success does not establish reliable reconnection after transient losses or explain the controller hardware timeouts.
- Preserve existing paired/trusted phone, `connection.autoconnect=yes`, `bt-tether.auto_reconnect=true`, USB SSH recovery, and localhost-only authenticated web UI.

## Test scope decision — 2026-11-06
- I consider existing standalone PiSugar 3 battery-powered operation sufficient for current AEG-003 build stage and elects to **defer** another controlled battery endurance test.
- I also elected to **defer repeat Bluetooth interruption/reconnection tests** following successful post-reboot recovery of iPhone Termius SSH and SSH-tunneled dashboard.
- Evidence distinction preserved: battery can power device and live PiSugarX telemetry was displayed, but 10% automatic low-battery shutdown/cutoff and sustained runtime are not behaviorally verified; iPhone Bluetooth post-reboot recovery passed, but automatic recovery after ordinary out-of-range/toggle interruption had previously failed and is not claimed fixed.
- Current build/testing session can proceed without additional stress testing; retain noted limitations for future field checks if symptoms recur. Alfa AWUS036ACM was evaluated as an optional expansion but ultimately was not required for this completed build.

---

## Command record — executed checks and configuration (sanitized)

This appendix consolidates commands from my November 6 build and troubleshooting session. I preserved shell syntax where recorded and replaced **real addresses, device names, SSIDs and credentials** with placeholders. Where my session notes describe an action without its exact shell line (for example flashing the SD card through a GUI), I document that action as a procedure instead of inventing a command. Some commands initially failed; I retain the failures and their outcomes for reproducibility.

### 1. Image preparation, configuration and initial management

- Used Raspberry Pi Imager on Windows 11 to write `pwnagotchi-64bit-2.9.5.8.img.xz` to a 32 GB SanDisk microSD (GUI workflow; no shell flash command).
- Created `bootfs/config.toml` for the `aegis-pwn` identity, Waveshare display, PiSugar plugin and authorized-lab allowlist; real wireless identifiers omitted.
- Verified the boot configuration from Windows PowerShell:

```powershell
Get-Content <BOOTFS_DRIVE>:\config.toml
ssh pi@<PRIVATE_USB_IPV4>
```

- The Windows USB device appeared as Raspberry Pi USB RNDIS under Ethernet 5. I kept the working USB addresses in private notes rather than copying assumed community defaults into the system.

### 2. Core service, capture and system clock

```bash
systemctl status pwnagotchi --no-pager -l
sudo ls -lah /etc/pwnagotchi/handshakes/
sudo grep -n 'handshakes' /etc/pwnagotchi/default.toml
sudo tail -n 50 /etc/pwnagotchi/log/pwnagotchi.log
date -Is
timedatectl status
sudo timedatectl set-timezone America/Chicago
```

I manually corrected the date/time using the Windows host as my time source. The exact manual UTC-setting command was not retained in the session record; I won't invent it. **NTP remained active but unsynchronized** when checked. I confirmed only that a PCAP exists, not its handshake validity.

### 3. Secure web dashboard

```bash
sudo ss -ltnp | grep ':8080'
ssh -L 8080:127.0.0.1:8080 pi@<PRIVATE_USB_IPV4>   # On Windows
sudo cp /etc/pwnagotchi/config.toml /etc/pwnagotchi/config.toml.bak
sudo nano /etc/pwnagotchi/config.toml
sudo chown root:root /etc/pwnagotchi/config.toml
sudo chmod 600 /etc/pwnagotchi/config.toml
sudo systemctl restart pwnagotchi
systemctl status pwnagotchi --no-pager -l
sudo ss -ltnp | grep ':8080'
```

My effective configuration restricted the interface to loopback and required authentication. I used a unique password but **did not record the username or password in GitHub**.

```toml
[ui.web]
enabled = true
address = "127.0.0.1"
port = 8080
auth = true
# Username and password are intentionally omitted from this public example.
```

I checked TOML syntax using Python's `tomllib` under `sudo`, since the config was root-readable only:

```bash
sudo python3 - <<'PY'
import tomllib
with open('/etc/pwnagotchi/config.toml', 'rb') as f:
    config = tomllib.load(f)
print("TOML syntax valid")
PY
```

I confirmed the dashboard demanded credentials via the SSH tunnel and that `ss` showed `127.0.0.1:8080`, not a wildcard listener.

### 4. Display faces and AEGIS theme

```bash
sudo grep -A 45 '^\[ui.faces\]' /etc/pwnagotchi/default.toml
sudo cp /etc/pwnagotchi/config.toml /etc/pwnagotchi/config.toml.pre-aegis-faces.bak
sudo nano /etc/pwnagotchi/config.toml
```

I added a custom `[ui.faces]` section. The following check initially failed without `sudo` because I protected `config.toml` with root-only read permissions; rerunning it as root succeeded and reported 22 configuration entries.

```bash
sudo python3 - <<'PY'
import tomllib
with open('/etc/pwnagotchi/config.toml', 'rb') as f:
    config = tomllib.load(f)
faces = config.get('ui', {}).get('faces', {})
print("TOML syntax valid")
print(f"Configured facial states: {len(faces)}")
PY
sudo systemctl restart pwnagotchi
systemctl is-active pwnagotchi
```

I observed two expressions on the e-Paper screen. Then I backed up the configuration again and applied the web accent:

```bash
sudo cp /etc/pwnagotchi/config.toml /etc/pwnagotchi/config.toml.pre-web-theme.bak
sudo nano /etc/pwnagotchi/config.toml
```

```toml
[ui.web.theme]
accent_r = 159
accent_g = 232
accent_b = 112
```

```bash
sudo python3 - <<'PY'
import tomllib
with open('/etc/pwnagotchi/config.toml', 'rb') as f:
    config = tomllib.load(f)
print("TOML valid")
print("Web theme:", config.get("ui", {}).get("web", {}).get("theme"))
PY
sudo systemctl restart pwnagotchi
systemctl is-active pwnagotchi
```

The authenticated dashboard displayed the AEGIS green theme successfully.

### 5. PiSugar 3 battery troubleshooting

```bash
sudo grep -A 8 '^\[main.plugins.pisugarx\]' /etc/pwnagotchi/default.toml
sudo python3 - <<'PY'
import tomllib
with open('/etc/pwnagotchi/config.toml', 'rb') as f:
    config = tomllib.load(f)
plugin = config.get("main", {}).get("plugins", {}).get("pisugarx", {})
for key in ("enabled", "lowpower_shutdown", "lowpower_shutdown_level",
            "shutdown_delay", "max_charge_voltage_protection"):
    print(f"{key}: {plugin.get(key, 'inherited from defaults')}")
PY
sudo grep -iE 'pisugar|lowpower|battery|shutdown' /etc/pwnagotchi/log/pwnagotchi.log | tail -n 30
ls -l /dev/i2c*
sudo i2cdetect -y 1             # Failed: i2cdetect not installed
sudo apt update                 # Failed: no repository DNS via USB gadget
sudo apt install -y i2c-tools   # Failed: unable to download dependencies
```

Both `smbus2` and `smbus` were already installed in the Pwnagotchi Python environment, allowing an offline targeted probe:

```bash
sudo /opt/.pwn/bin/python3 - <<'PY'
import importlib.util
for module in ("smbus2", "smbus"):
    print(f"{module}: {'available' if importlib.util.find_spec(module) else 'not installed'}")
PY

sudo /opt/.pwn/bin/python3 - <<'PY'
from smbus2 import SMBus
devices = {0x57: "PiSugar battery controller", 0x68: "PiSugar RTC"}
with SMBus(1) as bus:
    for address, name in devices.items():
        try:
            bus.read_byte(address)
            print(f"[DETECTED] 0x{address:02X} - {name}")
        except OSError as error:
            print(f"[NOT RESPONDING] 0x{address:02X} - {name}: {error}")
PY
```

Both I²C addresses responded. The plugin initially reported "No PiSugar device was found", then "PiSugar3 is connected" and "PiSugar3 is ready", followed by one `read error[Errno 5]`. I inspected the service and log state:

```bash
sudo grep -iE 'pisugar|battery' /etc/pwnagotchi/log/pwnagotchi.log | tail -n 15
sudo grep -iE 'PiSugar3 is ready|PiSugar3 is connected|PiSugar is not ready|No PiSugar device' /etc/pwnagotchi/log/pwnagotchi.log | tail -n 12
sudo tail -n 40 /etc/pwnagotchi/log/pwnagotchi.log
date '+%Y-%m-%d %H:%M:%S %Z'
systemctl is-active pwnagotchi
sudo journalctl -u pwnagotchi --since "5 minutes ago" --no-pager -n 40
sudo stat -c 'Last log update: %y' /etc/pwnagotchi/log/pwnagotchi.log
ps -eo pid,ppid,stat,etime,cmd | grep -E '[p]wnagotchi|[p]isugar'
sudo systemctl status pwnagotchi --no-pager -l
ps -p <PWNAGOTCHI_PYTHON_PID> -o pid,stat,nlwp,etime,%cpu,%mem,cmd
systemctl list-units --all --type=service | grep -i pisugar
```

I then opened the PiSugarX dashboard through the authenticated local SSH tunnel and saw live battery data. The inherited defaults specify shutdown at 10% and a 45-second delay, but **I did not execute a real low-battery shutdown test**.

### 6. Alfa AWUS036ACM software prerequisites

```bash
uname -r
modinfo mt76x2u | head -n 12
for file in mt7662_rom_patch.bin mt7662.bin; do
    echo "Checking: $file"
    find /lib/firmware -name "$file" -print
done
```

Kernel `6.18.39+rpt-rpi-v8` contains the `mt76x2u` module, and I found both firmware files. I also mistakenly attempted to execute the compressed `.ko.xz` driver file and received `Permission denied`; this is a kernel module, not a shell program. I have not yet attached an Alfa adapter.

### 7. Bluetooth controller, iPhone pairing and PAN networking

```bash
bluetoothctl list
sudo systemctl status bluetooth --no-pager -l
sudo rfkill list
bluetoothctl show
sudo bluetoothctl
```

During interactive pairing I used the applicable `bluetoothctl` commands:

```text
power on
agent on
default-agent
pairable on
discoverable on
scan on
devices
pair <IPHONE_BLUETOOTH_MAC>
trust <IPHONE_BLUETOOTH_MAC>
info <IPHONE_BLUETOOTH_MAC>
scan off
discoverable off
pairable off
quit
```

I verified `Paired: yes`, `Trusted: yes`, and later `Bonded: yes`. I do not publish the phone's Bluetooth MAC or personal device name. An attempt to run `scan off` returned an error once; I continued by checking the actual controller state.

I inspected plugin settings without printing credentials or phone identifiers:

```bash
sudo python3 - <<'PY'
import tomllib
for path in ("/etc/pwnagotchi/default.toml", "/etc/pwnagotchi/config.toml"):
    with open(path, "rb") as f:
        config = tomllib.load(f)
    bt = config.get("main", {}).get("plugins", {}).get("bt-tether", {})
    print(path, "keys:", sorted(bt.keys()))
    print("enabled:", bt.get("enabled", "inherited"))
    print("device profiles:", sorted(bt.get("devices", {}).keys()))
PY
nmcli -f NAME,TYPE,DEVICE connection show
ip -br addr show bnep0
sudo nmcli connection up "<IPHONE_BLUETOOTH_PROFILE>"
ip -4 -br addr show bnep0
nmcli -f NAME,TYPE,DEVICE connection show --active
ip route
```

Manual profile activation succeeded and assigned a private Bluetooth PAN address. From the iPhone, I connected with Termius over SSH, then used a Termius local port forward to open `http://127.0.0.1:8080` in Safari.

### 8. Bluetooth reconnection troubleshooting

When automatic reconnection failed after I turned iPhone Bluetooth off and back on, I inspected and updated NetworkManager's profile:

```bash
nmcli -g connection.autoconnect connection show "<IPHONE_BLUETOOTH_PROFILE>"
sudo nmcli connection modify "<IPHONE_BLUETOOTH_PROFILE>" connection.autoconnect yes
nmcli -g connection.autoconnect connection show "<IPHONE_BLUETOOTH_PROFILE>"
```

I also verified that the Pwnagotchi `bt-tether` plugin was enabled with `auto_reconnect=true`, a 60-second retry interval and a 300-second failure cooldown. The next interruption test still failed without manual activation.

```bash
sudo grep -iE 'bt-tether|bluetooth|reconnect|PAN|NAP' /etc/pwnagotchi/log/pwnagotchi.log | tail -n 35
sudo journalctl -u NetworkManager --since "10 minutes ago" --no-pager -n 60
nmcli -f DEVICE,TYPE,STATE,CONNECTION device status
nmcli -f NAME,TYPE,DEVICE connection show --active
ip -4 -br addr show bnep0
ip -4 route show dev bnep0
bluetoothctl devices Connected
bluetoothctl devices Paired
bluetoothctl info <IPHONE_BLUETOOTH_MAC>
sudo journalctl -u bluetooth -u NetworkManager --since "5 minutes ago" --no-pager -n 50
sudo grep -iE 'bt-tether|NAP|reconnect|bluetooth' /etc/pwnagotchi/log/pwnagotchi.log | tail -n 25
bluetoothctl show | grep -E 'Powered:|PowerState:|Discoverable:|Pairable:'
sudo rfkill list bluetooth
sudo bluetoothctl power on        # Failed: org.bluez.Error.Failed
sudo dmesg -T | grep -iE 'bluetooth|hci0|brcm|firmware|uart|timeout' | tail -n 50
sudo journalctl -u bluetooth --no-pager -n 40
systemctl is-active bluetooth
systemctl is-active hciuart
```

The logs showed NetworkManager BlueZ NAP I/O errors, `bt-tether` reporting a temporary NAP success without sustained connectivity, then `org.bluez.Error.NotReady: br-connection-adapter-not-powered`. The controller reported `Powered: no` without an `rfkill` block. Kernel `hci0` reported Broadcom hardware errors and HCI Reset opcode `0x0c03` timeouts (`-110`). A controlled reboot restored Bluetooth operation:

```bash
sudo reboot
# Reconnected through my established USB SSH recovery path
bluetoothctl show | grep 'Powered:'
nmcli -f NAME,TYPE,DEVICE connection show --active
ip -4 -br addr show bnep0
```

I verified iPhone management was working again. **I did not repeat the Bluetooth toggle/reconnection test afterward**, and I have not claimed this intermittent failure is permanently fixed.

### 9. Closeout and outstanding work

I elected to defer a further standalone battery endurance test and repeat Bluetooth-interruption test for this session. These decisions do **not** replace evidence for an automatic low-power shutdown, stable reconnection after an interrupted link, validated capture completeness, or a physical Alfa monitor-mode test.

At the time of this test session, the project was in **Testing**. I subsequently marked the operational build **Complete** on November 7, 2026. I will return to these optional acceptance items when needed; I will preserve the USB recovery path and keep secret values out of the public repository.

## Final acceptance — post-startup management and clock check (2026-11-07)
- I booted AEG-003 and successfully connected using Termius over the existing iPhone management setup.
- I inspected the system date from my terminal and confirmed it was correct after startup. This supports boot-time clock/date retention and management connectivity, **but does not yet verify automatic NTP synchronization**.
- Next I will check `systemctl is-active pwnagotchi`, `systemctl is-active bluetooth`, `systemctl is-active NetworkManager`, and `sudo journalctl -b -p err --no-pager -n 20` to establish service health after boot.

## Final acceptance — services and boot-error review (2026-11-07)
- From my post-boot Termius SSH session, I ran `systemctl is-active pwnagotchi`, `systemctl is-active bluetooth`, and `systemctl is-active NetworkManager`. All three returned `active`.
- I reviewed `sudo journalctl -b -p err --no-pager -n 20`. Entries included ALSA udev missing-GOTO-label warnings, VCHI/MMAL multimedia initialization failures (`-22`), Broadcom `brcmfmac` monitor-interface creation messages for `wlan0mon`, and `dhcpcd is not running`.
- I confirmed the core services start and Bluetooth SSH management works despite these messages. I did not disable drivers, alter audio/multimedia modules, or replace NetworkManager. The log alone does not establish any operational impact from the multimedia or dhcpcd entries.
- Acceptance outcome: **startup/service availability passed**. Extended-duration reliability remains distinct and untested in this checkpoint.

## Final acceptance — capture file inventory (2026-11-07)
- After reboot I ran `sudo ls -lh /etc/pwnagotchi/handshakes/` and confirmed **nine nonempty `.pcapng` captures**, with displayed sizes ranging from 128 bytes to approximately 83 KiB. A `cache/` subdirectory was also present.
- I also ran `sudo find /etc/pwnagotchi/handshakes/ -maxdepth 1 -type f -name '*.pcap' -printf '%f — %s bytes\n'`; it printed no results because the stored files use the `.pcapng` extension rather than `.pcap`.
- Several file timestamps still reflect the historical pre-clock-correction date of 2026-08-18; I do not treat these as reliable evidence of actual capture time.
- **PASS:** stored capture files persist after startup. **PENDING:** validate file structure and packet/handshake content. I omit real capture filenames, SSIDs, and MAC-like identifiers from this public document.
- Next commands: `sudo find /etc/pwnagotchi/handshakes/ -maxdepth 1 -type f -name '*.pcapng' -printf '%s bytes\n' | sort -n`, `sudo file /etc/pwnagotchi/handshakes/*.pcapng` (output requires sanitization if publishing), and `command -v tshark || echo 'tshark not installed'`.

## Final acceptance — PCAPNG recognition and sizes (2026-11-07)
- I ran `sudo find /etc/pwnagotchi/handshakes/ -maxdepth 1 -type f -name '*.pcapng' -printf '%s bytes\n' | sort -n` and observed nine nonempty files: 128, 256, 832, 900, 1,940, 1,980, 12,856, 16,256 and 84,880 bytes (120,028 bytes total).
- I ran `sudo file /etc/pwnagotchi/handshakes/*.pcapng`; all nine were recognized as `pcapng capture file - version 1.0`. I omit SSIDs, address-derived filename suffixes and filenames from this public record.
- `command -v tshark || echo 'tshark not installed'` returned `tshark not installed`.
- **PASS:** all nine have recognizable PCAPNG headers/format and are nonzero-sized. **NOT YET PASSED:** complete block integrity, presence of actual packet records and EAPOL/four-way handshake validation; the 128-byte file might contain headers only. Next test uses only installed tools to assess block structure; no package installation necessary.

## Final acceptance — PCAPNG structural integrity and packet counts (2026-11-07)
- I ran a local, read-only Python 3 PCAPNG block parser over nine captures. It inspected each block's header, byte-order magic, 32-bit block length, four-byte alignment, bounds, and repeated trailer length. I counted packet-bearing block types 2, 3 and 6, without decoding actual Wi-Fi frames or publishing capture identifiers.
- The nine outputs were: capture 1 **PASS**, 295 blocks / 293 packet-bearing blocks; capture 2 **PASS**, 2 blocks / 0 packets; capture 3 **PASS**, 11 blocks / 9 packets; capture 4 **PASS**, 4 blocks / 0 packets; capture 5 **PASS**, 9 blocks / 7 packets; capture 6 **PASS**, 59 blocks / 57 packets; capture 7 **PASS**, 4 blocks / 2 packets; capture 8 **PASS**, 5 blocks / 3 packets; capture 9 **PASS**, 70 blocks / 68 packets.
- Summary: **9/9 files structurally parsed, 7 files with packet-bearing blocks, 2 without, 439 packet-bearing blocks total**. The two zero-packet captures contain valid PCAPNG structure but no packet records; I do not claim they contain usable capture evidence.
- **PASS:** PCAPNG basic structural checks and the existence of packet-bearing records. **NOT YET VERIFIED:** detailed packet decoding, EAPOL frame presence, four-way handshake completeness, or the validity of historical timestamps.
- Validation command was a read-only, standard-library Python PCAPNG parser (`struct`, `pathlib`) run with `sudo python3`, operating over `/etc/pwnagotchi/handshakes/*.pcapng`; all nine printed `Capture N: PASS | blocks=X | packets=Y`. See the acceptance matrix for limitations.

## Final acceptance — controlled shutdown and boot (2026-11-07)
- I executed `sudo shutdown -h now` from my existing Termius SSH management session and observed that the Pi shut down normally.
- After restarting with the existing PiSugar procedure, I reconnected over Termius and ran `systemctl is-active pwnagotchi` and `uptime`.
- Results: `active`; `08:54:37 up 1 min, 1 user, load average: 0.61, 0.28, 0.10`. A fresh uptime and working Termius session confirm successful startup and working remote administration.
- **PASS:** manual orderly shutdown, reboot, Pwnagotchi service startup, and remote SSH access. The e-Paper update after this restart was not separately reported at this checkpoint. **NOT TESTED:** automatic low-battery shutdown at the PiSugar 10% setting or battery-controller delayed power cutoff; these are distinct from Linux `shutdown -h now`.

## Final acceptance — e-Paper restart and live display evidence (2026-11-07)
- After I performed a controlled Linux shutdown, restarted from PiSugar power and confirmed Termius SSH and the Pwnagotchi service were working, I photographed the Waveshare 2.13-inch V4 display twice.
- The two photos show my `aegis-pwn` identity, two distinct custom facial expressions and changing screen messages (from a session-log reading state to the normal personality greeting), establishing that the e-Paper interface was operating and updating after restart.
- Battery percentages visible in the photos are approximately 46% and 51%, demonstrating the percentage is displayed but **not establishing accurate state-of-charge measurement or charging behavior**. Both pictures show on-screen `UP 00:00:00`; I did not separately verify that this UI counter advances. Linux `uptime` had already reported one minute after restart.
- The display also showed a private Bluetooth PAN address. I **did not include that address** in this public journal or commit the photographs. Before publishing any images I will redact/crop private device/network identifiers, SSIDs and capture information.
- **PASS:** e-Paper renders and changes faces/messages after controlled shutdown and restart, while SSH and the Pwnagotchi service are functional. **OPEN:** PiSugar automatic low-battery cutoff and on-screen uptime counter observation.

## Final acceptance — startup application crash versus Linux reboot (2026-11-07)
- While using USB external power with PiSugar 3 charging, I ran `sudo systemctl show pwnagotchi -p NRestarts -p ExecMainStartTimestamp -p ActiveEnterTimestamp`. It reported `NRestarts=1`, both timestamps `2026-11-07 09:03:52 CST`.
- `sudo journalctl -u pwnagotchi -b --no-pager -n 50` showed Pwnagotchi started at 09:02:51, exited `status=1/FAILURE` at 09:03:10, and was restarted by systemd at 09:03:52. Subsequent plugin initialization activated `bnep0` and dhcpcd successfully leased a Bluetooth PAN address at 09:04:12 (actual IP omitted here).
- I ran `uptime` at 09:11:22 and observed **8 minutes**. This differentiates the Pwnagotchi service restart within the current boot from an entire OS reboot: the Pi remained running after the app crash. My earlier 09:03 uptime reflected a separate new Linux boot, but the prior reboot cause remains unproven due to absent persistent journal history.
- The bt-tether plugin invoked `dhcpcd` even though NetworkManager is active. Possible interface management conflict remains a hypothesis, **not** confirmed as the application failure cause. No configuration changes or network-service shutdowns performed.
- Next: inspect application error/exception lines around 09:02–09:03. The initial error is **unresolved**; do not mark overall power/runtime stability passed merely on an eight-minute uptime sample.

## Final acceptance — systemd startup-failure window checked (2026-11-07)
- I ran `sudo journalctl -u pwnagotchi -b --since "2026-11-07 09:02:45" --until "2026-11-07 09:03:15" --no-pager`.
- It showed only the service starting at 09:02:51, the main process exiting at 09:03:10 with `status=1/FAILURE`, systemd recording `Failed with result 'exit-code'`, and 9.103s of CPU time; **no application exception or failure cause** appeared in this systemd slice.
- Next I will inspect `/etc/pwnagotchi/log/pwnagotchi.log` around 09:03 and any traceback/exception details, without altering the working setup or publicly revealing network identifiers.

## Final acceptance — application log around startup failure (2026-11-07)
- I inspected `/etc/pwnagotchi/log/pwnagotchi.log` around the systemd-reported startup failure. At 09:03:01, Pwnagotchi initialized `Fix_Services`, PiSugar 3, auto-backup, GPS plugin, update plugin, PiSugarX, web configuration and Bluetooth tether. The Waveshare v2in13_V4 display initialized by 09:03:07. The local web server began listening on `127.0.0.1:8080`, and the main thread connected to Bettercap's localhost API and detected monitor interface `wlan0mon` around 09:03:08–09:03:09.
- The earlier systemd journal reports `status=1/FAILURE` at 09:03:10. The pasted application excerpt did **not** include a fatal Python traceback or confirmed root cause. The next displayed startup header in the application log is 09:04:00 following systemd's service restart at 09:03:52.
- A previous-night `pwnmail` inbox `Exception: not connected` is unrelated by timestamp and must not be attributed to the 09:03 crash without corroboration.
- Investigating startup sequencing or plugin activity is reasonable, but a Bettercap race or plugin error is **not yet confirmed**. I will keep the current working USB-powered setup intact and inspect only the narrow crash window and Bettercap service logs before altering configuration. No private phone names, MAC addresses, SSIDs, or PAN IPs included here.

## Final acceptance — narrow startup-crash logs inconclusive (2026-11-07)
- I checked `sudo grep '2026-11-07 09:03:' /etc/pwnagotchi/log/pwnagotchi.log | tail -n 35` and `sudo journalctl -b --since '2026-11-07 09:03:00' --until '2026-11-07 09:03:15' --no-pager -p warning`.
- Pwnagotchi initialized PiSugar 3, Waveshare e-paper, localhost web service, Bettercap API connection and `wlan0mon` successfully just before exiting; the Bluetooth tether plugin was attempting to establish its paired iPhone connection. Systemd emitted only `pwnagotchi.service: Failed with result 'exit-code'` at 09:03:10. No causal traceback or fatal application message was found in the supplied crash-window excerpt.
- I will treat Bluetooth initialization as a possible lead, **not an established root cause**. Before altering plugin or network settings I will verify whether the service restart counter increases during stable USB-powered operation. Keep prior unexpected whole-system reboot and one application crash distinguished.

## Final acceptance — USB-powered service stability after crash recovery (2026-11-07)
- With the Pi on external USB power and PiSugar 3 charging, I ran `uptime` at 09:16:51 CST: `up 14 min, 1 user, load average: 0.23, 0.22, 0.13`.
- `systemctl show pwnagotchi -p ActiveState -p NRestarts -p ExecMainStartTimestamp` reported `ActiveState=active`, `NRestarts=1`, and `ExecMainStartTimestamp=Sat 2026-11-07 09:03:52 CST`.
- The restart counter was **unchanged** from the previous checkpoint. The service had stayed up for approximately 13 minutes after its automatic restart, with the OS up 14 minutes. **PASS:** short-term (10+ minute) USB-powered post-recovery application stability. **NOT YET CONFIRMED:** battery-only stability, extended runtime, and root cause of earlier full reboot or startup failure.
- I preserved the working configuration and USB recovery path rather than changing network management, plugin or PiSugar settings without a proven cause.

## Final acceptance — live USB-to-PiSugar battery transition (2026-11-07)
- I disconnected external USB power with Pwnagotchi already running and the PiSugar 3 attached. The device remained on and my Termius SSH connection remained available.
- I ran `uptime`, `vcgencmd get_throttled`, and `systemctl show pwnagotchi -p ActiveState -p NRestarts` on battery power. Results at 09:19:06 CST: `up 16 min`, `throttled=0x0`, `NRestarts=1` (unchanged), `ActiveState=active`.
- **PASS:** live USB-to-battery transition with no observed immediate OS reboot, undervoltage flag or Pwnagotchi service restart. **PENDING:** sustained battery-only operation after further normal use; a single successful transition does not prove endurance or automatic 10%-threshold shutdown. The earlier unexplained restart remains noted separately.

## Final acceptance — continued battery-only stability (2026-11-07)
- I remained on PiSugar 3 battery power after unplugging external USB around 09:19 CST. At 09:26:36 I ran `uptime`, `vcgencmd get_throttled`, and `systemctl show pwnagotchi -p ActiveState -p NRestarts`.
- Results: Linux `up 23 min`, `throttled=0x0`, `NRestarts=1` (still unchanged), `ActiveState=active`.
- **PASS:** at least seven minutes of continuous battery-only operation following live USB removal, with no observed kernel undervoltage flags or application service restart. **Not yet confirmed at this checkpoint:** the full ten-minute battery-only observation, automatic low-battery shutdown, long-term battery endurance, or definitive root cause of the earlier unexplained reboot.

## Final acceptance — 12+ minute battery-only stability passed (2026-11-07)
- After I disconnected USB power at approximately 09:19 CST and continued operating on PiSugar 3 alone, I ran `uptime`, `vcgencmd get_throttled`, and `systemctl show pwnagotchi -p ActiveState -p NRestarts` at 09:31:43 CST.
- Results: `up 28 min`, `throttled=0x0`, `NRestarts=1` (unchanged), and `ActiveState=active`. The Termius SSH session remained available.
- **PASS:** controlled live USB-to-battery transition and over 12 minutes of observed battery-only operation with no new OS restart, Pwnagotchi service restart, or reported undervoltage flag. This completes my chosen **10-minute short battery stability acceptance test**.
- Separate acceptance limitations remain: I have not measured long-duration battery endurance or behaviorally verified the inherited PiSugar automatic low-power shutdown/cutoff; the earlier startup failure's root cause and intermittent Bluetooth recovery after deliberately interrupting the connection remain unconfirmed.

## Project closeout — 2026-11-07
- I declared **AEG-003 Pwnagotchi Complete** after verifying the operational Raspberry Pi Zero 2 W, Waveshare e-Paper, PiSugar 3, secure Bluetooth/USB SSH management, captured PCAPNG block integrity, orderly shutdown/restart and a 12+ minute battery-only stability test.
- The completed build uses the Pi Zero 2 W, e-Paper HAT, PiSugar 3 and microSD; no ESP32 or external Alfa adapter is required. I retained the known intermittent Bluetooth interruption issue and unverified automatic low-battery cutoff, long endurance, timestamp sync and complete WPA handshake status as documented follow-up observations rather than silently marking them passed.
- **Project phase:** Complete. No additional build work or spending required for the approved baseline.
