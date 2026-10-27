# AEG-002 — Procurement Plan v2
**Status:** Candidate parts selected, **NOT PURCHASED**.

## Preferred battery and housing
- **Battery:** [Adafruit #353 3.7V protected 6600mAh Li-ion pack](https://www.adafruit.com/product/353): **$24.50** listed; 69 × 54 × 18mm; JST-PH-2; rated charge current up to 1.65A by pack maker, **but RAK19007 charges far slower**.
- **Enclosure:** [Hammond 1554F2GYCL](https://hammond-store.com/electronics/small-case/plastic/1554): **$13.83** listed; clear-lid gasketed polycarbonate, **120 × 90 × 60mm external**. This is an evaluation selection, not a verified internal fit.
- **Core:** [RAKwireless Meshtastic Starter Kit](https://store.rakwireless.com/products/wisblock-meshtastic-starter-kit): **$24.99–$60.99 variants**, use $60.99 as conservative placeholder; choose RAK19007, US915 and Client-Tracker, confirm RAK12501 GNSS + RAK1921 OLED included.

## Budget, one node
| Component | USD | Basis |
|---|---:|---|
| RAK configured kit placeholder | $60.99 | Vendor published variant ceiling, precise checkout unverified |
| Adafruit 6600mAh battery | $24.50 | Listed price |
| Hammond clear-lid enclosure | $13.83 | Listed price |
| Waterproof RF bulkhead/interface | $25.00 | Estimate |
| Nonconductive mounts and pack restraints | $20.00 | Estimate |
| Insulation/padding and strain relief | $10.00 | Estimate |
| Charging access contingency | $20.00 | Estimate; may not be spent |
| Shipping/tax/rework reserve | $35.00 | Estimate |
| **Total budget allowance** | **$209.32** | **Not a final checkout quote** |

Does not include a second owned Meshtastic node or specialist test instruments. Budget remains under the user's open-ended $250+ preferred funding band, leaving reserve for a test peer, environmental testing, or alternate components.

## Mechanical & electrical considerations
1. Use the **clear lid** as the OLED viewing window; no separate window cutout required. Readability, GNSS reception through plastic and board/display orientation require bench tests.
2. Fit 69×54×18mm battery plus RAK19007 30×60mm baseboard and cable loops with supports; **external dimensions are not usable internal dimensions**. A stacked mount may be needed; preserve clearance from screws.
3. Avoid exposed USB penetration in v1. Open lid in a dry indoor environment for charging, then reseat gasket and screws before field use. This is less convenient but removes a common leak path.
4. Any antenna hole requires an accurately matched watertight bulkhead/feedthrough. Verify antenna connector type and rubber seal.
5. Check pack voltage, JST connector pin order and polarity using official schematics and multimeter. A physically fitting JST can have reversed polarity.
6. RAK19007 low charge-current limit makes full recharge potentially **20+ hours**; verify actual charge behavior and ventilation.
7. Modified enclosure's published IP68 rating is **not a certified finished-device rating**. Test assembled enclosure for realistic splashes/rain before use; no intentional submersion claim.

## Do not purchase until
- [ ] Verify exact variant cart and delivered module assembly/pinout
- [ ] Download/check Hammond interior dimensions and mounting drawing
- [ ] Confirm battery-to-base polarity without relying on matching connector
- [ ] Confirm SMA/pigtail/feedthrough mating interfaces and mechanical layout
- [ ] Verify safe indoor charging access and external antenna waterproofing
- [ ] Decide whether a second peer is needed for testing

Sources: https://www.adafruit.com/product/353 ; https://hammond-store.com/electronics/small-case/plastic/1554 ; https://store.rakwireless.com/products/wisblock-meshtastic-starter-kit
