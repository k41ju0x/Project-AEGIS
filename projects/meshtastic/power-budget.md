# AEG-002 — Battery Runtime Model v1

**Target:** At least 48 hours of operation with Meshtastic, GPS and local display enabled in a documented representative duty cycle.

## Capacity model
Proposed nominal battery capacity: **5000 mAh**, *not yet sourced, tested or validated*. Applying a provisional 80% usable fraction for losses/operating reserve gives:
- usable charge allowance: 5000 × 0.8 = **4000 mAh**
- maximum allowable average device current over 48 hours: **4000 / 48 ≈ 83.3 mA**

This is a **planning ceiling**, not measured draw. The usable fraction is an assumption and will depend on discharge limits, age, temperature, regulator efficiency, cell quality and usage.

## Sensitivity to measured average device current
| Measured average draw | Hypothetical runtime at 4000 mAh usable |
|---|---|
| 20 mA | 200 h |
| 35 mA | 114 h |
| 50 mA | 80 h |
| 70 mA | 57 h |
| 83 mA | 48 h |
| 100 mA | 40 h |
| 125 mA | 32 h |

## Loads to quantify
- nRF52840/SX1262 idle/receive/transmit state and actual packet traffic
- GNSS acquisition vs periodic tracking modes
- RAK1921 OLED active brightness and sleep/timeout
- BLE active vs disconnected
- Power regulators and charging circuitry, battery temperature

## Acceptance test
1. Use safe vendor-compatible battery and instrumentation, record pack capacity and charging history.
2. Fix firmware, radio settings, GPS tracking interval, screen brightness/timeout, BLE state and traffic profile.
3. Fully charge according to pack/baseboard instructions, then run untethered for >=48h.
4. Record message success and GPS/display function through the test; report cutoff behavior and measured usable capacity.
5. Retest if firmware, GNSS interval, enclosure or battery changes meaningfully.

**If under target:** Measure which subsystem dominates draw and revise display/GNSS duty cycle, battery capacity, or enclosure constraints—do not simply declare the goal met.

Reference: https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/base-board/
