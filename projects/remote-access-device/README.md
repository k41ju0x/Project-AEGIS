# AEG-004 — Portable LattePanda Remote Access Device

**Status:** Parked idea / not approved for purchase or build  
**Platform decision:** LattePanda (not a separate Raspberry Pi drop box)  
**Tracking:** [AEG-004 issue #4](https://github.com/k41ju0x/Project-AEGIS/issues/4) · [Canonical registry](../../PROJECTS.md)

## Purpose

I plan to design a portable, high-performance, authorized remote administration and security-assessment device based on a **LattePanda** single-board computer. This is **one unified project** incorporating concepts previously split across:

- AEG-004 Remote Access Device / headless assessment drop box
- Former AEG-005 Portable LattePanda Platform
- Former AEG-010 Raspberry Pi Remote Access Node / drop box

**These former project names have been merged into AEG-004, but the IDs AEG-005 and AEG-010 are now reassigned to ESP32 Marauder and ESP32 GPS Wardriver. I will not build a separate Raspberry Pi drop box.**

## Preliminary concept (subject to research)

- Primary use: **headless** field deployment, with an optional local GUI when required.
- OS concept: **Kali Linux** booted directly from local storage, subject to hardware/driver compatibility.
- Secure management candidates: WireGuard and/or authenticated reverse SSH with approved endpoints, auditable connection logs and a reliable recovery method.
- Physical form factor: ventilated protective enclosure, potentially Pelican-style, with cooling.
- Energy objective: investigate an approximately **eight-hour battery target**, with optional external power bank; this is **not** an established capability or a purchase commitment.
- Performance: select the most capable suitable LattePanda after requirements and power budgeting, rather than purchasing hardware prematurely.

## Authorization, security and test constraints

Use only devices, infrastructure and networks I own or have explicit permission to administer or assess. Require strong authentication, least privilege, logging, safe teardown and defensive testing of network access/egress detection. Do not expose credentials, actual endpoints or private infrastructure details in public documents.

## Planned lifecycle

1. Define authorized lab use cases, network scope and measurable acceptance criteria.
2. Compare candidate LattePanda models for Kali, power consumption, cooling, networking, storage and expansion.
3. Design encrypted remote-management connectivity, recovery and audit logs.
4. Specify enclosure, power budget and battery feasibility before hardware selection.
5. After explicit approval, build the prototype and test reliability, secure access and detection controls.
6. Publish sanitized command-by-command implementation and validation notes.

## Current decision

**This project remains parked.** I am prioritizing existing AEGIS projects and am not buying anything for AEG-004 now. Historical references to the old LattePanda/drop-box concepts should point here; current AEG-005 and AEG-010 refer to their ESP32 projects.
