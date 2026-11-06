# AEG-003 — Pwnagotchi

**Status:** Active build; battery-powered boot and telemetry verified (2026-11-06); endurance/enclosure pending

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

## Build session 1 — firmware selection
- Firmware asset validated: `pwnagotchi-64bit-2.9.5.8.img.xz` from jayofelony release `v2.9.5.8` (published 2026-08-18).
- Download: https://github.com/jayofelony/pwnagotchi/releases/download/v2.9.5.8/pwnagotchi-64bit-2.9.5.8.img.xz
- Host: Windows 11; Raspberry Pi Imager installed.
- Next: flash 32GB SanDisk microSD with custom image and verify write; flashing not yet reported complete.

## First successful display boot — 2026-11-06
- Photo evidence supplied by user: Raspberry Pi Zero 2 W powered via USB, Waveshare 2.13-inch V4 showing Pwnagotchi face and `aegis-pwn` identity.
- On-screen readings: `CH 00`, `APS 0 (00)`, `BAT 0%`, `UP 00:00:00`, `AUTO`; initial startup readings, not yet independently validated.
- Verified: image boots sufficiently to render display and custom identity. USB Ethernet management and Wi-Fi behavior not verified.
- PiSugar 3 not installed yet; battery telemetry not tested. Before wireless operation, verify passive settings and authorized-lab scope. Next milestone: USB management access and PiSugar hardware fit/telemetry.

## Battery power and telemetry verified — 2026-11-06
- Hardware stack: Raspberry Pi Zero 2 W, Waveshare 2.13-inch V4 e-paper HAT, PiSugar 3 1200mAh UPS.
- PiSugar 3 boot procedure: short press then long press; the Pi booted without USB attached.
- Pwnagotchi displayed battery state of charge **52%**; confirms initial software battery telemetry and battery-powered boot.
- Previously validated: functional Pwnagotchi display, updating uptime and application status, USB RNDIS network and SSH (working interface addresses verified; site-specific addresses intentionally omitted from public documentation).
- Remaining: measure endurance, verify graceful shutdown/low-battery behavior, inspect enclosure dimensions and design 3D-printable case.

## Network documentation policy
USB RNDIS management uses two compatible static IPv4 addresses on a dedicated point-to-point subnet. The exact addressing is environment-specific and should be kept in private operational notes. Example only: Windows `10.0.0.1/24`, Pi `10.0.0.2/24` (not the addresses validated in this build). Do not publish Wi-Fi credentials, SSH private keys, or sensitive capture files.
