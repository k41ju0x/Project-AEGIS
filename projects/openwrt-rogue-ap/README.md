# AEG-008 — OpenWrt Rogue AP Lab

**Status:** Proposed / Backlog (not started; no procurement authorized)
**Track:** Wireless & Network
**Complexity:** High
**Suggested phase:** Phase 2

## Charter and objective
Build an isolated OpenWrt access-point research rig and validate client and network defenses.

## Preliminary hardware and software (not purchased)
Compatible GL.iNet OpenWrt router; isolated lab uplink; test clients; optional second AP.

## Research and implementation scope
AP configuration; SSID/BSSID observations; network segmentation; controlled rogue AP identification.

## Defensive validation
WIDS/WIPS; trusted network profiles; certificate validation; 802.1X policies.

## Showcase / acceptance criteria
Detect an unauthorized lab AP and show client/network defenses without targeting third-party devices.

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
