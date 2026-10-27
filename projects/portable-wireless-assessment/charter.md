# AEG-005 — Portable Wireless Assessment Platform

**Status:** Concept / architecture selection
**Build strategy:** Entirely new hardware build (greenfield); do not assume reuse of old LattePanda or peripherals.
**Selected architecture:** Headless LattePanda x86 computer, remotely administered from a laptop/phone. Exact model pending selection.
**Design priority:** Maximum sustained compute performance over portability, battery runtime, weight, and cost.
**Enclosure direction:** Rugged Pelican-style protective case; user accepts active fans and larger form factor. Exact model and ingress-protection strategy TBD.
**Power requirement:** Both wall-powered and standalone battery-powered operation. Full sustained performance on AC; target full performance on battery subject to measured load and safe battery design.
**Battery endurance target:** 8 hours at a documented active assessment workload; support an externally attachable backup battery/power bank for additional runtime, subject to verified voltage, current, continuous wattage and power-path compatibility.

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
- Sustained-load thermal management with active cooling and measured throttling. For Pelican-style cases, explicitly distinguish sealed transport protection from powered operation: fan openings defeat the original case ingress rating unless separately engineered and validated.
- Investigate ducted intake/exhaust with filtered vents versus a sealed conduction-cooled enclosure. Include temperature sensors, dust/water protection, and service access.
- Dedicated monitor-mode wireless adapter; separate reliable management interface.
- Dual-input AC adapter and field battery architecture, with properly rated regulation, BMS, fuses and thermal protection. Investigate uninterrupted switchover only after selecting board input specifications; do not assume simple parallel wiring is safe.
- Size onboard battery for an **8-hour mission target** using measured complete-system average power, including radios, storage and fans. Illustrative nominal Wh = average W × 8 / 0.85; 60 W average implies ~565 Wh nominal under this assumption, not a validated BOM.
- Provide a protected, accessible external backup-power input. Validate power bank or station output ratings, cable/connectors, electrical isolation and safe transfer before purchase; a generic USB power bank may not support the selected LattePanda.
- Avoid committing to chemistry, charger or enclosure placement before thermal and electrical design.
- Benchmark CPU, memory, storage throughput, multi-adapter capture stability and power consumption before enclosure finalization.

## Initial next milestone
Architecture trade study and requirements discovery; then draft BOM and build plan.
