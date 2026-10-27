# AEG-012 — Evil Twin Defense Lab

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Wireless & Network
**Complexity:** High
**Suggested phase:** Phase 3

## Charter and objective
Study client trust decisions around lookalike APs and captive portals in a controlled RF/network lab.

## Preliminary hardware and software (not purchased)
Dedicated lab AP/router; test clients; isolated SSIDs; synthetic test identities; capture/monitoring system.

## Research and implementation scope
Controlled SSID impersonation; captive portal UX; client association and certificate behavior; no collection of real credentials.

## Defensive validation
WPA3-SAE; WPA-Enterprise/802.1X certificate validation; trusted profiles; rogue AP detection.

## Showcase / acceptance criteria
Reproduce a lab-only impersonation scenario using synthetic credentials and verify defenses.

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
