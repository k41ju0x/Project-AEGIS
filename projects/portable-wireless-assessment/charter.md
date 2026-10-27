# AEG-005 — Portable Wireless Assessment Platform

**Status:** Concept / architecture selection
**Build strategy:** Entirely new hardware build (greenfield); do not assume reuse of old LattePanda or peripherals.

## Mission
Design and validate a modular, portable Kali Linux wireless security assessment workstation for authorized wireless discovery, GPS-correlated surveys, controlled WPA2/WPA3 lab security evaluation, and secure remote management.

## Historical reference
Owner's four-page *Remote Access Device Build* PDF documents an older LattePanda Delta V3, Alfa AC1900, GlobalSat BU-353S4, cellular connectivity, Kali Linux, Tailscale, GPSD and Kismet system. Use as inspiration, not as a current hardware BOM or validated installation guide.

## Candidate subsystems (not yet selected or purchased)
- Modern x86 SBC/mini-PC versus Raspberry Pi 5
- Linux-supported monitor-mode Wi-Fi interface (validate chipset and driver)
- GPS/GNSS + GPSD; Kismet and Wireshark
- Secure administration via Tailscale
- Optional cellular backhaul
- Portable power, thermal management, and rugged field-serviceable enclosure

## Design constraints and gates
- Work only on owned or explicitly authorized networks; protect collected SSIDs, BSSIDs, coordinates, and capture files.
- Document threat model and data handling, including local-only management by default.
- Compare architecture options for software compatibility, RF performance, power, thermals, size, cost, repairability.
- Verify driver and chipset support with current upstream documentation before ordering.
- Establish measurable acceptance tests and reproducible lab demos.
- Budget, size, runtime, display/interaction, and cellular requirements remain open decisions.

## Initial next milestone
Architecture trade study and requirements discovery; then draft BOM and build plan.
