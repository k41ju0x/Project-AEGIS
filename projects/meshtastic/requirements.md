# AEG-002 — Requirements Baseline v1.0
**Date:** 2026-10-26 · **State:** User-confirmed objectives; acceptance tests pending.

| ID | Priority | Requirement | Acceptance evidence |
|---|---|---|---|
| REQ-001 | Must | Selected Meshtastic platform is RAK4631, compatible Arduino-bootloader version | Identify SKU, firmware and two successful boots |
| REQ-002 | Must | US-compatible radio and matched attached antenna | Verify US915 SKU, local regulatory suitability and firmware region before transmission |
| REQ-003 | Must | Bidirectional text messaging to compatible authorized peer | Time-stamped send/receive logs from two nodes |
| REQ-004 | Must | Rechargeable battery with **48-hour operating target** | Run a continuous 48h test with GPS/display and ordinary messaging workload documented |
| REQ-005 | Must | Built-in working GPS/GNSS | GNSS lock and opt-in location readback demonstrated |
| REQ-006 | Must | Built-in functional display | Readable status / message-related display test |
| REQ-007 | Must | Rugged portable enclosure with weather-resistant construction | Inspect sealing, strain relief and environmental exposure method; do not claim certified IP rating without testing |
| REQ-008 | Must | Phone connection for Meshtastic configuration and message composition | Pair and exchange messages from supported client |
| REQ-009 | Must | Reproducible, sanitized build | BOM, wiring, assembly, firmware version, test evidence documented |
| REQ-010 | Should | Device cost within user-approved scope | Per-node itemized checkout total reviewed before procurement; $250+ is a budget band, not a fixed ceiling |

## Open test parameters
- GPS acquisition frequency (continuous vs interval), OLED brightness/timeout, transmit/receive load, Bluetooth use and temperature must be recorded.
- Runtime target is **not** a claimed battery specification. Battery capacity and firmware behavior will be verified.
- Enclosure ingress protection rating of raw box does not transfer automatically to drilled/modified finished assembly.
- Range is not guaranteed and will be evaluated separately based on terrain/antenna height.
