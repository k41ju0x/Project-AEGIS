# AEG-002 — Procurement Notes and Budget v1

**Status:** Price planning, not a purchase order. **Date:** 2026-10-26.

## Cost model for one rugged node
| Group | Allowance (USD) | Source quality |
|---|---:|---|
| RAK4631/RAK19007 Client-Tracker configured kit | $60.99 | Published RAKwireless **range upper variant price** ($24.99–$60.99), **not verified exact options checkout** |
| Compatible protected ~5000mAh 1S LiPo | $39 | Estimate |
| Gasketed enclosure | $39 | Estimate |
| Screen window/sealing | $23 | Estimate |
| RF feedthrough accessories | $24 | Estimate |
| USB/charging access seals | $22 | Estimate |
| Mounting and strain relief | $18 | Estimate |
| Consumables | $25 | Estimate |
| Shipping/tax/variation reserve | $35 | Estimate |
| **Planned total** | **$285.99** | **Mixed sourced price + engineering allowances** |

An **optional second test node** could add roughly **$60–$100+** depending on configuration; not included in the total. A second peer or approved existing reachable node is necessary for repeatable two-way message tests.

### Vendor source
RAKwireless [RAK4631 Meshtastic Starter Kit](https://store.rakwireless.com/products/wisblock-meshtastic-starter-kit): variant pricing listed $24.99–$60.99. Its **Client-Tracker** option bundles a RAK12501 GNSS, RAK1904 acceleration sensor and RAK1921 OLED. Select **RAK19007 base**, **US915 radio**, and confirm display assembly, exact kit contents and final checkout price. The published kit includes antenna and RF lead, so don't pay twice for them unless sealing/connector requirements necessitate changes.

### Procurement gates
- [ ] Screenshot/record exact vendor option values and completed checkout *before payment*
- [ ] Confirm 915 MHz correct region, Arduino-bootloader variant
- [ ] Confirm charger and LiPo connector polarity, dimensions, temperature and protection
- [ ] Dry-fit enclosure against vendor CAD / actual parts
- [ ] Confirm weather-sealed screen, antenna and charging access design
- [ ] Select controlled second test peer
- [ ] Reconcile expected cost vs actual paid total; retain receipts privately

Do not copy purchase addresses, order numbers or serial numbers to this public repository.
