# AEG-006 Engineering Build Journal


> **Sanitization note (2026-11-08):** Earlier documentation replaced the actual host identifier with `<TCT_HOSTNAME>` and normalized hostname-derived local application paths to the illustrative directory `~/tct-app`. Paths shown in historical examples may differ from the folder originally used on the device. For a new installation, follow the consistent paths in the [reproduction guide](../REPRODUCE.md); this edit does not claim that my original commands used the normalized folder.
This journal records the Raspberry Pi 5 / 10-inch touchscreen Tactical Control Terminal. This journal was reconstructed from verified sessions; it is not a verbatim terminal transcript. Photos mentioned below are pending upload and are not represented as committed artifacts.

## Phase 0 — Install the correct Raspberry Pi OS image (before assembly and SSH recovery)

**Required image for this specific build:** **Raspberry Pi OS (64-bit) with Desktop**, selected in **Raspberry Pi Imager** for Raspberry Pi 5. The verified installation boots a graphical desktop and reports Debian GNU/Linux 13 (Trixie). Do **not** select **Raspberry Pi OS Lite** for this walkthrough: Lite lacks the graphical desktop, Chromium and graphical session required by the documented touchscreen kiosk. A Lite-based build would need additional packages and setup not covered here. The optional image labeled *Desktop and recommended software* is not required.

**Prepare the 128 GB microSD card from a separate management computer:**
1. Install and open Raspberry Pi Imager; choose **Raspberry Pi 5** as the device.
2. Under **Operating System**, choose **Raspberry Pi OS (64-bit)** — the **desktop** image, not the Lite variant. Check the image description in Imager because menu labels can change.
3. Under **Storage**, select the intended microSD card. Writing the image **erases the selected drive**; double-check the target.
4. Before writing, use the OS customization options to set the device hostname (here `<TCT_HOSTNAME>`), create the `aegis` account with a strong password, configure Wi-Fi and its regulatory country if Wi-Fi is used, select time zone `America/Chicago`, and **enable SSH**. Select either password authentication for initial setup or provision a public SSH key already generated on the management computer.
5. Write and verify the image, safely eject the card, insert it into the Pi, attach the DSI touchscreen and cooler according to their hardware instructions, and apply the official Pi 5 power supply.
6. If the display is blank, **do not assume the OS failed to install**. Check whether the Pi joined the network and continue with the following headless SSH recovery phase.

**Why Desktop matters:** AEGIS Mesh Control is a Flask server displayed locally in Chromium fullscreen kiosk mode via the Raspberry Pi OS graphical `labwc` session. The browser, display stack and touch navigation depend on the desktop environment being installed. The Flask API itself can operate headlessly; the **documented AEG-006 operator interface** cannot.

**Verify the installed OS after SSH access is available (commands run on Pi):**
```bash
cat /etc/os-release          # Confirm Debian release (Trixie for this build)
getconf LONG_BIT             # Confirm 64-bit userspace (expected: 64)
command -v chromium          # Check browser presence (actual path may vary)
```

**Evidence and accuracy:** Debian 13 Trixie, working graphical desktop, and Chromium kiosk were verified during the build. This is a reproducible installation checklist; the exact Raspberry Pi Imager selections from the original imaging session were not fully captured.

<img width="680" height="482" alt="Pi 5 OS Selection" src="https://github.com/user-attachments/assets/47c84773-65bc-4ee4-a0aa-4dcf1d51d4b1" />


## Phase 1 — Assembly and OS
Installed Pi 5, DSI touchscreen, and Active Cooler. Initial blank screen resolved after EEPROM update and reboot. Debian 13 Trixie; touchscreen taps and swipes verified.

Commands and rationale:
```bash
cat /etc/os-release      # Identify OS
uname -a                 # Identify kernel
sudo apt full-upgrade    # Apply package upgrades
sudo rpi-eeprom-update   # Inspect bootloader
```

<img width="480" height="482" alt="Pi Touch and Pi5 Complete" src="https://github.com/user-attachments/assets/7a2639c9-21d7-410f-ae03-bc21d0f84129" />

## Phase 1A — Headless SSH recovery when the touchscreen was blank

**Problem:** Initial power-on produced a black touchscreen. Commands could not be entered using the local display, so the Raspberry Pi was administered remotely from a Kali Linux terminal over the local network. The display was not considered operational until after remote troubleshooting and the EEPROM update/reboot.

**Prerequisites:** Raspberry Pi OS must already be written to microSD with a usable login, networking, and SSH enabled. For a new build, configure the hostname, account/password or authorized SSH public key, Wi-Fi (if used), and **Enable SSH** in Raspberry Pi Imager's OS customization before first boot. This is a reproducibility instruction, not proof that each Imager setting was used during the original build.

**Important distinction:** SSH to the Pi and SSH authentication to GitHub are two different connections. A GitHub-specific `id_ed25519_github` key was configured later for repository pushes; that key is not required to diagnose the blank display. Access to the Pi can initially use password authentication if SSH is enabled, or an authorized public key provisioned before boot.

### Step A — Locate the Pi from the management computer

The hostname was `<TCT_HOSTNAME>`. Name resolution using `<TCT_HOSTNAME>.local` was attempted but did not reliably resolve, so the Pi's LAN-assigned IP address was found through the router's connected-device list.

Example commands on the **Kali management machine**, not on the Pi touchscreen:

```bash
ping -c 2 "<TCT_HOSTNAME>.local"        # Optional discovery check; mDNS may fail
ssh aegis@<PI_LAN_IP>           # Connect using the IP discovered from router
```

Replace `<PI_LAN_IP>` with the actual private LAN address; do not publish real network identifiers. The SSH login was eventually successful using the address found in the router.

### Step B — SSH key authentication (optional hardening / fresh installation)

