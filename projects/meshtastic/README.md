# AEG-002 — Meshtastic Rugged Field Node
**Phase (November 11, 2026):** USB-connected node fully integrated and verified with AEG-006 AEGIS Mesh Control v1.0. Firmware, identity, local telemetry, safe event history, disconnect/reconnect and reboot recovery passed. AEG-002 field-hardware qualification (GNSS fix, OLED, BLE, power/endurance and enclosure) remains open.
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
With AEG-006 v1.0 accepted, **validate a fresh GNSS satellite fix** using the existing RAK12501 antenna outdoors, without publicly logging coordinates. Then verify the actual OLED module SKU and compatible slot before installation, and perform a controlled Bluetooth pairing test with the mobile app. Verify the sensor-module SKU from its markings. Two-node messaging, battery/endurance and the rugged enclosure remain later phases; **no additional hardware purchase is required for the immediate checks**. Keep CLIENT role and the US/LONG_FAST configuration unless a specific test requires a deliberate, documented change. The previously planned Flask integration, event-history UI, USB fault recovery and automatic boot are now complete for the single-node baseline. See [AEG-006 v1.0 release evidence](../tactical-control-terminal/README.md) and [the Meshtastic test plan](test-plan.md).

[Tracking issue](https://github.com/k41ju0x/Project-AEGIS/issues/2)
