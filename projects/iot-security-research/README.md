# AEG-014 — IoT Security Research Platform

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Hardware & Embedded
**Complexity:** Very High
**Suggested phase:** Phase 3

## Charter and objective
Perform end-to-end authorized research on a disposable smart-home device across firmware, network, application and cloud surfaces.

## Preliminary hardware and software (not purchased)
Owned smart plug or camera; isolated IoT VLAN; serial adapter; logic analyzer optional; capture workstation.

## Research and implementation scope
Hardware inventory; firmware acquisition where lawful; network telemetry; mobile app/API observations; update and credential review.

## Defensive validation
Segmentation; secure updates; credential rotation; TLS verification; telemetry.

## Showcase / acceptance criteria
Produce a complete device threat model, findings, mitigations, and repeatable validation tests.

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
