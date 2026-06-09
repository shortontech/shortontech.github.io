## 6. Generated Metadata as a Concrete Pattern

The model annotation is only the beginning. The useful control comes from carrying the field policy into generated metadata that analyzers can read consistently.

In a Django-style implementation, each policy-bearing field can expose metadata describing visibility, mutation authority, logging behavior, serialization audience, audit requirements, and storage requirements. A checker can read that metadata directly from the model layer and compare it against serializers, log sinks, query scopes, and mutation paths.

Generated metadata gives security tooling a stable place to stand. A sensitive field routed into a public serializer can be flagged. A field marked `NeverLog` can be traced toward logging sinks. A field marked `PhysicianMutates` can require evidence of relationship, role, workflow, and audit before a write path is accepted.

The healthcare extension is a natural next step. A model field can declare healthcare-specific policy such as PHI, physician visibility, mutation authority, log redaction, audit requirements, and patient-facing serialization. The generated model metadata carries those policies forward. Static analysis then checks whether application code respects them.

Pickle is a useful reference point because it already treats schema declarations as the source of generated model metadata, response types, serialization helpers, ownership scopes, and visibility maps. Its migration annotations are one way to provide a faithful policy surface. The same idea can be applied to an existing ORM by augmenting normal model fields rather than replacing the model layer.
