# AEG-009 — v0.1 Acceptance Tests

**Status:** Planned; none executed on the user's Kali VM yet.

| Test | Required result |
|---|---|
| Port parsing | Accept valid lists/ranges; sort/deduplicate; reject zero, >65535, reversed ranges and malformed input |
| Target scope | Invalid address or target/allow-target mismatch fails before any socket call |
| Numeric settings | Reject nonpositive, NaN, infinite and excessive rates; reject invalid timeouts |
| Open port | A loopback listener is reported open |
| Closed port | Explicit refusal is reported closed |
| Timeout/error | Injected timeout and unreachable errors remain distinct from closed |
| Rate limit | Fake-clock unit test proves attempt start spacing is at least 1/rate |
| Socket cleanup | All success and failure paths close sockets |
| Output | JSON/CSV agree; unique directories preserve earlier runs |
| Interruption | Partial results are explicitly marked and exit status is 130 |
| Nmap comparison | Same local address/ports tested under same listener state; differences explained |
| Defensive observation | Optional loopback capture demonstrates full TCP connections; capture remains local |

Record OS, Python/Nmap versions, commands, observed outcomes and date before marking PASS. Mocked tests validate error handling, not real network timeout behavior. External testing is outside the initial acceptance run.
