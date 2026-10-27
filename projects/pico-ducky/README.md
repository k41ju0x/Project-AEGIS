# AEG-006 — Pico Ducky / HID Research

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Hardware & Embedded
**Complexity:** Medium
**Suggested phase:** Phase 1

## Charter and objective
Build a Raspberry Pi Pico-based USB HID security research device and demonstrate endpoint defenses.

## Preliminary hardware and software (not purchased)
Raspberry Pi Pico/Pico W; USB cable; optional case; isolated Windows/Linux test endpoint.

## Research and implementation scope
USB HID enumeration; harmless scripted keystrokes on an owned test machine; payload provenance; USB device control; endpoint logs.

## Defensive validation
USB device allowlisting; endpoint telemetry; user-session locking; HID device alerts.

## Showcase / acceptance criteria
Controlled demo performs benign text entry only; logs show device connection; mitigation prevents or alerts on unapproved HID.

## Milestones
1. M0 — Confirm authorization boundaries, test environment, and success metrics.
2. M1 — Research architecture, compatibility, safety, and draft bill of materials.
3. M2 — Build or configure a minimum viable lab prototype.
4. M3 — Execute repeatable functional and security tests; record evidence.
5. M4 — Validate defensive controls and publish a sanitized walkthrough.
6. M5 — Retrospective, lessons learned, and backlog for v2.

## Safety, privacy and scope
Use only owned or explicitly authorized equipment, accounts, badges, applications and networks. Isolate experiments from production and third-party systems. Never collect or publish real credentials, private network location data, access tokens, or sensitive packet captures. Obtain authorization before any active wireless or network testing. Maintain logs and a documented teardown procedure.

## Project state and next action
**Current:** Idea registered; hardware, budget, schedule and detailed requirements are TBD.
**Next:** Approve a project-specific requirements document and compatibility research before ordering parts.
