# AEG-009 — Custom Reconnaissance Toolkit

**Status:** In Progress — requirements and lab preparation (November 13, 2026)
**Track:** Software Development
**Visibility:** Public planning and sanitized learning records; scan evidence stays local.

## Objective
Build understandable Python discovery utilities, then add reproducible automation around established tools. Explain each command and result so the project can support teaching as well as practical lab work. APEX and Project NEXUS remain separate.

## First milestone: v0.1 TCP connect scanner
Use the existing Kali VM. No additional hardware or paid services are required. Start with one literal IPv4 address and explicitly selected TCP ports. The scanner will apply timeouts and rate limits, record outcomes, and export JSON and CSV plus a readable summary. Compare the result with Nmap against the same local test service.

**Current evidence:** Planning documents published; scanner implementation and user-machine testing have not started. This is not a released v0.1.

## Documents
- [Requirements and architecture](requirements.md)
- [Kali lab setup and first checks](START-HERE.md)
- [Acceptance test plan](test-plan.md)
- [Build log and next session](build-log.md)

## Development sequence
1. Prepare the Kali working directory and record Python/Nmap versions.
2. Create a separate implementation repository under the hub's graduation policy.
3. Implement and test port parsing and explicit scope checks.
4. Implement sequential TCP connection probes with rate limits and timeouts.
5. Add output files and command/run metadata; test on localhost.
6. Compare with Nmap and record actual differences.
7. Later: owned-zone DNS enumeration and optional tool adapters.

## Boundaries
v0.1 does not perform exploitation, credential testing, stealth scans, UDP discovery, CIDR sweeps, or automatic follow-on scanning. Tests start on loopback; later targets must be explicitly authorized. Keep real target inventories, reports and packet captures out of the public hub.

**Next action:** Complete START-HERE.md in the Kali VM and capture the version output. No procurement is needed.
