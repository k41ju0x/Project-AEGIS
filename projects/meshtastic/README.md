# AEG-002 — Meshtastic Rugged Field Node
**Phase (November 11, 2026):** USB-connected node fully integrated and verified with AEG-006 AEGIS Mesh Control v1.0. Firmware, identity, local telemetry, safe event history, disconnect/reconnect and reboot recovery passed. AEG-002 field-hardware qualification (GNSS fix, OLED, BLE, power/endurance and enclosure) remains open.
**Core:** RAK4631 / RAK19007 US915 Client-Tracker with RAK12501 GNSS, RAK1921-series OLED (exact label to reconfirm) and RAK1904 sensor (inventory photographed; GNSS/core inspected; OLED now observed operational; sensor SKU unverified)  
**Runtime requirement:** 48h preferred; **24h verified fallback acceptable**  
**Visibility:** Public sanitized build notes; keep private coordinates and keys confidential.

## Earlier rugged enclosure/power concept (superseded by compact preference)
- **Battery:** Adafruit #353, protected 3.7V **6600mAh** lithium-ion (JST polarity to be verified).
- **Housing:** Hammond **1554F2GYCL** clear-lid sealed polycarbonate **120 × 90 × 60mm external**, internal fit not yet confirmed.
- **UI:** OLED visible through clear factory lid, phone text entry via Bluetooth.
- **Antenna:** Matched US915 with watertight bulkhead; exact RF connectors to verify.
- **Charging:** Open enclosure in dry indoor location; no additional USB penetration in first build.
- **Budget allowance:** **$209.32** (three catalog prices plus planning estimates, *not* a guaranteed shopping cart).

## Documents
[Charter](charter.md) · [Requirements](requirements.md) · [Architecture](architecture.md) · [Hardware decision](decisions/ADR-0001-rak4631.md) · [BOM](bom.csv) · [Procurement](procurement.md) · [Power budget](power-budget.md) · [Risk register](risk-register.md) · [Test plan](test-plan.md) · [Build log](build-log.md) · [Resume](resume-here.md)

## Next action
**Compact, phone-assisted portable node is the selected direction.** Identify a case that actually fits the RAK19007/RAK4631, installed OLED, GNSS and antennas, then select the protected 3.7V LiPo pack compatible with that case and the RAK19007 battery-connector pinout. Do not order parts until fit, polarity and seller information are checked. iPhone Bluetooth pairing and subsequent return to Pi USB ownership passed; fresh internal GNSS-sourced position reported 15 satellites and coordinate fields (no public coordinates). Two-node peer messaging, portable runtime and weather sealing remain pending. Keep CLIENT/US/LONG_FAST. See [AEG-006 v1.0 acceptance](../tactical-control-terminal/README.md) and [test plan](test-plan.md).

[Tracking issue](https://github.com/k41ju0x/Project-AEGIS/issues/2)

## November 11, 2026 — qualification progress

**Verified:** Meshtastic iPhone app pairs to the RAK4631 via BLE and establishes a working connection (user confirmation). OLED shows active node information and satellite reception; a fresh local `POSITION_APP` event reported 15 satellites, `LOC_INTERNAL` and presence of coordinates (exact location withheld). GNSS precision/fix quality was not explicitly reported. Return the Pi from the controlled BLE pairing test to USB-owned Flask monitoring before leaving it unattended. [Observed evidence](build-log.md).

## November 11, 2026 — selected portable design decision

**User-selected:** keep AEG-002 small and portable, with the existing OLED for status and the **iPhone Meshtastic app as the Bluetooth keyboard/message interface**. Do not add an onboard keyboard or touchscreen to AEG-002. The radio operates without cell service or Wi-Fi; sending to others requires a reachable compatible peer/mesh. Reuse the RAK4631/RAK19007, existing working antennas, GNSS and OLED. The spare PiSugar 3 is **not** selected for this radio. Select a compatible protected 3.7V single-cell LiPo and physically fitting compact enclosure together; exact case and battery SKU are **not yet finalized or purchased**. Previous 6600mAh/Hammond proposal remains historical context, not the active compact-build choice. No second radio purchase planned.
