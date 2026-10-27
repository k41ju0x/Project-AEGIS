# Publication and Research Safety

Project Aegis uses a **hybrid portfolio**: public documentation and sanitized design summaries belong here; sensitive implementation details belong in access-controlled repositories or encrypted offline storage.

Do **not** commit passwords, API keys, private encryption keys, tokens, personal identifiers, detailed private network inventory, VPN configs, access credentials, sensitive diagrams, or confidential third-party data.

All security testing must be performed on owned systems or with explicit authorization. Review screenshots, logs, packet captures, and configuration files before publishing. Git history preserves deleted content; if a secret is committed, revoke/rotate it and address history appropriately.
