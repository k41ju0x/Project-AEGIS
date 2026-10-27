# GitHub Projects Board Standard

[Project Aegis | Research & Development](https://github.com/users/k41ju0x/projects/3/views/1)

## Fields
| Field | Type | Recommended values |
|---|---|---|
| Status | Single select | Ideas, Research, Planning, In Progress, Testing, Completed, On Hold |
| Priority | Single select | Critical, High, Medium, Low |
| Category | Single select | Home Lab, RF / Wireless, Cybersecurity, Hardware, Automation, Other |
| Target Date | Date | Leave empty unless the date is meaningful |
| Repository | GitHub built-in where available | Source issue's repository |

## Views
- **Board** grouped by Status: workflow and blockers.
- **Table**: master triage, priority and ownership (no duplicate spreadsheet required).
- **Roadmap**: optional later when start/target dates are established.

## Linking
Each AEG project gets one parent-level project tracking issue; implementation can spawn additional child issues. Add issues from other project repositories to this same board. A GitHub Project item is **not** itself a repository or a folder.

## Initial suggested triage
- AEG-001 Project NEXUS: priority High, category Home Lab; confirm current actual status.
- AEG-002 Meshtastic: priority High, category RF / Wireless, Planning.
- AEG-003 Pwnagotchi: priority Medium, category Cybersecurity, Ideas.
- AEG-004 Remote Access Device: priority Medium, category Hardware, Ideas.

Treat these as suggestions, not audited progress. Custom field/board configuration is managed in GitHub UI and is not automatically synchronized from Markdown.

## Weekly 10-minute review
1. Review In Progress and On Hold.
2. Move research-ready items out of Ideas.
3. Ensure each active issue has an owner (if applicable) and next action.
4. Review deadlines and stale tasks.
5. Update `PROJECTS.md` for durable project-level changes.
