# AEG-005 — Portable Wireless Assessment Platform

**Status:** Concept / architecture selection
**Build strategy:** Entirely new hardware build (greenfield); do not assume reuse of old LattePanda or peripherals.
**Selected architecture:** Headless LattePanda x86 computer, remotely administered from a laptop/phone. Exact model pending selection.
**Design priority:** Maximum sustained compute performance over portability, battery runtime, weight, and cost.

## Mission
Design and validate a modular, portable Kali Linux wireless security assessment workstation for authorized wireless discovery, GPS-correlated surveys, controlled WPA2/WPA3 lab security evaluation, and secure remote management.

## Historical reference
Owner's four-page *Remote Access Device Build* PDF documents an older LattePanda Delta V3, Alfa AC1900, GlobalSat BU-353S4, cellular connectivity, Kali Linux, Tailscale, GPSD and Kismet system. Use as inspiration, not as a current hardware BOM or validated installation guide.

## Candidate subsystems (not yet selected or purchased)
- **LattePanda x86 SBC (selected platform family)**; evaluate current models for performance, Kali compatibility, power draw, cooling and expansion
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
- Headless operation selected: no integrated display or keyboard required. Management via secure local link and/or Tailscale.
- Separate management network/interface from assessment Wi-Fi interface.
- Budget, size, runtime, and cellular requirements remain open decisions.

## Performance-first design criteria
- Prefer highest practical LattePanda CPU class and 32GB+ RAM when offered; validate actual model specifications before purchase.
- Fast NVMe storage sized for PCAP/Kismet data; separate archival and retention policies.
- Sustained-load thermal management with active cooling and measured throttling.
- Dedicated monitor-mode wireless adapter; separate reliable management interface.
- Robust DC power supply, with portable battery architecture designed after load measurements.
- Benchmark CPU, memory, storage throughput, multi-adapter capture stability and power consumption before enclosure finalization.

## Initial next milestone
Architecture trade study and requirements discovery; then draft BOM and build plan.
