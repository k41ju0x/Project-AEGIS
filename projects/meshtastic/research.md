# AEG-002 — Hardware Research Journal
**Research date:** 2026-10-26  
**Research status:** Shortlist, not a purchase decision.

## Candidate A — RAK WisBlock RAK4631 (nRF52840 / SX1262)
- Meshtastic documents a modular WisBlock ecosystem with starter kits, optional GNSS, display and sensors.
- Core uses BLE-capable nRF52840 and SX1262; listed frequency options include 915 MHz. Select correct regional SKU and compatible base, battery connectors and antenna.
- Must distinguish the RAK4631 Arduino-bootloader version from RAK4631-R with RUI3 bootloader; Meshtastic notes conversion may be necessary.
- Good shortlist candidate for a lower-power modular portable build. No endurance number assumed.

**Sources:**  
https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/  
https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/core-module/?rakcore=RAK4631

## Candidate B — LILYGO T-Echo (nRF52840)
- Appears on Meshtastic's official supported-device flasher list.
- Evaluate actual US-band SKU, integrated features, battery replaceability, enclosure adaptability, availability and cost before comparing with RAK.
**Source:** https://flasher.meshtastic.org/

## Candidate C — Other supported compact boards
- Heltec and other boards appear among the officially supported device families, but model/revision, chipset, radio variant and power requirements vary.
- Do not pick based on brand name without validating exact model and board revision.
**Source:** https://flasher.meshtastic.org/

## Decision matrix (complete after budget/form factor are confirmed)
| Criterion | Weight | RAK4631 WisBlock | T-Echo | Other |
|---|---|---|---|---|
| Battery efficiency | High | Candidate | Candidate | Unknown |
| Expandable GPS/display | Medium | Modular | Check SKU | Check exact board |
| Field enclosure compatibility | High | Check case | Check case | Check case |
| Cost and availability | High | Quote needed | Quote needed | Quote needed |
| Flashing/documentation | High | Officially documented | Officially supported | Varies |
| Regional RF variant | Mandatory | Verify US SKU | Verify US SKU | Verify US SKU |

## Firmware notes
Official guidance warns against powering/transmitting without the antenna attached. A USB *data* cable is required for many flashing methods. Follow firmware instructions for the exact platform and record the installed firmware version.
https://meshtastic.org/docs/getting-started/
https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/

## Evidence gaps
No retailer pricing, battery tests, regional regulatory review for a specific purchase, or antenna match verified yet. These must be completed before procurement.