If choosing SSH keys, create the key on the **Kali management machine** and provision its public half on the Pi via Raspberry Pi Imager before boot, or after an initial password-authenticated login:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_aegis -C "TCT-SSH-KEY"
# If password authentication already works and the Pi allows it:
ssh-copy-id -i ~/.ssh/id_ed25519_aegis.pub aegis@<PI_LAN_IP>
ssh -i ~/.ssh/id_ed25519_aegis aegis@<PI_LAN_IP>
```

`ssh-keygen` generates a keypair; `ssh-copy-id` installs **only the public key** for the target account; `ssh -i` selects the matching private key locally. Never copy the private key to the Pi or commit either private key or secret values to GitHub. A fresh installation does **not** require generating a key if password SSH is already configured and acceptable for initial recovery. The original session records do not establish that this exact key-generation sequence was executed for Pi login.

### Step C — Diagnose and recover the display remotely

After connecting through SSH, commands are run on the **Pi shell**:

```bash
cat /etc/os-release          # Verify OS version
uname -a                     # Verify running kernel
sudo apt update              # Refresh package metadata
sudo apt full-upgrade        # Apply system packages and Pi-related updates
sudo rpi-eeprom-update       # Inspect bootloader/EEPROM status
sudo reboot                 # Reboot after applying updates when appropriate
```

**Observed in this build:** Raspberry Pi OS Debian 13 Trixie; initial blank screen resolved after EEPROM maintenance and reboot; later bootloader status reported up to date. Physical touch input was subsequently verified. Distinguish the demonstrated outcome from the general SSH provisioning procedure above.

**Troubleshooting / safeguards:** If SSH is refused, check that the Pi booted, networking works, and SSH was enabled in Imager; if authentication fails, confirm the configured username and matching password/public key. The device must be on a reachable authorized LAN. Do not disable password authentication until key-based login has been tested successfully. For a power-only screen, check DSI ribbon orientation, GPIO power wiring and supported display configuration before assuming software is the only problem.


## Phase 1B — Mobile SSH administration with Termius (2026-11-07)

**Objective:** Establish a second, independent SSH management path from the Termius mobile client to the Raspberry Pi 5 Tactical Control Terminal, while preserving the working Kali SSH session and the existing key-based-only SSH policy.

**Starting condition:** Kali could connect over SSH using an authorized key. Password-based login from Termius failed. Connection-specific OpenSSH configuration was checked on the Pi:

```bash
sudo sshd -T -C 'user=aegis,host=<TCT_HOSTNAME>,addr=127.0.0.1' \
  | grep -E '^(passwordauthentication|pubkeyauthentication|kbdinteractiveauthentication) '
```

**Observed effective SSH settings:**
```text
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
```

**Interpretation:** Key-based access was allowed; password and keyboard-interactive authentication were disabled. Password failure in Termius was therefore expected. A separate ED25519 keypair was generated inside Termius for the mobile device. The public key was authorized on the Pi; the private key was kept in the mobile SSH client. A passphrase is recommended for the mobile private key, with its storage cipher left at the app's secure default.

### Procedure — add the mobile public key safely

1. With the original Kali SSH session **still open**, generate an ED25519 key in Termius; assign the local key a descriptive label such as `AEGIS-TCT-iPhone`.
2. Copy **the exact public key** using Termius's *Copy Public Key* action. The label/comment at the end of an OpenSSH public-key line is optional. Do not manually retype ambiguous Base64 characters such as `I`, `l` and `1`.
3. On the **Pi via Kali SSH**, preserve the working authorized-key file and append the new public key as a separate line:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys.bak
nano ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

4. Verify each key independently to identify malformed lines without disclosing key material:

```bash
while IFS= read -r key; do
    if [[ "$key" == ssh-* || "$key" == ecdsa-* ]]; then
        printf '%s\n' "$key" | ssh-keygen -lf -
    fi
