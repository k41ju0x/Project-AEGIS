# AEG-002 — Meshtastic
**Project:** Portable LoRa mesh communications prototype  
**Status:** Planning (engineering docs baseline; hardware not selected)  
**Tracking issue:** [AEG-002](https://github.com/k41ju0x/Project-AEGIS/issues/2)  
**Visibility:** Public sanitized summary / private sensitive RF and location configuration

## Mission
Design, build and field-test a reliable battery-powered Meshtastic node, learning RF selection, hardware assembly, configuration, power engineering, and repeatable validation.

## Current state
- Completed: first-pass charter, requirements matrix, hardware research shortlist, risk register, draft validation plan, and dated documentation log.
- Pending: hardware and antenna selection, budget, battery/runtime target, feature selection, procurement, assembly, firmware flashing, tests.
- No performance or range measurements have been claimed.

## Documentation
| Document | Purpose |
|---|---|
| [Charter](charter.md) | Purpose, scope and success gates |
| [Requirements](requirements.md) | Functional and technical acceptance matrix |
| [Research journal](research.md) | Platform candidates and sources |
| [Risk register](risk-register.md) | RF, power, privacy and integration risks |
| [Test plan](test-plan.md) | TST-001 onwards; not yet executed |
| [Build log](build-log.md) | Dated decisions and results |
| [Resume here](resume-here.md) | Last state and immediate next action |

## Current technical direction
Evaluate low-power officially supported hardware (including modular RAK4631 WisBlock) before purchasing. Confirm exact RF SKU, antenna matching and Meshtastic firmware support. Plan a controlled second node or authorized existing peer for two-way tests.

## Decisions still needed
1. Form factor: compact or rugged portable?
2. Budget ceiling?
3. Mandatory GPS, display, on-device controls, weather resistance?
4. Runtime goal and conditions?
5. Second test node procurement?

## Next action
Confirm requirements and create an architecture decision record (ADR-0001) and vendor-checked bill of materials. Do not purchase prematurely.

## Safety
Use compatible charging circuitry and antenna; adhere to applicable RF rules. Keep private channel credentials and exact personal location details out of this public repository.
