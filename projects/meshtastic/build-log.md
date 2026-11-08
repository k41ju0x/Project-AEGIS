# AEG-002 — Build Log

## 2026-10-26 — Battery and enclosure candidates selected
**Goal:** Support rugged enclosure and 48h endurance, with 24h verified fallback.

**Research:** Hammond 1554F2GYCL clear-lid 120×90×60mm IP-rated empty enclosure ($13.83 listed) and Adafruit #353 protected 3.7V 6600mAh pack, 69×54×18mm ($24.50 listed). No custom OLED window needed.

**Why:** Clear lid minimizes seal penetrations; protected higher-capacity pack gives 110mA theoretical average-current allowance over 48h assuming 80% usability (220mA for 24h).

**Unknown:** Battery pack polarity vs RAK19007, interior usable dimensions, radio antenna bulkhead match, exact RAK configured kit cost and actual system current/charge time.

**Observed:** Documentation only. No hardware procured or tested. Case manufacturer's empty-box rating does not certify modified build.

**Next:** Verify vendor cart, pinout and CAD interior before ordering.

## 2026-10-26 — RAK4631 architecture selected
Requirements captured: rugged, GPS, screen, 48h preferred, open-ended $250+ budget; RAK4631 and RAK19007 platform accepted.

## 2026-10-26 — Planning baseline
Established initial charter, risks, research shortlist and tests.

## 2026-10-29 — RAK4631 starter kit ordered
I ordered one WisBlock RAK4631/RAK19007 starter kit with US915 hardware selection, OLED, RAK12501 GNSS and RAK1904 sensor configuration. Recorded checkout price: $56.30 before import fees and 14–20-day shipping estimate. Physical receipt, actual included parts and functional test **not yet verified**. Previous 'no hardware procured' statements above describe the earlier October 26 planning state only.

**Next:** Inventory on arrival; photograph actual parts; confirm correct antenna, region and safe connection before powering or flashing.