done < ~/.ssh/authorized_keys
```

**Observed troubleshooting:** Only the existing Kali key initially produced a valid fingerprint. The newly pasted Termius line caused `(stdin) is not a public key file.` This indicated an invalid/malformed public-key entry, consistent with a transcription or clipboard-formatting issue. The invalid mobile key line was replaced with an exact copy from Termius without altering the Kali key. The subsequent mobile SSH connection succeeded.

**Mobile client configuration:** Host address set to the Pi's LAN IP, TCP port `22`, username `aegis`, authentication set to the newly generated Termius SSH key rather than password. Actual addresses, fingerprints, passwords and private keys are deliberately omitted from this public journal.

**Acceptance result:** **PASS** — Termius authenticated successfully to AEG-006 from the mobile device; the pre-existing Kali key access was preserved. No change to the effective SSH password-authentication policy was necessary. The dashboard application itself remained unchanged.

**Recommended repeatable confirmation (not claimed as recorded terminal output):**
```bash
whoami
hostname
systemctl is-active aegis-mesh.service
```

Expected: `aegis`, `<TCT_HOSTNAME>`, and `active` if the dashboard service is running.

**Security note:** Do not add private-key files, real `authorized_keys` contents, account passwords, host fingerprints tied to private infrastructure, or LAN addresses to the public repository. Store recovery copies securely outside the Git repository. Keep a known-working SSH session open until each new authentication method has been tested.

## Phase 2 — Cooling and system baseline
Measured approximately 45 C CPU temperature; manual fan speed measurements approximately 7566 RPM at PWM 255 and 5099 RPM at PWM 125.
```bash
cat /sys/class/thermal/thermal_zone0/temp
ls /sys/class/hwmon/
```

## Phase 3 — Python/Flask and kiosk
Python 3.13.5, Meshtastic Python client 2.7.11, Flask 3.1.3. **Actual tested runtime virtual environment:** `/home/aegis/aegis-tct/.venv` (earlier sanitized instructions used illustrative `~/tct-app/.venv`). Flask binds 127.0.0.1:5000. systemd unit aegis-mesh.service enabled. Chromium kiosk starts via labwc autostart.
```bash
systemctl is-enabled aegis-mesh.service
systemctl is-active aegis-mesh.service
systemctl status aegis-mesh.service --no-pager
curl -sS http://127.0.0.1:5000/api/status
```
Why: validate service, boot integration, and telemetry before adding radio features.

<img width="480" height="482" alt="App Works" src="https://github.com/user-attachments/assets/d8b1ad63-465d-40c2-969d-36bed4c48340" />

## Phase 4 — v0.2 system monitoring
Implemented CPU temperature, memory, storage, uptime, and fan RPM. Fixed uptime parsing and hwmon pwmfan detection. Verified cards on touchscreen. Source milestone: 776c9db.

## Phase 5 — v0.3 RF monitor
```bash
curl -sS http://127.0.0.1:5000/api/rf
```
Verified radio_connected false, packets_received zero, spectrum_available false. No radio or SDR attached. Source milestone: 307f2f8.

## Phase 6 — v0.4 synthetic packets
In-memory packet store bounded at 200 events. Three explicitly synthetic samples: TEXT from TEST-NODE-A (-82 dBm, 7.5 dB), POSITION from TEST-NODE-B (-94 dBm, 2.1 dB), TELEMETRY from TEST-NODE-C (-88 dBm, 5.3 dB).
```bash
curl -i --max-time 5 http://127.0.0.1:5000/api/packets
sudo journalctl -u aegis-mesh.service -n 30 --no-pager
grep -n 'def packet_events' ~/tct-app/src/app.py
grep -n 'def packet_events' ~/aegis-portfolio/projects/tactical-control-terminal/src/app.py
```
Why: investigate HTTP 404. Root cause: live backend lacked the endpoint even though GitHub copy contained it. Corrected file synchronized, compiled, restarted, and three synthetic records verified.
Source milestones: 0fc2625, eab09bf.

## Phase 7 — v0.5 packet statistics
Confirmed TEXT filter shows one event, one source, -82.0 dBm RSSI and 7.5 dB SNR. Three-record averages -88.0 dBm RSSI and 5.0 dB SNR. RSSI bars are illustrative, not spectrum data. Touchscreen tested.

## Phase 8 — v0.6 history controls
Verified source filter, type filter, Pause/Resume, Clear/Restore View, RSSI bars, and statistics on touchscreen. Backend retained separately; clearing view does not delete server packet history. Version 0.6 published. History 10/50/200 selectors still need validation with more than 10 records.
Evidence: original v0.6 touchscreen photograph captured during acceptance testing; not yet uploaded to GitHub.

## Phase 9 — RAK4631 arrival, bench assembly and live USB communication (November 10–11, 2026)

**Status: PASSED for initial USB serial integration.** This phase supersedes the previous delivery-pending checkpoint. AEG-002 arrived November 10, with the RAK19007 base, RAK4631 core (RAK4630 module marking), GNSS board, separate OLED, BLE, 902–928 MHz LoRa antenna, ceramic GNSS antenna, rubber LoRa antenna, SMA pigtail and mounting accessories. Initial inventory came from unpacking photographs; individual component SKU markings and the optional accelerometer should be verified again during detailed assembly. The OLED remained **uninstalled and untested**.

### Antenna assembly and precautions

With USB/battery disconnected, the LoRa antenna was attached to the connector labeled `LoRa`, the BLE antenna to `BLE`, and the square ceramic GNSS antenna to the GNSS module. Photographs show all three leads attached, although seating cannot be proven conclusively from photographs alone. Do not power/transmit with the LoRa antenna disconnected. Use just one LoRa antenna; the rubber/SMA assembly was not needed for this bench test. No soldering or external battery was used.

### Wi-Fi network change and kiosk recovery

The Raspberry Pi 5 was moved to a new home Wi-Fi network. Chromium was running in kiosk mode, so **F11 did not exit fullscreen**. `Alt+F4` closed the kiosk browser, returning to the Raspberry Pi OS desktop; the new Wi-Fi was selected via the desktop network menu. The local Flask service was not reinstalled. The Pi's LAN address may have changed; remote SSH clients must use the current address.

Reproducible verification commands (not all exact outputs preserved):

```bash
hostname -I
systemctl is-active aegis-mesh.service
chromium --kiosk http://127.0.0.1:5000
```

### USB serial detection and Meshtastic firmware

The assembled radio was attached by USB-A-to-USB-C data cable to the Pi. The serial device appeared at `/dev/ttyACM0`. `lsusb` and serial-path discovery were used; the exact `lsusb` line is not preserved.

```bash
lsusb
ls -l /dev/ttyACM* /dev/ttyUSB* 2>/dev/null
cd ~/aegis-tct
source .venv/bin/activate
meshtastic --version
meshtastic --port /dev/ttyACM0 --info
```

**Observed:** Python Meshtastic CLI **2.7.11** connected and returned `Connected to radio`; installed RAK4631 firmware was **2.7.15.567b8ea**, device role `CLIENT`, and the node database initially contained just **one node (self)**. No over-the-air peer-to-peer exchange was demonstrated.

### Regulatory region and modem verification

```bash
meshtastic --port /dev/ttyACM0 --get lora.region
# Observed initially: lora.region: 0 (UNSET)

meshtastic --port /dev/ttyACM0 --set lora.region US
# Observed: Set lora.region to US
# Observed: Writing modified preferences to device
# Observed: Writing lora configuration to device

meshtastic --port /dev/ttyACM0 --get lora.region
# Observed: lora.region: 1 (US)

