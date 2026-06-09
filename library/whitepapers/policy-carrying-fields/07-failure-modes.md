## 7. Failure Modes

Policy-carrying fields can fail if the annotations become decoration.

The first failure mode is assertion without verification. A field marked `NeverLog` means little if no tool checks logging paths. The annotation has to feed a checker, a fixture, a review artifact, or a CI gate.

The second failure mode is policy drift. A field may start as staff-only and later become safe for patient-facing export. Another field may start as safe for logs and later become sensitive after product changes. Annotations need owners, review history, and tests.

The third failure mode is broad annotation vocabulary. If every team invents twenty overlapping labels, the tool cannot enforce them consistently. The first vocabulary should be small. It should focus on visibility, mutation authority, logging, serialization audience, encryption, and audit.

The fourth failure mode is false precision. A field-level policy is precise, but field flow is still hard. Dynamic dispatch, reflection, framework callbacks, and serialization helpers can hide paths. A useful tool reports unresolved evidence when it cannot prove safety.

The fifth failure mode is treating AI output as proof. AI can help write the checker, but the checker has to run against source, produce evidence, and survive review without the original agent session.
