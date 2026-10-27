# AEG-002 — Meshtastic Rugged Field Node
**Status:** Planning — RAK4631 selected, procurement pending  
**Requirements:** Rugged portable; budget **$250+** (no upper ceiling agreed); GPS, screen, weather-resistant enclosure; target **48 h measured** runtime.  
**Tracking:** [AEG-002](https://github.com/k41ju0x/Project-AEGIS/issues/2)  
**Visibility:** Public sanitized overview, private sensitive configurations.

## Selected architecture
**RAK4631** (nRF52840 + SX1262) with **RAK19007** baseboard; a US915 kit variant; **RAK12501 GNSS** and **RAK1921 OLED**; protected 1S LiPo battery; properly matched external antenna; customized gasketed enclosure. BLE phone provides text input. Follow the [architecture](architecture.md) and [ADR-0001](decisions/ADR-0001-rak4631.md).

## Engineering package
- [Charter](charter.md) · [Requirements](requirements.md) · [Research](research.md)
- [Architecture](architecture.md) · [Hardware decision](decisions/ADR-0001-rak4631.md)
- [Estimated bill of materials](bom.csv) · [Cost and procurement notes](procurement.md)
- [48-hour power model](power-budget.md) · [Risks](risk-register.md)
- [Test plan](test-plan.md) · [Build log](build-log.md) · [Resume notes](resume-here.md)

## Outstanding before purchasing
Confirm precise **Client-Tracker/RAK19007/US915** bundle contents and pricing; choose compatible battery with verified polarity and charger limits; select physical enclosure, screen mounting, sealed cable entries and antenna connector. A second compatible test node or authorized peer is required to test message exchange.

**Current evidence:** Architecture selected, no hardware assembled, RF/ingress protection or battery life verified. Avoid publishing exact coordinates or channel secrets.
