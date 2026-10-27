# AEG-002 — Meshtastic Project Charter
**Initiated:** 2026-10-26  
**Phase:** Planning / requirements baseline  
**Tracking:** https://github.com/k41ju0x/Project-Aegis/issues/2  
**Visibility:** Public sanitized planning; sensitive operational configurations private.

## Purpose
Build and document a portable, off-grid LoRa messaging node running Meshtastic. Learn RF hardware integration, firmware, power management, configuration, and disciplined field validation. Explore a second node or fixed relay later if justified by tests.

## Desired v1 outcome
A portable battery-powered Meshtastic node that:
1. Boots reliably with a suitable antenna attached.
2. Can be paired to a supported client or otherwise managed locally.
3. Sends and receives messages to another compatible node under an authorized, lawful test setup.
4. Can be recharged and operated for a measured period with test conditions recorded.
5. Has reproducible assembly/configuration notes and verified results.

## In scope
Hardware/platform selection, regional radio compliance, matched antenna, charging and battery safety, firmware flashing, enclosure planning, pairing and messaging, measurement, test logs, and documentation.

## Out of scope (initial version)
Voice calls, broadband data, guaranteed internet access, universal coverage, covert tracking, unattended solar infrastructure, and claims of emergency-service reliability.

## Open decisions
- Portable compact vs rugged field enclosure (no commitment yet)
- Budget and required battery runtime
- GPS, OLED, physical controls, weather resistance
- Need for a second owned test node vs coordination with an existing mesh
- Where and how tests will be conducted

## Success gate
REQ-001 through REQ-006 evaluated with documented acceptance evidence; unresolved features explicitly recorded rather than assumed.

## Risks
RF compliance/local rules, antenna damage from transmitting unloaded, incorrect battery polarity/charging, nonrepresentative range claims, exposed location/channel secrets. See [risk register](risk-register.md).

## Next action
Confirm intended form factor, budget, and mandatory features; compare supported hardware; select core platform in an ADR before purchasing.
