# AEG-007 — RFID/NFC Security Lab

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Hardware & Embedded
**Complexity:** Medium
**Suggested phase:** Phase 2

## Charter and objective
Analyze legacy 125 kHz proximity and 13.56 MHz NFC technologies using owned test credentials.

## Preliminary hardware and software (not purchased)
Proxmark3 for broad LF/HF research; PN532 for 13.56 MHz only; owned test tags; isolated reader.

## Research and implementation scope
Frequency and protocol identification; authorized reads; controlled duplicate test tokens where permitted; reader behavior comparison.

## Defensive validation
Modern cryptographic credentials; diversified keys; reader configuration; audit trails.

## Showcase / acceptance criteria
Demonstrate security differences using disposable lab credentials without copying active access badges.

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