meshtastic --port /dev/ttyACM0 --get lora.modem_preset
# Observed: lora.modem_preset: 0 (LONG_FAST)
```

**Why:** An unset regional configuration must be corrected for lawful local operation; a readback verifies persistence. The LONG_FAST preset required no alteration. A `termios.error: (5, 'Input/output error')` appeared after one region readback during serial cleanup. Following a brief pause, `/dev/ttyACM0` was present and the CLI connected successfully without the same error. The suspected USB reset/re-enumeration was **not proven by kernel logs**.

Node ownership was configured and read back:

```bash
meshtastic --port /dev/ttyACM0 --set-owner "AEGIS-MESH-01"
meshtastic --port /dev/ttyACM0 --set-owner-short "AE01"
meshtastic --port /dev/ttyACM0 --info
```

**Verified identity:** long name `AEGIS-MESH-01`, short name `AE01`. Avoid publishing actual node IDs, private channel keys or precise GNSS coordinates.

### Live CLI receive and first telemetry

```bash
meshtastic --port /dev/ttyACM0 --listen
# Exit using Ctrl+C, releasing the serial port before another client connects.
```

Live decoded `TELEMETRY_APP` events and a `POSITION_APP` event were observed. Representative recorded values from `--info`: battery level `101` (external power sentinel), voltage `4.243 V`, uptime `209 s`, channel utilization `0.0`, `airUtilTx` `0.046944443`. The presence of a position event does **not** prove a fresh, accurate GNSS fix. The one-node dataset does **not** prove peer RF reception.

The kiosk still reported `Meshtastic Radio: Not Connected`. An explicit API check showed the expected **v0.6 hardcoded state** although a serial device existed:

```bash
systemctl is-active aegis-mesh.service
# Observed: active
curl -s http://127.0.0.1:5000/api/status | python3 -m json.tool
# Observed fields:
# app_status: online
# radio_status: not_connected
# node_data_status: awaiting_radio
# serial_candidates: ["/dev/ttyACM0"]
# nodes: []
```

**Root cause:** The published v0.6 Flask backend detects serial candidates but does **not** open a Meshtastic serial session. Offline radio status is therefore a software integration limitation, not evidence of failed hardware. `/api/packets` continues to contain three explicitly synthetic test events, not actual RF packets.

## Phase 10 — v0.7 standalone live-radio manager (November 11, 2026)

**Status: standalone prototype passed; Flask integration not yet applied or tested.**

### Preserve v0.6 and inspect existing source

```bash
cd ~/aegis-tct
cp src/app.py src/app.py.v0.6.backup
ls -lh src/app.py*
grep -nE 'radio_status|node_data_status|serial_candidates|api/status|api/packets|meshtastic|Flask' src/app.py
wc -l src/app.py
sed -n '1,140p' src/app.py
systemctl cat aegis-mesh.service
sed -n '1,200p' src/packet_store.py
```

**Observed:** `app.py` was **140 lines**; the radio status and node data status were fixed to `not_connected` and `awaiting_radio`. `packet_store.py` uses a lock-protected `deque(maxlen=200)`, loaded with three labeled synthetic records. The live service runs as `aegis` from `/home/aegis/aegis-tct`, uses its `.venv` Python executable, sets `PYTHONUNBUFFERED=1`, `Restart=on-failure`, `RestartSec=5`, and `NoNewPrivileges=true`. The copied `systemctl cat` screenshot truncated part of `ExecStart`, so don't treat the truncated text as the full service command.

### Direct Python event-subscription smoke test

A standalone 30-second test subscribed to `meshtastic.receive`, opened `SerialInterface(devPath="/dev/ttyACM0")` and counted `len(interface.nodes)`:

```text
Connecting to radio at /dev/ttyACM0...
[CONNECTED] Meshtastic radio
Known nodes: 1
Listening for 30 seconds...
[LIVE] Packet type: TELEMETRY_APP
  batteryLevel: 101
  voltage: 4.253
  uptimeSeconds: 365
  channelUtilization: 0.0
  airUtilTx: 0.046944443
[LIVE] Packet type: POSITION_APP
Test finished.
```

This verified **Python-level callbacks for live device events**, but did not establish receipt from another radio. The receiving program deliberately omitted position coordinates, message payloads and keys.

### New local `src/radio_manager.py`

A standalone module, **not yet committed as a repository source file and not yet imported by Flask**, was created using `cat > ~/aegis-tct/src/radio_manager.py <<'PY'`. Its design:

- Background daemon thread supervising `SerialInterface` on `/dev/ttyACM0`.
- One serial owner; PubSub callbacks for `meshtastic.receive` and `meshtastic.connection.lost`.
- Lock-protected status snapshot: `connected`, port, one-node count, event count, last event type/time, selected device metrics and error state.
- `deviceMetrics` extraction limited to battery, voltage, uptime, channel utilization and TX airtime utilization.
- USB absence and connection exceptions trigger a retry loop; **unplug/replug auto-recovery is not yet validated**.
- Standalone 30-second JSON status output every five seconds.
- No persistence, no actual Flask integration, no production packet-history ingestion, and no storage of location coordinates or text.

Commands:

```bash
cd ~/aegis-tct
source .venv/bin/activate
python -m py_compile src/radio_manager.py
python -u src/radio_manager.py
```

**Initial prototype result:** `INFO: Meshtastic connection established`; `connected: true`, `node_count: 1`, `packets_observed: 2`, last event `TELEMETRY_APP`, no reported errors; `device_metrics: {}` in all six snapshots of the first 30-second run. This was not evidence of parser failure: device metrics were subsequently received during a longer inspection.

### Telemetry field-shape inspection (60 seconds)

A second standalone subscription printed only decoded field names and allowed metrics:

```text
Connected. Inspecting telemetry for 60 seconds...
[TELEMETRY EVENT]
Decoded fields: ['portnum', 'payload', 'telemetry']
Telemetry fields: ['time', 'deviceMetrics', 'raw']
Device metrics: {'batteryLevel': 101, 'voltage': 4.241, 'uptimeSeconds': 1627, 'channelUtilization': 0.0, 'airUtilTx': 0.06586111}
[TELEMETRY EVENT]
Decoded fields: ['portnum', 'payload', 'telemetry']
Telemetry fields: ['time', 'deviceMetrics', 'raw']
Device metrics: {'batteryLevel': 101, 'voltage': 4.229, 'uptimeSeconds': 1812, 'channelUtilization': 0.0, 'airUtilTx': 0.08477777}
Inspection complete.
```

**Conclusion:** The parsed `decoded.telemetry.deviceMetrics` field names are correct. Device metrics arrive on their own cadence and may not appear during a 30-second sampling window. A defensive edit was nevertheless made so telemetry events lacking `deviceMetrics` cannot overwrite the last valid metric snapshot with an empty dictionary.

### Editing incident and recovery

During editing in `nano`, lines 71–78 of the new module lost proper indentation. The following were observed:

```text
TabError: inconsistent use of tabs and spaces in indentation (radio_manager.py, line 77)
IndentationError: expected an indented block after 'if' statement on line 77 (radio_manager.py, line 78)
```

`expandtabs(4)` removed tab characters but did not correct the missing indentation depth. `nl -ba src/radio_manager.py | sed -n '55,95p'` identified the malformed comprehension and `if new_metrics` body. A targeted Python text replacement restored the following block:

```python
            new_metrics = {
                key: metrics[key]
                for key in allowed
                if key in metrics
            }

            if new_metrics:
                changes["device_metrics"] = new_metrics
