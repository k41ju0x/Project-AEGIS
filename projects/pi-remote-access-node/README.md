# AEG-010 — Raspberry Pi Remote Access Node

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Remote Operations
**Complexity:** High
**Suggested phase:** Phase 3

## Charter and objective
Engineer an authorized remotely managed field node with robust reconnect and strong access controls.

## Preliminary hardware and software (not purchased)
Raspberry Pi 4/5 or equivalent; storage; case; optional PoE HAT; managed lab network.

## Research and implementation scope
WireGuard or authenticated SSH management; boot-time recovery; patching; audit logging; network fault simulation.

## Defensive validation
Asset inventory; egress monitoring; host and network logs; switch-port controls.

## Showcase / acceptance criteria
Reconnection reliability and defender detection documented on an explicitly authorized lab network.

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
