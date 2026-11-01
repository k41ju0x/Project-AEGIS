# AEG-016 — AEGIS Sentinel

**Status:** Ready for Purchase (in cart; checkout not yet confirmed)
**Battery decision (confirmed 2026-11-01):** Desktop UPS + portable operation required. Select PiSugar 3 1200mAh as preferred battery, pending shared-I2C and Whisplay electrical/mechanical bench validation. Desktop external charging via PiSugar; software battery telemetry and safe shutdown. Do not assume uninterrupted upstream desktop AI/network access during outages. Estimated runtime to be measured with LCD/audio/Wi-Fi workloads. No battery ordered yet.
**Controller decision (confirmed 2026-11-01):** Raspberry Pi Zero 2 W, preferably with pre-soldered 40-pin GPIO header. Remote AI inference on existing Windows desktop; no dedicated Pi 5 purchase for Sentinel.
**Track:** AI, Embedded Systems, Home Automation, Cybersecurity Research
**Concept:** Futuristic desktop AI companion and Project AEGIS voice command center.

## Vision
A compact desktop AI companion with a hybrid personality: warm, expressive, and conversational in everyday use; concise, evidence-driven and tactical during Project AEGIS and security operations. Visual concept v1.0: dark graphite angular 3D-printable enclosure, cyan expressive animated eyes, AEGIS green tactical status lighting, serviceable modular base. Concept art is illustrative and not dimensionally accurate.

## Five modules
1. **Companion:** animated expressions, push-to-talk, speech-to-text, text-to-speech, conversational context.
2. **AEGIS command center:** read GitHub project status and authenticated TCT service health.
3. **Meshtastic:** status, incoming message announcements and confirmed outbound voice-to-text messages via AEG-006 Tactical Control Terminal.
4. **Home Assistant:** approved home-device control and sensor monitoring; restrict security-sensitive actions.
5. **APEX assistant:** analyze lab outputs and support authorized security research; require explicit approval for active tools.

## Hardware baseline (pending bench validation)
- PiSugar Whisplay HAT: 1.69-inch 240x280 LCD, dual microphones, mono speaker, RGB LEDs, programmable button, 40-pin GPIO.
- **Dedicated Raspberry Pi Zero 2 W with populated 40-pin header** as compact display/audio endpoint; remote AI inference on existing Windows desktop or a configured cloud endpoint. Dedicated Pi 5 is not part of the selected baseline; reconsider only if measured requirements justify it.
- PiSugar 3 1200mAh UPS (preferred; 5V/2.5A maximum output, I2C 0x57/0x68), USB-C charging and battery telemetry; confirm no conflict with Whisplay codec and power draw.
- microSD card, suitable 5V supply, USB cable, standoffs/headers as required.
- Custom enclosure **only after physical measurement**; maintain acoustic openings, ventilation, button access, and physical microphone-disable provision.
- Existing AEG-006 Pi 5 is a separate project and must not be dismantled or repurposed.

## Purchase gates
- Phase A: Whisplay HAT, dedicated Pi Zero 2 W **with 40-pin header**, PiSugar 3 1200mAh UPS, microSD and power supply if not already owned. Confirm actual stock, shipping, board/header compatibility, and codec revision.
- Phase B: verify LCD, dual mic capture, speaker, LED and button on current Raspberry Pi OS and PiSugar driver; then implement local animated face and push-to-talk.
- Phase C: measure board assembly, select 3D-print material and enclosure, add secure service integrations.
- No purchases have been placed by this GitHub registration.

## Acceptance criteria
- Boots headless and auto-starts UI.
- Clearly indicates mic-active state; default push-to-talk and a real mic-disable method.
- Correctly animates listening/thinking/speaking/tactical/alert expressions on physical 240x280 display.
- Conversational mode can connect to approved inference endpoint with timeout/failure handling.
- AEGIS status checks use read-only scoped credentials initially.
- Meshtastic transmissions, home security controls, and APEX tool execution require confirmation.
- Logs and secrets are stored securely; private conversations not committed to GitHub.

## Roadmap
M0 concept and scope; M1 hardware procurement and inventory; M2 Whisplay driver and audio/display validation; M3 animated personality and speech; M4 AEGIS/Mesh/Home/APEX integration; M5 enclosure and documented testing.

## Sources
- https://docs.pisugar.com/docs/product-wiki/whisplay/overview
- https://github.com/PiSugar/Whisplay
- https://www.pisugar.com/products/whisplay-hat-for-pi-zero-2w-audio-display
