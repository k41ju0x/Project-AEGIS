# AEG-002 — Compatibility Verification & Pre-Purchase Hold Points
**Reviewed:** 2026-10-26. **Status:** Desk review completed; hardware/electrical checks pending. **No parts purchased.**

## Check 1 — Li-ion battery connector and polarity
- RAK19007 documentation specifies **JST PHR-2 2mm female mating plug**, battery V+ and GND marked on the PCB; manufacturer says GND battery connector contact is toward board edge.
- Adafruit #353 is a protected 3.7V, 6600mAh battery pack with 2-pin JST-PH. **Physical connector similarity does not prove pin order.** Adafruit explicitly warns other makers may use opposite polarity.
- **Required validation before connecting:** Inspect PCB silk +/–, use a digital multimeter to identify which battery plug contact is positive (take care never to bridge contacts), and compare pins in the actual mating orientation. If reversed, obtain a professionally wired/correct-polarity adapter rather than forcing or improvising. Inspect pack for damage. Do not charge unattended.
- Status: **Electrical plausibility confirmed, polarity unverified — HOLD**.

Sources:
- https://www.adafruit.com/product/353
- https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/
- https://forum.rakwireless.com/t/battery-polarity-wisblock-starter-kit-rak4631-rak19007/11486

## Check 2 — Hammond enclosure mechanical fit
- Hammond 1554F2GYCL external 120 × 90 × ~60.5mm; drawing for 1554F gives **~112.91mm inside length, ~78.91mm inside width, ~54.50mm inside height**. Corner bosses, screw locations and gasket channel further limit mounting.
- RAK19007 footprint ~60 × 30mm; Adafruit pack **69 × 54 × 18mm**.
- Flat side-by-side across short dimension would require 30+54=84mm before spacing, so **not viable in that orientation**.
- **Potential solution:** Insulated stacked arrangement or alternate long-axis placement. Mechanical fit is not proven until CAD assembly/dry-fit considers OLED, GNSS, antennas, connector bend radius, standoffs, battery expansion clearance and charging access.
- Factory clear lid avoids a cutout for display; visibility and GPS reception require functional checks.
- Status: **Individual dimensions confirmed, assembled fit pending — CONDITIONAL**.

Sources:
- https://www.hammfg.com/part/1554F2GYCL
- https://www.hammfg.com/pdf/1554F.pdf
- https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen
- https://www.adafruit.com/product/353

## Check 3 — RF connectors and weather seal
- RAK Meshtastic starter kit lists **MHF-to-SMA cable** and a matching rubber LoRa antenna, along with BLE antenna. RAK4631's board-side LoRa RF antenna uses small MHF/I-PEX connection.
- Path: RAK4631 LoRa MHF port → kit-supplied MHF-to-SMA pigtail → enclosure SMA bulkhead → kit-supplied US915 antenna.
- **Remaining validation:** Exact SMA connector gender and mating type of the ordered variant, pigtail length, nut/washer/gasket and bulkhead mechanical drawing, needed hole diameter, cable bend radius and available sealed gland. A bare SMA bulkhead is not automatically waterproof. Verify kit antenna band and matching; don't transmit without antenna attached.
- Status: **Connector path documented; weatherproof feedthrough not verified — HOLD**.

Source: https://store.rakwireless.com/products/wisblock-meshtastic-starter-kit
Source: https://downloads.rakwireless.com/Meshtastic/Quick%20Start%20Guide_WisMesh%20RAK4631%20Starter%20Kit.pdf

## Purchase staging
1. Manufacturer-confirmed, standard: RAK4631/Rak19007, GNSS/OLED kit, verified radio band.
2. Candidate only: Adafruit #353 and Hammond 1554F2GYCL, pending battery polarity and dry-fit plan.
3. Do **not** select or drill waterproof antenna bulkhead until actual supplied connector part dimensions can be checked; do a bench prototype first.
4. Maintain 48h measured target / 24h verified fallback. No runtime claims without testing.
