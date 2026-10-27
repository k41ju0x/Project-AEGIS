# AEG-002 — Runtime Model v2 (6600mAh)
**Design decision:** Prefer 48 hours; **minimum acceptable fallback 24 hours** based on user direction. Both require measured validation.

## Candidate pack
Adafruit 353 protected **3.7 V, 6600mAh**, 69 × 54 × 18 mm / 155g, JST-PH-2 connector. **The connector shape does NOT guarantee polarity compatibility** with RAK19007; verify using a multimeter against vendor pinout **before connection**.

https://www.adafruit.com/product/353

## Preliminary math (not measured)
Assume usable battery charge = 80% of 6600mAh = **5280mAh** (arbitrary engineering reserve, not vendor derating).
- 48h target: max average draw **110 mA**.
- 24h fallback: max average draw **220 mA**.

| Average current | Hypothetical duration at 5280mAh usable |
|---:|---:|
| 35mA | 151h |
| 50mA | 106h |
| 80mA | 66h |
| 100mA | 53h |
| 110mA | 48h |
| 150mA | 35h |
| 220mA | 24h |

Measured averages depend on GNSS acquisition, OLED usage, BLE, LoRa airtime, regulator losses, temperature and battery age. No vendor claim of 48h endurance.

## Charging consideration
RAK19007 charge-current limit is reported approximately **350mA**. A nominal 6600/350 = **18.9 hours minimum ideal constant-current**; real charging generally takes longer as current tapers and system loads draw power. Verify charger revision/spec and pack manufacturer's charging limits; avoid charging an unattended prototype or in excessive temperature.

## Acceptance
Test for 48h with representative GNSS + OLED settings. If it fails, quantify runtime under identical conditions; 24h can be accepted as **approved fallback**, with evidence and a recorded deviation. Do not change the requirements silently. Measure battery voltage and observe device performance at intervals.
References:
- https://www.adafruit.com/product/353
- https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen
