# AEG-004 — Portable LattePanda Remote Access Device

**Status:** Hardware ordered; awaiting shipment and delivery. Build and software deployment not started (November 8, 2026)  
**Platform decision:** Original LattePanda Sigma, Intel Core i5-1340P, **32GB RAM with bundled SSD and Wi-Fi**  
**Tracking:** [AEG-004 issue #4](https://github.com/k41ju0x/Project-AEGIS/issues/4) · [Canonical registry](../../PROJECTS.md)

## Purpose

I plan to design a portable, high-performance, authorized remote administration and security-assessment device based on a **LattePanda** single-board computer. This project combines secure remote management, headless security assessment, and optional local GUI capabilities into one hardware build.

## Preliminary concept (subject to research)

- Primary use: **headless** field deployment, with an optional local GUI when required.
- OS concept: **Kali Linux** booted directly from local storage, subject to hardware/driver compatibility.
- Secure management candidates: WireGuard and/or authenticated reverse SSH with approved endpoints, auditable connection logs and a reliable recovery method.
- Physical form factor: ventilated protective enclosure, potentially Pelican-style, with cooling.
- Energy objective: investigate an approximately **eight-hour battery target**, with optional external power bank; this is **not** an established capability or a purchase commitment.
- Performance: **original LattePanda Sigma 32GB** purchased as the preferred platform; validate actual firmware, storage and radio/wireless module details on arrival.

## Authorization, security and test constraints

Use only devices, infrastructure and networks I own or have explicit permission to administer or assess. Require strong authentication, least privilege, logging, safe teardown and defensive testing of network access/egress detection. Do not expose credentials, actual endpoints or private infrastructure details in public documents.

## Planned lifecycle

1. Define authorized lab use cases, network scope and measurable acceptance criteria.
2. Compare candidate LattePanda models for Kali, power consumption, cooling, networking, storage and expansion.
3. Design encrypted remote-management connectivity, recovery and audit logs.
4. Specify enclosure, realistic power budget and battery feasibility before selecting additional peripherals.
5. After delivery and inventory, assemble, install Kali, and test reliability, secure access and detection controls.
6. Publish sanitized command-by-command implementation and validation notes.

## Current decision

**Hardware procurement milestone (November 8, 2026):** Ordered the original **LattePanda Sigma 32GB SSD + Wi-Fi bundle**. Shipping was estimated at approximately **five weeks from order** (around December 13, 2026, not a guaranteed dispatch or delivery date). Exact bundled SSD capacity and Wi-Fi model should be verified from order confirmation and upon arrival; no price or order identifiers are published. **Current status: awaiting shipment.** Kali compatibility, cooling, Pelican-style enclosure, remote administration and eight-hour battery runtime remain untested. The project is uniquely identified as **AEG-004**; AEG-005 and AEG-010 are separate ESP32 projects.