```

A new `py_compile` check then passed, and a second standalone radio-manager test succeeded.

### Final observed standalone acceptance

```text
INFO: Connecting to /dev/ttyACM0
INFO: Meshtastic connection established
{
  "connected": true,
  "connection_type": "usb_serial",
  "port": "/dev/ttyACM0",
  "node_count": 1,
  "packets_observed": 2,
  "last_event": {
    "type": "POSITION_APP",
    "timestamp": "2026-11-11T07:10:35+00:00"
  },
  "device_metrics": {
    "batteryLevel": 101,
    "voltage": 4.25,
    "uptimeSeconds": 1872,
    "channelUtilization": 0.0,
    "airUtilTx": 0.08477777
  },
  "error": null
}
Radio test finished.
```

The status was repeated every five seconds throughout the 30-second run without a reported exception. The standalone program shut down cleanly and released the serial port. This demonstrates **live node telemetry processing**, not a completed v0.7 deployment.

**Outstanding integration work:** (1) retrieve the exact `app.py` route definitions and code near lines 45–115; (2) connect the single persistent manager to Flask lifecycle and `/api/status`/`/api/rf`; (3) separate live packet history from synthetic demo records; (4) update/test kiosk UI and verify no serial contention; (5) validate unplug/replug, reboot, GNSS fix, display/OLED, BLE pairing and two-node messaging when a second authorized peer is available. The untested 10/50/200-history selectors and enclosure/battery endurance remain open.

**Source-control hold point:** `radio_manager.py` currently exists on the Pi only. It must be copied verbatim from the tested live file into `projects/tactical-control-terminal/src/radio_manager.py`, reviewed and committed before claiming reproducible v0.7 source. Do not substitute this narrative for the actual Python source.

## Photo register (additional original image upload pending)
- photos/01-assembly.jpg — Pi and display assembly
- photos/02-kiosk.jpg — running touchscreen dashboard
- photos/03-monitoring.jpg — system telemetry
- photos/04-v06.jpg — packet history controls
- photos/05-rak4631-unboxing.jpg — AEG-002 starter kit inventory
- photos/06-rak4631-front-back.jpg — baseboard and module connectors
- photos/07-rak4631-antennas.jpg — LoRa/BLE/GNSS antenna arrangement
- photos/08-meshtastic-cli.jpg — firmware, region and CLI connection
- photos/09-live-telemetry.jpg — anonymized serial/event output

## Future session format
Record goal, actual commands, reason for each command, full redacted output, what the output means, error and resolution, test pass/fail, source commit and embedded original photo. Never fabricate output or imply photos are present before they are committed.

Tracking: https://github.com/k41ju0x/Project-AEGIS/issues/6

## Reproduction status and source cross-reference (2026-11-08)

I audited the original v0.6 project source and identified that the initial journal did not preserve every shell command used to configure its virtual environment, systemd unit, and Chromium kiosk. Rather than presenting guessed commands as my actual past terminal history, I wrote a separate [source-grounded reproduction guide](../REPRODUCE.md) with setup, `pip` dependency installation, local API checks, an **example** systemd unit, an **example** labwc kiosk autostart, expected outputs and explicit gaps requiring fresh-install validation.

The original build results above remain the historical record; the separate guide is a **procedure to repeat**, not a declaration that its reconstructed lines were executed verbatim during the original build. Its accuracy should be confirmed on a clean microSD/second Pi before describing it as end-to-end reproducible.


## November 11, 2026 — Cross-project repository/source audit and resume checkpoint

This checkpoint reconciles **AEG-002** and **AEG-006** against photographed hardware, command outputs and actual GitHub source. It does not imply that the live Pi filesystem or deployed Flask service was remotely modified during the documentation audit.

| Area | Verified at checkpoint | Remaining gap |
|---|---|---|
| AEG-002 physical inventory | Kit received, base/core/GNSS visually inventoried, antenna leads attached | Exact OLED/optional sensor SKU and connector seating verification; OLED still uninstalled |
| Firmware and LoRa | RAK4631 firmware 2.7.15.567b8ea, US region, LONG_FAST and node names read back | Firmware recovery/flash and cold-boot tests |
| CLI | Meshtastic 2.7.11 connects over /dev/ttyACM0 | Concurrency policy once live Flask manager is enabled |
| Telemetry | Actual TELEMETRY_APP/POSITION_APP events, parsed device metrics | Fresh GNSS fix, remote RF peer, sustained reception |
| Python manager | Locally tested radio_manager.py passes compilation and 30-sec session; debug incident resolved | Exact source file must be copied from Pi, reviewed and committed; unplug/replug testing |
| v0.6 Flask backend | GitHub src/app.py inspected; /api/status and /api/rf have hardcoded offline status; /api/packets is synthetic | Implement and acceptance-test v0.7 integration |
| Packet store | GitHub src/packet_store.py inspected; 200-event bounded deque, 3 demo records | Separate real and synthetic queues, annotate local-vs-over-air events |
| systemd | Service active; user aegis and venv running; restart on failure | Verify full ExecStart and production behavior with live serial owner |
| Physical evidence | Older journal contains original uploaded photos; new kit and terminal screenshots seen during testing | Add and embed original RAK4631 photos, with privacy/location metadata stripped |
| Security | No private keys, channel credentials, exact GPS coordinates or private LAN IPs copied into journal | Review any subsequently committed logs/screenshot EXIF |

### Exact code provenance / known gap

The tested `/home/aegis/aegis-tct/src/radio_manager.py` was created and repaired **on the Raspberry Pi**, not through the GitHub connector. GitHub currently retains the verified v0.6 `src/app.py` and `src/packet_store.py`. The functional manager source has **not** been independently fetched from the device, so do not call any reconstructed version of it the exact tested file.

The complete **original proposed manager creation command** was supplied in the engineering session. The applied correction replaced the initial unconditional assignment of an empty metric dict with:

```python
            new_metrics = {
                key: metrics[key]
                for key in allowed
                if key in metrics
            }

            if new_metrics:
                changes["device_metrics"] = new_metrics
