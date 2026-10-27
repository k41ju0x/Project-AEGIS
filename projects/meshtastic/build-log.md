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
