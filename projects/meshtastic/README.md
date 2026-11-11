# AEG-002 — Meshtastic Rugged Field Node
**Phase (November 11, 2026):** Kit received November 10; antennas installed; RAK4631 USB/Meshtastic firmware, US region, LONG_FAST, node identity and standalone Python telemetry/event callbacks verified. Peer messaging and full field validation pending.  
**Core:** RAK4631 / RAK19007 US915 Client-Tracker with RAK12501 GNSS, RAK1921-series OLED (exact label to reconfirm) and RAK1904 sensor (inventory photographed; GNSS/core inspected; OLED still uninstalled and sensor SKU unverified)  
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
Continue from **verified USB-connected node**: integrate local `radio_manager.py` into AEG-006 Flask API after reviewing routes, then test live telemetry, safe packet history and connection recovery. Copy exact locally tested source to GitHub before claiming v0.7 release. OLED, BLE pairing, fresh GNSS fix, second-node communications, battery and enclosure remain unverified. See [build log](build-log.md). Battery, Hammond enclosure and sealed RF feedthrough remain proposed, not purchased; check JST polarity and mechanical fit before any separate purchases. No measured runtime or assembled-device ingress rating yet.

[Tracking issue](https://github.com/k41ju0x/Project-AEGIS/issues/2)
