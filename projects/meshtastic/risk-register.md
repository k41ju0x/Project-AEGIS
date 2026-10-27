# AEG-002 — Initial Risk Register
| ID | Risk | Potential impact | Prevention / mitigation | Verification |
|---|---|---|---|---|
| R-01 | Powering transmitter without suitable connected antenna | RF stage damage | Attach verified matched antenna before power-on/transmission | Pre-power visual checklist |
| R-02 | Wrong frequency SKU / regional configuration | Invalid operation / poor interoperability | Confirm local spectrum rules, hardware labeling, firmware region before test | SKU + setting record |
| R-03 | Incorrect LiPo polarity, charging or enclosure integration | Fire, battery damage | Use compatible protected battery/system, confirm connector polarity, manufacturer limits | Electrical inspection |
| R-04 | Publicly leaked channel key, private coordinates or serial identifiers | Loss of confidentiality / privacy | Secure private configs; sanitize screenshots and logs | Publication review |
| R-05 | Unrealistic range expectations | Failed success criteria | Test across known conditions, elevations and line of sight | Repeatable field plan |
| R-06 | Only one test node | No repeatable peer-to-peer validation | Plan second controlled peer or approved local counterpart | Two-way message evidence |
| R-07 | Incompatible peripherals / pinout | Damage / unreliable build | Verify exact board revision and manufacturer schematics | Design review before wiring |