```

To publish the **actual** tested file, use this sequence on the Pi when resuming:

```bash
cd ~/aegis-tct
source .venv/bin/activate
python -m py_compile src/radio_manager.py
sha256sum src/radio_manager.py
cd ~/aegis-portfolio
git pull --ff-only origin main
cp ~/aegis-tct/src/radio_manager.py projects/tactical-control-terminal/src/radio_manager.py
git diff -- projects/tactical-control-terminal/src/radio_manager.py
git add projects/tactical-control-terminal/src/radio_manager.py
git commit -m "feat(AEG-006): add verified standalone Meshtastic radio manager"
git push origin main
```

**Why:** `git pull --ff-only` syncs the new GitHub documentation before local commit; `cp` preserves the actual successfully tested Python file; review/commit/push gives traceable source provenance. These are **next-session instructions, not commands claimed executed**. Inspect the file for secrets and environment paths before staging. Avoid committing `.venv`, backups, logs or credentials.

### Immediate next development step

The last completed development operation was the 30-second `radio_manager.py` test concluding with `Radio test finished.` The running kiosk is still v0.6. Resume by inspecting exact endpoint definitions and implementation context **without editing anything**:

```bash
cd ~/aegis-tct
grep -nE '^(@app.route|@app.get|def |if __name__)' src/app.py
sed -n '45,115p' src/app.py
```

Follow with a backup, syntax validation, controlled manual API test and rollback plan before restarting the systemd service. Implement one persistent serial owner, distinguish local node callbacks from actual external mesh reception, and retain demonstration events in a separate clearly labeled store. Keep the server loopback-bound until remote access is separately designed.


## 2026-11-11 — v0.7 live Flask backend promoted to systemd (verified)

**Purpose:** Replace the v0.6 hardcoded offline status with data from the already-tested local `src/radio_manager.py`, while preserving the existing synthetic packet demo. This was an incremental backend integration, **not** a complete v0.7 UI/packet-history release.

**Troubleshooting:** An initial automated Flask patch never applied: a guard expected exactly one `"radio_connected": False` occurrence, but it existed in both the RF and synthetic packet endpoints. Checks of both source (`grep`) and the port-5000 API confirmed no `radio_manager` import and still-hardcoded `radio_status: not_connected`. A corrected route-specific patch was then applied and compiled. The working v0.6 application was backed up locally as `src/app.py.v0.6.safe` (backups not committed).

**Implementation observed through API:** Flask now imports/starts the background radio manager, reads `snapshot()` in `/api/status` and `/api/rf`, and supports an optional `AEGIS_HTTP_PORT` override for independent loopback testing. The UI and synthetic packet store were not edited. The exact modified `app.py` and locally tested `radio_manager.py` have **not yet been published** to GitHub as source files; the GitHub `src/app.py` is still v0.6.

### Isolated Flask acceptance on localhost port 5001

```bash
cd ~/aegis-tct
source .venv/bin/activate
AEGIS_HTTP_PORT=5001 python -u src/app.py
# Separate terminal:
curl -sS http://127.0.0.1:5001/api/status | python3 -m json.tool
curl -sS http://127.0.0.1:5001/api/rf | python3 -m json.tool
curl -sS http://127.0.0.1:5001/api/packets | python3 -m json.tool
```

**Observed:** `/api/status` returned `radio_status: connected`, `node_data_status: radio_connected`, `radio.connected: true`, `node_count: 1`, `packets_observed: 5`, device voltage 4.254 V, uptime 4363 s, and error null. `/api/rf` later returned `radio_connected: true`, `events_observed: 6`, last `TELEMETRY_APP` event, and 4.24 V. The `packets_received: 0`, empty packets array, `capture_active: false`, null RF region/preset and `spectrum_available: false` fields remained unchanged because no external-packet collector or SDR exists. `/api/packets` returned **three** explicitly labeled synthetic records (`mode: synthetic_test`, `synthetic: true`, `count: 3`), still with legacy hardcoded `radio_connected: false` on that demo endpoint. No mixing of synthetic and observed events.

After stopping the port-5001 process, `ss -ltnp | grep ':5001 '` found no listener.

### Systemd production promotion and verification

```bash
cd ~/aegis-tct
sudo systemctl restart aegis-mesh.service
systemctl is-active aegis-mesh.service
# Observed: active
curl -sS http://127.0.0.1:5000/api/status | python3 -m json.tool
```

**Observed production API response at 2026-11-11T01:41:38-06:00:** `app_status: online`, `radio_status: connected`, `node_data_status: radio_connected`, `radio.connected: true`, `connection_type: usb_serial`, port `/dev/ttyACM0`, one known node, one event since restart (`TELEMETRY_APP`), and `error: null`. Device metrics: `batteryLevel: 101` (USB/external power sentinel), voltage **4.237 V**, radio uptime **4623 seconds**, channel utilization **0.0**, TX airtime utilization **0.122611105**. Host CPU temperature 46.3 C, 943/8062 MB used, Active Cooler 0 RPM, and service `active`. The production Flask connection and API validation **PASSED**.

**Not yet verified:** whether the existing 10-inch kiosk frontend visually changes to *Connected*, reconnect behavior across USB removal/restart, live node enumeration (`nodes` is still an empty array), and real packet history. The event counter includes local device events; do not equate it with peer-to-peer RF reception. Do not describe v0.7 as a complete finished release.

**Next actions:** (1) visually inspect Overview tab on the touchscreen; (2) publish the *exact tested local* `src/app.py` and `src/radio_manager.py` after synchronizing the checkout and reviewing secrets; (3) keep synthetic and live packet histories separate, implement node listing and validate frontend; (4) test reconnect and reboot. Do not start a second Meshtastic serial process while the systemd service owns `/dev/ttyACM0`.

## November 11, 2026 — Touchscreen live-radio UI and packet-history acceptance

The previously deployed Flask backend exposed live connection status, but the v0.6 Overview JavaScript still set `#radio` to `NOT CONNECTED` unconditionally. A focused local template edit made Overview read `/api/status.radio_status` and display **CONNECTED**, which was visibly verified on the physical Raspberry Pi Touch Display 2.

The RF Monitor continued to show the three demonstration sources TEST-NODE-A/B/C because its packet-history fetch targeted the synthetic `/api/packets` endpoint. The locally developed `live_packet_store.py` added a separate 200-event, process-memory buffer subscribed to `meshtastic.receive`. Initially, `/api/packets/live` returned HTTP **404**: inspection of `src/app.py` showed only `radio_manager.start()`, proving that the endpoint patch had not been applied. The missing Flask route, import and subscription were subsequently added and the service restarted.

**Recorded production endpoint acceptance:**

```bash
curl -i --max-time 5 http://127.0.0.1:5000/api/packets/live
# HTTP/1.1 200 OK
```

The API returned a real **local** event: `mode=live_local_events`, `synthetic=false`, `radio_connected=true`, `count=1`, `source=AEGIS-MESH-01`, `origin=local_node`, `packet_type=TELEMETRY`, `id=LIVE-00000001`, timestamp `2026-11-11T07:57:14+00:00`, with `rssi_dbm=null` and `snr_db=null`. This is serial-visible local-node telemetry, **not proof of peer-to-peer LoRa reception**.

