# AEG-002 — Initial Requirements & Acceptance Plan
**State:** Proposed baseline — thresholds and options to be confirmed before acquisition.

| ID | Level | Requirement | Proposed validation |
|---|---|---|---|
| REQ-001 | Must | Device runs an officially supported Meshtastic firmware target | Record platform, firmware release, successful boot |
| REQ-002 | Must | RF variant and antenna are appropriate for applicable US regional rules | Photograph/record labels, antenna rating and configured region; verify local obligations |
| REQ-003 | Must | Node can communicate with a second compatible, authorized node | Exchange bidirectional test messages and record received packets, timestamps and conditions |
| REQ-004 | Must | Node operates from a safely integrated rechargeable battery | Inspect electrical compatibility, charge safely, measure actual endurance |
| REQ-005 | Must | Local configuration and messaging available via supported client/interface | Document successful pairing/connectivity and configuration readback |
| REQ-006 | Must | Build can be replicated from sanitized records | Versioned BOM, wiring/configuration notes, build journal, test results |
| REQ-007 | Should | Portable protective enclosure | Assess fit, connector strain, accessibility and thermal considerations |
| REQ-008 | Could | GPS position capability | Verify opt-in location acquisition and privacy behavior if installed |
| REQ-009 | Could | Display and user controls | Verify usability in anticipated environment if installed |
| REQ-010 | Could | Future fixed/solar relay compatibility | Evaluate after v1 field results |

## Parameters requiring user choices
- Target runtime: TBD hours (measure; don't promise prematurely)
- Budget: TBD USD
- Range target: TBD and conditioned on geography, antenna height, and obstacles
- Weather resistance: TBD, do not claim IP certification without testing
- Enclosure dimensions / weight: TBD

## Acceptance notes
One Meshtastic node cannot demonstrate end-to-end messaging alone. Plan for two compatible nodes or an authorized reachable peer. Record software versions, environment, antenna and physical placement for every RF test.
