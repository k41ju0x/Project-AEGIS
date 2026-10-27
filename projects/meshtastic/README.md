# AEG-002 — Meshtastic Rugged Field Node
**Phase:** Detailed hardware planning (no orders placed)  
**Core:** RAK4631 / RAK19007 US915 Client-Tracker with RAK12501 GNSS and RAK1921 OLED  
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
Validate exact configured kit checkout, **JST polarity**, internal enclosure clearance and matching watertight SMA feedthrough before placing orders. No measured runtime or waterproof rating for assembled device yet.

[Tracking issue](https://github.com/k41ju0x/Project-AEGIS/issues/2)
