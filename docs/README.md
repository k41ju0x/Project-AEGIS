# Project Aegis Documentation Handbook

**Purpose:** Establish a repeatable, lightweight engineering record for any research, software, RF, hardware, home lab, or cybersecurity project.

## Start here
1. Register the idea with the **next unused stable ID** in [PROJECTS.md](../PROJECTS.md) (currently AEG-021). Numbering alone doesn't authorize building or purchasing hardware.
2. Keep parked concepts in [FUTURE-IDEAS.md](../FUTURE-IDEAS.md). Create a GitHub issue or add a card to the [R&D tracking board](https://github.com/users/k41ju0x/projects/3/views/1) **only when planning or execution is approved**.
3. Create `projects/<slug>/README.md` from [PROJECT-TEMPLATE.md](../templates/PROJECT-TEMPLATE.md) when ready to research.
4. Copy relevant templates into the project folder as the work progresses. **Do not fill every template on day one.**
5. Every working session: update [BUILD-LOG-TEMPLATE.md](../templates/BUILD-LOG-TEMPLATE.md) and the project's **Next action**.
6. Capture decisions in [DECISION-RECORD-TEMPLATE.md](../templates/DECISION-RECORD-TEMPLATE.md); capture evidence using [TEST-PLAN-TEMPLATE.md](../templates/TEST-PLAN-TEMPLATE.md).
7. Before publishing, follow [SECURITY.md](../SECURITY.md) and [VISIBILITY-POLICY.md](VISIBILITY-POLICY.md).

## Source of truth
| Concern | Source |
|---|---|
| What projects exist? | `PROJECTS.md` |
| What should I work on now? | GitHub Projects board (Priority, Status, Category, Target Date) |
| What tasks or blockers need discussion? | GitHub Issues |
| Why was a technical decision made? | Decision record (ADR) |
| What was done and what happened? | Dated build log and validation evidence |
| Sensitive configuration, private diagrams, credentials | Private repository or secure secret manager; **never** this public hub |

## Standard project anatomy
Each project begins with a `README.md`; when active, optionally add `charter.md`, `requirements.md`, `research.md`, `decisions/`, `bom.csv`, `build-log.md`, `tests/`, `lessons-learned.md`, `assets/`. Projects with real code or significant hardware schematics should have dedicated repositories linked from the registry.

## Lifecycle and exit criteria
| Status | Exit criteria |
|---|---|
| Ideas | Problem/goal and next research question recorded |
| Research | Options evaluated, open questions and evidence recorded |
| Planning | Scope, requirements, architecture/BOM, risks, validation criteria defined |
| In Progress | Working prototype or implementation documented |
| Testing | Acceptance tests run; results and outstanding defects recorded |
| Completed | Success criteria met, documentation reviewed, remaining follow-ups categorized |
| On Hold | Pause reason, prerequisites, and restart step recorded |

Statuses describe work state; **Completed** does not mean permanently maintained. Reopen or create follow-up issues if maintenance is needed.

## Naming and conventions
- Project IDs: `AEG-NNN` sequential, unique, retained forever.
- Paths: lowercase kebab-case.
- Dates: `YYYY-MM-DD`; timestamps include timezone if time matters.
- Tests: use a stable project-specific test identifier (`T01`, `TST-001`, etc.) consistently; decisions: `ADR-0001` per project.
- Reference GitHub issue URLs, repository commits, firmware/software versions and measurement conditions.
- Write **observed** versus **expected** results explicitly; don't invent performance numbers.
- Keep all links relative inside the repository when possible.

See [WORKFLOW.md](WORKFLOW.md), [BOARD-CONFIGURATION.md](BOARD-CONFIGURATION.md), and [VISIBILITY-POLICY.md](VISIBILITY-POLICY.md).

## Documentation voice and reproducibility standards

I write build journals **in first person**, accurately recording what I physically installed, configured, tested, observed, and decided. I avoid narration such as “the user confirmed” or “the user ran.” Generic project templates may use instructional language, but actual build sessions must read as my engineering record.

Each dated build entry should capture **the actual command/action and execution context** (Windows, Kali, Raspberry Pi, phone), why it was chosen, expected versus observed output, errors and recovery, exact package/firmware versions, proof of tests, and what remains open. GUI operations need ordered instructions as well. **Do not fabricate terminal commands or source files** that were never recorded. When reconstructing a reproducible setup procedure from committed source, label it “reconstruction” and keep it separate from verified execution history.

- Use placeholders such as `<PI_LAN_IP>` and `<DEVICE_MAC>` for real addresses/identifiers, without publishing the originals.
- Do not publish plaintext credentials, private keys, wireless network names tied to real people, geolocation/capture filenames, secrets, or unauthorized packet captures.
- Only link photographs that are already committed or accessible, after cropping/redaction of sensitive details.
- Before calling a build *Completed*, distinguish the operational build from deferred acceptance tests and track any remaining risks.
- Audit project IDs and relative links whenever moving or renaming a project. Keep [PROJECTS.md](../PROJECTS.md) the sole canonical registry.
