## 3. Intent Becomes Concrete

Field annotations are not proof. They are claims the system can inspect.

That distinction matters. A field marked `NeverLog` may still be logged by a careless code path. A field marked `PhysicianMutates` may still be modified through an unguarded service. A field marked `OwnerSees` may still leak through an overly broad serializer. The annotation does not make the implementation safe. It gives enforcement tooling a concrete claim to verify.

Without the annotation, the reviewer has to infer policy from naming, domain memory, and nearby code. With the annotation, the question becomes sharper. Does this field enter a log sink. Does this serializer include a field the audience cannot see. Does this mutation path prove the actor has the required relationship. Does this query scope bind the patient, physician, and care context before the sensitive effect.

The annotation turns review intent into a stable surface. The analyzer can read it repeatedly. The test suite can fixture it. CI can enforce it after the check has earned trust. A human reviewer can inspect the generated evidence and challenge the reasoning.

For healthcare, the field is often the correct level of precision. A model may contain PHI and non-PHI. It may contain data visible to patients, physicians, billing staff, and internal reviewers. It may contain fields that can be logged after redaction and fields that should never be logged at all. Model-level traits are useful for broad categories, but field-level annotations capture the policy that decides where data may flow.