The HTML/JavaScript was patched locally to provide **Live Radio** and **Simulation** selectors, routing to `/api/packets/live` and `/api/packets` respectively and showing unavailable signal values as N/A. The physical touchscreen was subsequently confirmed to show **Live Radio** and **AEGIS-MESH-01** in its live source list. The synthetic A/B/C sample records remain a distinct simulation path.

**Version/state precision:** The working device now contains the live v0.7 backend **and** live-history UI, verified for local events only. The exact tested Pi files `src/app.py`, `src/radio_manager.py`, `src/live_packet_store.py`, and `src/templates/index.html` have **not yet been committed** into the GitHub project source as of this checkpoint. The published repository source still reflects v0.6. Source capture is the immediate hold point before v0.8 development.

**Known limitations:** One owned node only; external received LoRa packets and true peer RSSI/SNR not yet tested. Node listing `nodes=[]` and full device intelligence are incomplete; reconnection under unplug/replug and system reboot untested. No need to purchase a second radio to continue single-node monitoring. Keep channel keys, messages and precise coordinates out of public logs and commits.

### Next actions — source publication followed by v0.8

1. In the existing Pi repo checkout, pull current GitHub documentation, copy the four **actual working** local source files, review staged diff for privacy and unrelated changes, compile, then commit and push the precise v0.7 snapshot.
2. Confirm the GitHub source matches the tested Pi files; do **not** overwrite the live installation from the older repository copy.
3. Build v0.8 single-node intelligence (identity/health, firmware when available, local vs remote event counters, USB fault state), maintaining separate demo/live histories.
4. Validate power-cycle, unplug/replug and delayed reconnect behavior with safe antenna attachment; postpone two-node RF messaging until a compatible peer is available.

## November 11, 2026 — v0.8 single-node health cards: visual acceptance

After the verified v0.7 source snapshot was published, the Raspberry Pi's **local** `src/templates/index.html` was updated with the initial v0.8 Mesh Nodes health view. Its fields read the existing `/api/status.radio` snapshot: connection state, USB serial port, known node count, voltage, last reported device uptime, channel utilization, TX airtime utilization, event counter, most recent event type and reported connection error. A backup of the v0.7 template was preserved locally as `src/templates/index.html.v0.7.backup`.

**Observed:** The physical Touch Display 2 **shows the new Mesh Nodes cards**. The user verified the visual rendering. The individual metric values, dynamic node identity, connection-loss behavior and firmware extraction have **not** yet been independently validated. The v0.8 HTML modifications are **local Pi working changes**, not yet claimed as a published tested source commit.

**Next:** Retrieve identity from the radio's existing serial connection with safe fallback for unavailable fields; validate API/UI results and capture exact tested source. Do not open a competing Meshtastic CLI session while systemd owns the port. After that, test safe USB unplug/replug and recovery.

## November 11, 2026 — v0.8 dynamic local identity accepted

A guarded local source patch extended `radio_manager.py` to expose a privacy-reduced `local_node` object from the existing `SerialInterface` node database (display long name, short name and hardware label). The Mesh Nodes HTML now uses that object for its heading instead of a hardcoded node name. The user confirmed **the dynamic identity worked** on the physical dashboard; exact output values were not pasted. Both manager and template were backed up before the change. No second serial session was opened.

**Next checkpoint:** use the interface's read-only `metadata.firmware_version` field (when populated) for firmware UI; validate live value and fallback. Subsequent recovery testing should not assume that USB re-enumeration always retains the same `/dev/ttyACM0` path. Local dynamic-identity changes are not yet claimed to be published to GitHub.

## November 11, 2026 — v0.8 local node firmware + identity API verified

The user ran a production `/api/status` query against the active systemd Flask service on the Raspberry Pi. Actual observed radio snapshot:

```text
Connected: True
Firmware: 2.7.15.567b8ea
Local node: {'hardware': 'RAK4631', 'long_name': 'AEGIS-MESH-01', 'short_name': 'AE01'}
```

Firmware is obtained from the existing Meshtastic `SerialInterface.metadata.firmware_version` and node display information from the local node table; no second serial interface was opened. The v0.8 frontend now has a firmware field in the Mesh Nodes diagnostics pane, though its visual update has not been independently reported in this turn. This verifies the **backend values** and connected state, not yet USB failure/recovery behavior.

**State distinction:** The current v0.8 radio-manager and HTML changes have been applied on the Pi. They still need to be copied, reviewed and published as a verified v0.8 checkpoint; do not claim GitHub source contains these changes until verified. Preserve the working radio's attached LoRa antenna during USB replug tests; do not flash firmware or alter radio settings. The current manager watches `/dev/ttyACM0`; renumbering on reconnection is a known limitation to test. Do not open an independent Meshtastic CLI session during this test.

**Next:** create the local source checkpoint and sync GitHub, then test USB unplug/replug while monitoring the Flask radio state and systemd journal, checking any error state and automatically recovered connection.

## November 11, 2026 — v0.8 USB cable disconnect/reconnect test PASSED

**Test setup:** The RAK4631 was attached to the Raspberry Pi 5 over USB serial at `/dev/ttyACM0`, with the `aegis-mesh.service` Flask process polling its own persistent `radio_manager.snapshot()` through `/api/status`. The user unplugged the radio USB cable and subsequently replugged it; terminal poll interval was approximately three seconds.

**Observed terminal transitions (local clock):**

- `02:49:31` through `02:49:49`: `Connected: True | Port: /dev/ttyACM0 | Error: None`.
- `02:49:52`: `Connected: False | Port: /dev/ttyACM0 | Error: ConnectionError`.
- `02:49:58`: `Connected: False | Port: /dev/ttyACM0 | Error: Serial device unavailable` (same error persisted through `02:50:25`).
- `02:50:28`: `Connected: True | Port: /dev/ttyACM0 | Error: None`; remained connected through the final observed sample `02:50:44`.

The disconnected window observed in the polled samples was **36 seconds** (first observed offline at 02:49:52 to first observed restored at 02:50:28); exact cable reconnect time and recovery latency were not directly measured. Crucially, the radio manager recovered automatically without a manual application/service restart, and the serial path remained `/dev/ttyACM0`.

