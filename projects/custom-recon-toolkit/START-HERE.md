# AEG-009 — Start in the Kali VM

Run these commands in the existing **Kali VM**, not the Raspberry Pi or Windows PowerShell. This prepares a working directory; it does not install the scanner.

## 1. Check the environment
```bash
python3 --version
nmap --version
```
Record the outputs. Python runs the custom utilities; Nmap provides an independent comparison. If either command fails, resolve that prerequisite before continuing.

## 2. Create an isolated Python workspace
```bash
mkdir -p ~/projects/aegis-recon
cd ~/projects/aegis-recon
python3 -m venv .venv
source .venv/bin/activate
python --version
```
`venv` isolates future Python dependencies from Kali's system packages. No pip packages are required for the planned standard-library scanner. If virtual environment creation reports missing venv support, record the error before changing packages.

## 3. Start a controlled local listener
In the same terminal:
```bash
mkdir -p lab-web
python -m http.server 8765 --bind 127.0.0.1 --directory lab-web
```
This serves an empty lab directory and listens only on this machine's loopback interface. Keep it running. If port 8765 is occupied, stop and inspect the existing listener rather than terminating an unknown process.

## 4. Establish the comparison result
Open a second Kali terminal:
```bash
ss -ltn 'sport = :8765 or sport = :8766'
nmap -sT -Pn -n -p 8765,8766 127.0.0.1
```
- `ss -ltn` displays listening TCP sockets, verifying whether the test ports are already occupied.
- `-sT` uses full TCP connections, matching the planned Python scanner's basic mechanism.
- `-Pn` skips host discovery for this known local target.
- `-n` skips DNS resolution.
- `-p` restricts the comparison to two selected ports.

Expected: **8765 open** while the server is running; **8766 closed** only if nothing is listening there and the local network policy rejects the connection. Treat actual output as evidence; do not label an unexpected result a scanner bug before checking listeners and firewall behavior.

## 5. Stop the lab listener
Press Ctrl+C in the server terminal. Repeat the same Nmap command. Port 8765 should now report closed under the same assumptions.

## Next session
Provide Python/Nmap versions and both comparison results. Keep raw results local. We will use this known target to validate the first custom scanner. No external target or additional hardware is needed.
