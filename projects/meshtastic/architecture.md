# AEG-002 — Rugged RAK4631 Architecture v1.0
**Decision:** RAK4631 on RAK19007, US915 radio variant, with GNSS + OLED. **State:** Proposed integration pending fit/electrical tests.

```text
                    ┌──────────────── Rugged gasketed case ────────────────┐
Antenna US915 ─SMA──┤ sealed bulkhead ─ RF pigtail ─ SX1262 / RAK4631      │
                    │                                  │                    │
Phone ─── BLE ──────┤                             nRF52840                 │
                    │                                  │                    │
                    │                      RAK19007 baseboard              │
                    │                         │           │                │
                    │                  RAK12501 GNSS   RAK1921 OLED        │
                    │                         │           │                │
                    │               GPS antenna      gasketed window      │
                    │                         │                            │
                    │  protected 1S LiPo ─ charge circuitry ─ USB-C       │
                    └──────────────────────────────────────────────────────┘
```

## Connections and role
- **RAK4631:** nRF52840 + SX1262; 915 MHz hardware variant; *Arduino bootloader*, not the stock RAK4631-R RUI3.
- **RAK19007:** 30×60 mm baseboard with slots for sensor expansion, LiPo connector/charging and USB-C.
- **GNSS:** RAK12501 in vendor-supported sensor slot, with GPS antenna carefully located under a suitable nonmetallic cover.
- **Display:** RAK1921 0.96-inch 128×64 I2C OLED; vendor documents soldering and pin-order precautions. Use status screen; phone is text-entry interface.
- **RF:** Included matching US-band antenna and MHF/U.FL-to-SMA lead only if bundled with chosen variant. Additional waterproof gland/bulkhead may be required.
- **Power:** One protected compatible 1S LiPo (working design assumption 5,000 mAh), polarity checked before connection; evaluate onboard charge rate and thermal requirements.
- **Enclosure:** Commercial gasketed weather-resistant plastic case with mounts, separate screened window, strain-relieved RF bulkhead, and deliberate sealed charging-access strategy. Any modification invalidates automatic claims based on an empty enclosure's IP rating.

## Integration review checklist
- [ ] Record full vendor kit name, chosen radio band, baseboard and bundled modules
- [ ] Verify LiPo voltage, connector polarity, protection, dimensions and charging limits
- [ ] Confirm GPS module and display fit without slot/pin interference
- [ ] Confirm screen-viewing cutout sealing design
- [ ] Confirm antenna gland/bulkhead seals and orientation
- [ ] Confirm access for USB flashing / charging without exposed ports
- [ ] Confirm GNSS antenna visibility, LoRa antenna clearance and BLE coverage
- [ ] Bench-build and validate *before* installing into closed enclosure

Sources: https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/core-module/?rakcore=RAK4631 ; https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/screens/?rakscreens=OLED ; https://store.rakwireless.com/products/wisblock-meshtastic-starter-kit
