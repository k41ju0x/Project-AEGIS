# AEG-002 — Rugged Architecture v2

## Selected
RAK4631 nRF52840 / SX1262 on RAK19007 baseboard, US915 hardware, RAK12501 GNSS, RAK1921 OLED, BLE to phone, and appropriately matched 915MHz antenna.

## Enclosure and battery candidates
- **Hammond 1554F2GYCL** clear lid polycarbonate gasketed enclosure, **120 × 90 × 60mm external**, $13.83 listed.
- **Adafruit #353** protected **3.7V 6600mAh** parallel-cell pack, **69 × 54 × 18mm**, 155g, $24.50 listed.
- **RAK19007** board nominal **30 × 60mm**. Confirm *usable interior* case dimensions, standoff locations, GPS antenna orientation, and cable paths. Stack on electrically insulated mounts if necessary.
- OLED visible through factory clear lid eliminates an additional cutout. No exposed USB hole in version 1. Open gasketed lid indoors to charge; reseal before outdoor use.
- Only intentional case penetration: properly gasketed external 915MHz antenna feedthrough matched to the kit's supplied RF lead (confirm interface, don't assume SMA vs RP-SMA).
- GNSS antenna and BLE must operate through nonmetallic housing; verify actual reception and no excessive RF attenuation.

## Cross-sectional concept (not to scale)
```
  CLEAR LID / FACTORY GASKET  <-- no OLED window cut
  -------------------------------------------
  OLED + RAK4631/RAK19007 on insulated mount
  -------------------- clearance / standoffs
  Protected 6600 mAh pack restrained in cradle
  -------------------------------------------
  Hammond 1554F polycarbonate base
  (sealed antenna bulkhead on side)
```

## Engineering hold points
1. Confirm battery connector **polarity** by measurement; matching JST shape is insufficient.
2. Verify pack protection, nominal voltage and permitted charge current; RAK19007 charging is approximately 350mA and may take 20+ hours.
3. Download enclosure CAD drawing: exterior dimensions alone cannot prove fit.
4. Verify battery secure mounting (avoid crushing/puncture); check USB access after dry fitting.
5. Test GNSS, OLED, BLE and LoRa functionality with enclosure assembled.
6. Original enclosure rating is not automatically preserved after drilling; validate weather resistance of complete build.

## Runtime criterion
48h preferred; 24h accepted fallback only with documented representative workload and measurements. See [power budget](power-budget.md) and [procurement](procurement.md).
