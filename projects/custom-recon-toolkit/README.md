# AEG-009 — Custom Recon Toolkit

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Software Development
**Complexity:** Medium
**Suggested phase:** Phase 1

## Charter and objective
Create auditable Python network discovery utilities and compare their behavior to established tools.

## Preliminary hardware and software (not purchased)
Development laptop or VM; Python; isolated test network; GitHub CI.

## Research and implementation scope
TCP connect scanning; rate limits; timeouts; output formats; DNS/subdomain enumeration against owned zones; Nmap comparison.

## Defensive validation
Network monitoring; logging; asset inventory; alerting on scanning.

## Showcase / acceptance criteria
Unit tests and a reproducible lab comparison of correctness, runtime, and generated telemetry.

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
