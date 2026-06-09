## 5. Logging Is the Hard Test

Logging is a good test for policy-carrying fields because logging often defeats vague security intent.

Developers rarely intend to leak sensitive data. They log request objects, error contexts, event payloads, serializer outputs, model snapshots, and diagnostic maps because the system is failing and they need evidence. If field policy is stored only in a wiki page, logging paths will drift. If the policy is carried by the field, tooling can inspect whether the field reaches a log sink.

The enforcement rule can be narrow. Fields marked `NeverLog` may not reach logging sinks. Fields marked `LogRedacted` may reach logging sinks only through approved redaction helpers. Fields marked `LogAllowed` may be logged directly, with the finding artifact still showing the path.

This is where application-specific controls beat generic scanners. A generic scanner can warn about logging a variable named `password` or `token`. A local invariant checker can know that `diagnosis`, `internal_risk_flag`, `recovery_context`, or `payer_denial_reason` carries a specific policy even when the name is not obviously sensitive to a universal tool.

The artifact should be reviewable. It should name the field, the declared policy, the source path, the sink, the transformations seen on the path, and the missing proof. The reviewer should not have to trust a model's summary. The claim should terminate in source-backed evidence.
