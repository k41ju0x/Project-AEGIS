# AEG-002 — Meshtastic Rugged Field Node
**Phase:** Kit ordered; awaiting delivery, inventory and bench testing (as of November 1, 2026)  
**Core:** RAK4631 / RAK19007 US915 Client-Tracker with RAK12501 GNSS, RAK19221 OLED and RAK1904 sensor (ordered kit configuration; delivered contents not yet checked)  
**Runtime requirement:** 48h preferred; **24h verified fallback acceptable**  
**Visibility:** Public sanitized build notes; keep private coordinates and keys confidential.

## Selected candidate enclosure and power
- **Battery:** Adafruit #353, protected 3.7V **6600mAh** lithium-ion (JST polarity to be verified).
- **Housing:** Hammond **1554F2GYCL** clear-lid sealed polycarbonate **120 × 90 × 60mm external**, internal fit not yet confirmed.
- **UI:** OLED visible through clear factory lid, phone text entry via Bluetooth.
- **Antenna:** Matched US915 with watertight bulkhead; exact RF connectors to verify.
- **Charging:** Open enclosure in dry indoor location; no additional USB penetration in first build.
- **Budget allowance:** **$209.32** (three catalog prices plus planning estimates, *not* a guaranteed shopping cart).

## Documents
[Charter](charter.md) · [Requirements](requirements.md) · [Architecture](architecture.md) · [Hardware decision](decisions/ADR-0001-rak4631.md) · [BOM](bom.csv) · [Procurement](procurement.md) · [Power budget](power-budget.md) · [Risk register](risk-register.md) · [Test plan](test-plan.md) · [Build log](build-log.md) · [Resume](resume-here.md)

## Next action
Inventory the ordered single-node RAK4631 / RAK19007 US915 kit on arrival, verify modules/antenna, then begin bench testing. Battery, Hammond enclosure and sealed RF feedthrough remain proposed, not purchased; check JST polarity and mechanical fit before any separate purchases. No measured runtime or assembled-device ingress rating yet.

[Tracking issue](https://github.com/k41ju0x/Project-AEGIS/issues/2)
