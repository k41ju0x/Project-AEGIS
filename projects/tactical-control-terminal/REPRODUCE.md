# AEG-006 — Reproduction Guide (Repository Source)


> **Privacy and paths:** `<TCT_HOSTNAME>` is a placeholder; choose your own name when imaging the Pi. `~/tct-app` and `/home/aegis/tct-app` are example deployment paths selected for this sanitized walkthrough, not verified original device paths. Use the same actual account and application directory consistently throughout the service configuration.
**Last reviewed:** 2026-11-08  
**Build:** Raspberry Pi 5 (8GB), Raspberry Pi Touch Display 2, Active Cooler, Raspberry Pi OS 64-bit with Desktop (Debian Trixie), `<TCT_HOSTNAME>` hostname.

> This guide is a **repeatable deployment procedure reconstructed from the published source and verified architecture**, not a verbatim record of every original terminal command. For commands that were observed in the build and their results, read the [engineering build journal](docs/build-journal.md). I have not re-executed this exact clean-install procedure end to end on a fresh Pi. Use owned/authorized equipment and review commands before execution.

## 1. Prepare and verify Raspberry Pi OS

Use Raspberry Pi Imager to write **Raspberry Pi OS (64-bit) with Desktop** to microSD. In Imager OS customization, create the `aegis` login, set your own hostname (`<TCT_HOSTNAME>`), select the local timezone, configure networking and enable SSH. Connect official display DSI, power and fan wiring while unpowered; use the official Pi 5 power supply. After boot, connect from a trusted administrator machine:

```bash
ssh aegis@<PI_LAN_IP>
cat /etc/os-release
getconf LONG_BIT
python3 --version
command -v chromium
sudo apt update
sudo apt full-upgrade
sudo rpi-eeprom-update
```

Replace `<PI_LAN_IP>` privately. The original build used Debian 13 Trixie, Python 3.13.5 and Chromium; if versions differ, confirm dependency support before continuing. Reboot only when required by updates and first ensure you can reconnect.

## 2. Obtain the published application source

On the Pi, in the `aegis` account:

```bash
cd ~
git clone https://github.com/k41ju0x/Project-AEGIS.git aegis-portfolio
mkdir -p ~/tct-app
cp -a ~/aegis-portfolio/projects/tactical-control-terminal/src ~/tct-app/
cp ~/aegis-portfolio/projects/tactical-control-terminal/requirements.txt ~/tct-app/
python3 -m venv ~/tct-app/.venv
~/tct-app/.venv/bin/python -m pip install -r ~/tct-app/requirements.txt
~/tct-app/.venv/bin/python -m pip show Flask meshtastic
```

If `python3 -m venv` fails, install the version-appropriate `python3-venv` package on the supported OS. The exact pinned dependencies are in the repository `requirements.txt`. Installation requires package network access.

## 3. Run and test the application directly

The published `src/app.py` starts Flask on **127.0.0.1:5000**, initializes the bounded in-memory synthetic packet store and labels events as test data.

```bash
cd ~/tct-app/src
~/tct-app/.venv/bin/python app.py
```

From a **second SSH session to the Pi**:

```bash
curl -fsS http://127.0.0.1:5000/api/status
curl -fsS http://127.0.0.1:5000/api/rf
curl -fsS http://127.0.0.1:5000/api/packets
```

Expect an online status, **radio_connected=false** and `synthetic_test` packet metadata. Do **not** present these as real Meshtastic traffic. The first interactive process can be stopped with Ctrl+C after checking the APIs.

## 4. Configure an autostart service (example to reproduce the published architecture)

The repository contains verified application source but **does not currently include the original installed systemd unit**. The unit below is an explicitly labeled **reconstruction**, not a claim that this is a byte-for-byte copy of the device's original service.

```bash
sudo tee /etc/systemd/system/aegis-mesh.service >/dev/null <<'UNIT'
[Unit]
Description=AEGIS Mesh Control local dashboard
After=network.target

[Service]
Type=simple
User=aegis
WorkingDirectory=/home/aegis/tct-app/src
ExecStart=/home/aegis/tct-app/.venv/bin/python /home/aegis/tct-app/src/app.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable --now aegis-mesh.service
systemctl is-active aegis-mesh.service
sudo journalctl -u aegis-mesh.service --no-pager -n 30
curl -fsS http://127.0.0.1:5000/api/status
```

If the account name or home directory differs, **edit the unit first**. Do not make the Flask development server publicly reachable. The packaged source is a prototype; production exposure requires a hardened deployment and authentication.

## 5. Local touchscreen kiosk (example to reproduce the original approach)

The original working Pi uses the Raspberry Pi OS `labwc` desktop autostart mechanism with Chromium fullscreen and a basic password store to avoid a kiosk keyring prompt. The **exact original autostart line was not preserved** in the build transcript. A starting example for a dedicated local kiosk session is:

```bash
mkdir -p ~/.config/labwc
cat >> ~/.config/labwc/autostart <<'EOF'
chromium --kiosk --no-first-run --password-store=basic http://127.0.0.1:5000 &
EOF
```

Ensure the selected desktop session is actually **labwc** and graphical autologin is configured only in an appropriately controlled environment. Repeatedly running the append command duplicates the autostart entry; review `~/.config/labwc/autostart` before applying it again. A local kiosk is not remote access authentication. Reboot and test touch navigation after configuration.

## 6. Validate telemetry and documented limits

```bash
systemctl status aegis-mesh.service --no-pager
curl -fsS http://127.0.0.1:5000/api/status
curl -fsS http://127.0.0.1:5000/api/rf
curl -fsS http://127.0.0.1:5000/api/packets
ls -l /sys/class/hwmon/
cat /sys/class/thermal/thermal_zone0/temp
```

The v0.6 UI uses synthetic sample nodes; the actual RAK4631 radio integration, physical RF spectrum collection, greater-than-10-record history testing and original photo evidence are not complete.

## 7. Recovery and privacy

- Keep SSH administration working before changing any kiosk or display setting.
- Review `sudo journalctl -u aegis-mesh.service --no-pager -n 50` and `systemctl status aegis-mesh.service` when a service fails.
- Preserve original settings and screenshots **privately** before disruptive changes. Do not commit passwords, SSH keys, channel encryption keys, network IPs, raw captures, or private location data.
- Record OS versions, package installation failures, the observed output of each verification command, and any differences from the published source in the dated build journal.

## Provenance and test coverage

The original build **did** verify: graphical Pi OS and touchscreen, Active Cooler, Python/Meshtastic/Flask, SSH, `aegis-mesh.service` boot startup, Chromium/labwc kiosk, local dashboard, REST API telemetry, and v0.6 synthetic event UI. The procedure in this guide is **inferred from those verified results and committed source**, not a substitute for clean-room reproduction evidence. Follow the [original build journal](docs/build-journal.md) and [project README](README.md) to distinguish historical steps from reconstruction.
