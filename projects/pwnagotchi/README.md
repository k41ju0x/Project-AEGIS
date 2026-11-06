# AEG-003 — Pwnagotchi

**Status:** Active build (2026-11-06); hardware received; SD image preparation next

## Purpose
Document an authorized wireless security research hardware project.

## Next action
User resumed AEG-003 on 2026-11-06. Prepare a dedicated microSD using the community 64-bit image for Raspberry Pi Zero 2 W, then verify display and PiSugar 3 in stages.

## Hardware and procurement — 2026-11-01
- Ordered: dedicated Raspberry Pi Zero 2 W with pre-soldered GPIO header; PiSugar 3 1200mAh battery.
- Already owned: Waveshare 2.13-inch e-Paper HAT V4.
- Enclosure: custom 3D print after bench assembly and measurements; no enclosure ordered.
- Confirm separate microSD card and compatible charging/data cable at inventory.
- Intended use: authorized Wi-Fi research in owned/approved test environments.

## Arrival and bench-test plan
1. Inventory and photograph components; verify revisions and GPIO/battery mechanical fit.
2. Prepare supported community Pwnagotchi OS image on microSD; enable secure management access.
3. Test e-paper display and battery monitoring before enclosure design.
4. Measure stacked assembly for 3D-printed case; document build and results.

## Delivery log — 2026-11-06
User reports arrival of the second Raspberry Pi Zero 2 W and second PiSugar battery. Existing Waveshare 2.13-inch e-Paper HAT V4 is in inventory. Label and store parts; no assembly, flashing, or development until explicitly resumed. Verify exact battery model during inventory.

## Build session 1 — 2026-11-06
- User confirmed two PiSugar 3 1200mAh batteries received; one allocated to AEG-003.
- Priority changed: Pwnagotchi active; Sentinel deferred.
- Hardware: Pi Zero 2 W with soldered header, Waveshare 2.13-inch V4, PiSugar 3.
- Software selection: jayofelony Pwnagotchi 64-bit Raspberry Pi Zero 2 W image; source https://github.com/jayofelony/pwnagotchi/releases. PiSugar reference https://docs.pisugar.com/docs/product-wiki/pwnagotchi/intro.
- Next: verify microSD and host OS; download and flash verified image; no boot or hardware testing completed yet.
