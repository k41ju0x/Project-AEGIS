# Engineering Workflow — From Idea to Verified Build

## 1. Capture
Open one project intake issue with `AEG-XXX — Name`; record purpose, category, constraints, initial visibility and **next action**. Add the issue to [the board](https://github.com/users/k41ju0x/projects/3/views/1). Don't create dedicated repos for unvalidated ideas.

## 2. Research
Record dated notes and **source links**; separate confirmed facts, assumptions, hypotheses and unresolved questions. Compare options against project requirements. Use the [research template](../templates/RESEARCH-TEMPLATE.md).

## 3. Plan
Draft [charter](../templates/CHARTER-TEMPLATE.md), [requirements](../templates/REQUIREMENTS-TEMPLATE.md), architecture boundaries, [BOM](../templates/BOM-TEMPLATE.csv) and risks. Write an [ADR](../templates/DECISION-RECORD-TEMPLATE.md) for consequential choices. Define acceptance tests **before** assembly.

## 4. Implement
Keep a dated [build log](../templates/BUILD-LOG-TEMPLATE.md) explaining intent, actions, results and recovery steps. Store reproducible, sanitized configs; avoid raw sensitive logs. Link major milestones to issues/commits.

## 5. Validate
Use [test plan](../templates/TEST-PLAN-TEMPLATE.md) with measurable pass/fail criteria; record environment, tool versions, evidence references and actual outcomes. File follow-up issues for failures.

## 6. Finish or pause
Publish [lessons learned](../templates/LESSONS-LEARNED-TEMPLATE.md). Mark the project Completed only after reviewing acceptance criteria and publication safety. For On Hold, record blocker, last working state and one explicit restart action using [session handoff](../templates/SESSION-HANDOFF-TEMPLATE.md).

## Minimum update every work session
- Date and context
- Change/action performed and **why**
- Outcome and supporting evidence
- Current blockers or risks
- Next concrete action
- Board status updated only when its meaning has changed

## Definition of Done
- [ ] Success criteria verified with evidence (or deviations documented)
- [ ] README and project registry reflect current state
- [ ] BOM/versions/architecture accurate as-built
- [ ] Build log and test findings navigable
- [ ] Sensitive material sanitized and access reviewed
- [ ] Remaining issues and next maintenance step recorded

## Repository graduation triggers
Create a separate repository when a project has its own executable code, hardware fabrication files, significant assets, external collaborators, distinct release cadence, or confidential implementation. **Keep a public summary and link in Aegis**; do not use nested Git repositories inside the hub.
