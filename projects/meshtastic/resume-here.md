# AEG-002 — Resume Here
**Updated:** 2026-11-11  
**Stage:** Kit received November 10; RAK4631 antennas attached, USB serial and Meshtastic 2.7.15 firmware verified, US/LONG_FAST set, node identity `AEGIS-MESH-01`/`AE01` verified. Standalone Python radio manager receives telemetry/position callbacks. Flask v0.6 integration still pending. Battery/enclosure candidates not purchased.

## Selected / proposed
- RAK4631 + RAK19007 US915 Client-Tracker, GNSS, OLED
- **Candidate battery:** Adafruit 353 protected 3.7V 6600mAh, 69×54×18mm
- **Candidate enclosure:** Hammond 1554F2GYCL clear-lid polycarbonate, 120×90×60mm external
- **Runtime:** 48-hour preferred; 24-hour accepted fallback **only if verified through testing**.
- **Mechanical:** No window cutout; antenna needs sealed bulkhead; charge with lid open in dry indoor setting.
- **Budget allowance:** $209.32 (mix of observed catalog prices and estimates, excluding test node).

## Unverified / before purchase
Enclosure dry-fit/internal clearances, OLED function, exact accessory sensor SKU, battery JST polarity and charging compatibility, alternative antenna interfaces, fresh GNSS fix, phone/BLE pairing, peer-to-peer communications and runtime. USB radio communications ARE verified, but reconnect-under-unplug is not.

## Next action
Inspect the AEG-006 Flask app routes; integrate already-tested `~/aegis-tct/src/radio_manager.py` into backend without serial contention; preserve synthetic data in a separate demo source, test APIs and kiosk, then publish the *exact tested code*. See [build log](build-log.md). Keep optional hardware purchases deferred.

[Overview](README.md) · [BOM](bom.csv) · [Procurement](procurement.md) · [Runtime model](power-budget.md)
