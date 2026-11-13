# AEG-009 — v0.1 Requirements

## Platform and architecture decision
Use Python 3 and its standard library on the existing Kali VM. Keep executable source in a separate repository when implementation begins; this hub holds planning and sanitized evidence. No AI dependency, database, web dashboard or new hardware is needed.

Proposed modules: CLI → scope and port validation → sequential TCP probe engine → result model → JSON/CSV/summary writers. Separate the engine from the CLI so network behavior can be tested independently.

## Required behavior
- Accept exactly one literal IPv4 address; reject hostnames, CIDR ranges and IPv6 in v0.1 to avoid ambiguous DNS resolution and implicit target expansion.
- Require an explicit allowed-target value matching the scan target before opening sockets. This records operator scope; it is not proof of authorization.
- Accept explicit ports and inclusive ranges from 1–65535; deduplicate and sort. Reject malformed, reversed and out-of-range inputs before networking.
- Default timeout: 1 second. Default maximum start rate: 10 connection attempts/second. Both must be positive finite values; cap the initial implementation at 100 attempts/second.
- Use sequential TCP connects, not raw packets. Close every socket. Do not send application payloads.
- Classify successful connections as open, explicit connection refusal as closed, timeouts as timeout, and other network failures as error. A timeout is not proof of filtering or a closed port.
- Measure durations using a monotonic clock; record UTC run timestamps separately.
- Handle Ctrl+C with a clearly marked partial result and exit status 130. Configuration errors must return nonzero without scanning.
- Create a unique run directory; never overwrite a previous run. Store target, requested ports, settings, tool version, timestamps, per-port outcome and error details in JSON; equivalent rows in CSV; concise human summary.
- No root privileges required for the scanner.

## Proposed CLI contract — not implemented yet
```text
aegis-recon tcp --target 127.0.0.1 --allow-target 127.0.0.1 --ports 8765,8766 --timeout 1 --rate 10 --output runs
```

## Definition of v0.1 acceptance
Local automated tests pass; the user independently reproduces localhost results in Kali; JSON and CSV agree; Nmap comparison and limitations are recorded. Publication of a plan or code alone does not satisfy acceptance.

## Later milestones
v0.2: DNS enumeration for explicitly scoped owned zones.
v0.3: optional Nmap adapter with argument-array subprocess calls and recorded tool versions.
v0.4: reporting and repeat-run comparison.

These are proposed milestones, not completion claims. Generated network telemetry and defensive observations remain part of the wider project acceptance.