**Acceptance:** USB disconnect detection **PASS**; unavailable-device error reporting **PASS**; automatic reconnect on the same serial path **PASS**; cleared error state after reconnect **PASS**. Still unverified: serial-device renumbering, successive flapping, app reboot recovery, live packet subscription after reconnect, touchscreen recovery timing, and long-duration stability. Do not claim these as tested.

**Next:** verify post-reconnect telemetry arrives through the existing live API and dashboard; if confirmed, publish exact current v0.8 Pi files. Consider exposing reconnect counters and timestamps in the single-node diagnostics screen without adding a second radio session.

## November 11, 2026 — post-reconnect telemetry path confirmed

Following the observed USB cable disconnect/reconnect recovery, the user ran both acceptance checks: `GET /api/status` to inspect connection state, firmware, node metadata, event counter, last event and device metrics, and `GET /api/packets/live` to inspect current live events. The user reported **both checks passed** and therefore confirmed that live event reception resumed after the radio automatically reconnected. Exact post-reconnect response bodies/counters were not pasted; no numerical values are asserted beyond the previous captured recovery trace.

**Acceptance chain now verified:** operational USB serial connection → cable removed → supervisor detected connection loss → `/dev/ttyACM0` became unavailable → cable reconnected → supervisor re-established the session without restarting Flask → subsequent real telemetry reached Flask's live APIs.

**Open work:** publish the exact latest v0.8 Pi `radio_manager.py` and `templates/index.html` sources after staged diff and privacy review; add recovery/connection counters and last state-change timestamps; optionally test USB path renumbering and boot recovery. Do not present these as already tested. RF peer reception remains untested with only one node available.

## November 11, 2026 — v0.9 connection diagnostics initial validation PASSED

The Pi-local v0.9 changes to `radio_manager.py` added a monotonic `connection_uptime_seconds` metric, in-process `successful_connections` and `reconnect_count`, and UTC `last_connected_at` / `last_disconnected_at` fields. The Mesh Nodes view now presents these values alongside existing firmware, event and error diagnostics. The user reports the **Step 5 API check and touchscreen validation passed**. Individual numerical results were not provided, so none are asserted here.

**Important verification boundary:** A repeat controlled USB disconnect/reconnect test has not yet been reported for the new v0.9 counters. Therefore `reconnect_count` incrementing to one, the updated timestamps, and connection uptime reset still need to be tested. The Pi-local v0.9 source modifications have not yet been independently verified in the published GitHub source and must be copied/reviewed before claiming a release checkpoint.

**Next acceptance:** capture `/api/status.radio` before removal, during the cable-out period, and after reconnect; verify uptime transitions `number → null → low number`, successful connections `1 → 2`, reconnect count `0 → 1`, and nonempty connection/disconnection timestamps. Do not restart Flask during the cable test.

## November 11, 2026 — v0.9 recovery instrumentation acceptance: PASS

A controlled USB cable disconnect/reconnect test was run against the current local Pi v0.9 `aegis-mesh.service` while polling `GET /api/status` every roughly three seconds. The user supplied this exact observed progression:

- Baseline connected and healthy: `Connected=True`, uptime increments from **381** to **402** seconds, `successful_connections=1`, `reconnect_count=0`, `error=None`.
- Cable-out transition: `Connected=False`, `connection_uptime_seconds=None`, `successful_connections=1`, `reconnect_count=0`, initially `ConnectionError`, then `Serial device unavailable`.
- Automatic recovery: `Connected=True`, uptime **1** second, `successful_connections=2`, `reconnect_count=1`, `error=None`.
- Follow-up observations: connected uptime increased through **4, 7, 11 and 14 seconds**; counters remained 2 successful connections and 1 recovery; no error.

**Accepted:** fault detection, disconnect-state handling, successful reconnection, monotonic uptime reset, correct connection/recovery counter increments, and cleared error state. **Not yet independently checked in this run:** values of `last_connected_at` and `last_disconnected_at`, continued new live telemetry after this particular second test, or USB-port renumbering/reboot recovery. The previous v0.8 test verified resumed live telemetry after reconnection.

**Release gate:** Pi-local v0.9 source updates to `radio_manager.py` and `src/templates/index.html` should be copied to the GitHub checkout, inspected and committed; this journal update alone does not publish the tested code.

## November 11, 2026 — AEGIS Mesh Control v1.0 single-node reboot acceptance: 5/5 PASS

The user completed the **full Raspberry Pi reboot** acceptance check after v0.9 source publication (commit `b1d0407`, `feat(AEG-006): add v0.9 connection reliability diagnostics`). All five checklist entries were independently reported **PASSED**:

1. Raspberry Pi restarted successfully and Termius/SSH access returned.
2. `aegis-mesh.service` / Flask started automatically without manual intervention.
3. The USB-attached RAK4631 automatically re-established its serial connection.
4. Fresh device telemetry appeared after reboot through the live monitoring path.
5. Chromium touchscreen kiosk restored and displayed the dashboard.

**Release decision:** **ACCEPT AEG-006 AEGIS Mesh Control v1.0 single-node baseline**. This is a functional readiness designation supported by the user's boot and telemetry validation, not a claim of multiple independent field runs, extended soak testing, or peer-to-peer RF reception. The exact post-boot HTTP response, systemd journal and timestamped screenshots were not supplied in this acceptance turn.

**Prior measured evidence:** v0.8 same-path USB recovery and post-reconnect telemetry passed. v0.9 disconnect/reconnect produced `Connected=False` with `ConnectionError` / `Serial device unavailable`, then `Connected=True`, `successful_connections 1→2`, `reconnect_count 0→1`, and uptime reset to 1 s before increasing. The source `radio_manager.py` and `templates/index.html` containing v0.9 fields were confirmed available on GitHub.

**Known limitations / deferred gates:** only one RAK4631, so no inter-node LoRa reception, peer RSSI/SNR or two-node messaging verified; no measured RF spectrum waterfall; GNSS fix, battery endurance, USB renumbering, multicycle soak testing and published photos remain open as relevant future work. Counters and recent live history reset after Flask process restart. Application is loopback-only by design.

**Publication work:** update AEG-006 project README, ROADMAP.md, PROJECTS.md and issue #6 to reflect the accepted v1.0 baseline; preserve these exact functional limits. Do not conflate this baseline acceptance with acceptance of all AEG-006 future enhancements or of AEG-002 as a whole.
