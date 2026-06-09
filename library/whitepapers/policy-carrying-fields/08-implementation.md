## 8. Implementation Sketch

Start with one policy family.

For healthcare, logging is a strong pilot. Add `NeverLog`, `LogRedacted`, and `LogAllowed` to a small set of fields that already cause review concern. Generate metadata from the schema layer. Write a checker that follows those fields into serializers, event payloads, error contexts, and logging calls. Treat early findings as review candidates.

Once the logging check produces low noise, add visibility. Fields can declare physician-visible, patient-visible, support-visible, or staff-only policy. The checker can compare field policy against serializers and query scopes. The finding artifact should show the field, audience, serializer or route, and missing proof.

Mutation authority should come later. It is usually harder than visibility because it depends on actor state, relationship, workflow, and audit. A `PhysicianMutates` field should require evidence of active treatment relationship, write-scoped role, and audit emission. The first checker should be narrow enough that reviewers can understand every finding.

The final step is promotion. Signals become warnings after the team understands the false positives. Warnings become lintable errors after the check repeatedly finds real drift. CI enforcement should come only after the control has been run across enough code and history to earn trust.
