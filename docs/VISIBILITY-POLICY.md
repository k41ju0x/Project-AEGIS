# Hybrid Visibility & Publication Policy

**Default:** This public Project Aegis repository contains safe summaries, learning notes, and links. Sensitive implementation belongs in a separate **private** repository or appropriate secure storage.

## Generally suitable for public
- Sanitized project goals, components, generic architecture diagrams and design rationale.
- Public-source research and links, reproducible laboratory-only test methods.
- Aggregate testing results after review, with secret and location metadata removed.
- Lessons learned and non-sensitive build photos.

## Keep private or secure separately
- Passwords, tokens, signing keys, Meshtastic private channels/keys, cloud secrets.
- Exact private network inventories, management interfaces, VPN configs or diagrams exposing attack paths.
- Unique device identifiers, personal coordinates, unredacted PCAPs, logs with personal data.
- Confidential reports, non-public vulnerabilities, third-party data or proprietary binaries.
- Operational access paths for remote administration devices.

## Publication gate
Before committing, review the diff; scan for secrets; check filenames, EXIF location metadata, serial numbers, IPs, screenshots and embedded comments. Publish only what you have rights to share. Never assume `.gitignore` protects files already committed.

If exposed, revoke/rotate secrets immediately, restrict access, and remediate the repository history as necessary. Deleting a later commit alone does not remove earlier history.

## Project-level choice
Every project README identifies `Visibility: Public summary / Private implementation / Both`, with a link to any **publicly safe** repo only. A private repository URL can be omitted from public files.

## Research authorization
Security experimentation must use owned systems or systems covered by explicit authorization and approved scope. Record authorization and sensitive boundaries privately where necessary.
