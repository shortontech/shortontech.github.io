# Policy-Carrying Fields for Application-Specific Security Tooling

## Abstract

Many security failures happen because code loses track of what a field means. A patient diagnosis is not just text. A webhook secret is not just a string. An internal risk flag is not just a boolean. These fields carry policy. They define who may see the value, who may mutate it, where it may be serialized, whether it may enter logs, and which review evidence is required when the field crosses a boundary.

Most applications already have a place where this meaning can live. They do not need a new ORM. They need policy metadata on the ORM or schema layer they already use, plus tooling that can read that metadata and enforce local invariants.

This paper argues for policy-carrying fields as a practical foundation for application-specific security tooling. A field annotation makes intent concrete. Generated metadata makes the intent inspectable. Static analysis connects the field to serializers, routes, services, tasks, logs, and mutation paths. AI-assisted tooling lowers the cost of writing the invariant checks, but the security decision remains grounded in generated metadata and reviewable evidence.

The motivating implementation pattern is ordinary model code with explicit policy metadata. Put policy where the application defines data, carry it into generated metadata, and let enforcement tools verify that code paths obey it. The main argument applies to existing model-based ORMs such as Django.

## 1. Introduction

Security intent is often discussed in review comments and forgotten in code.

A reviewer says a field should never appear in logs. Another reviewer says a field should be visible to support staff and hidden from customers. A product decision says physicians may edit a treatment plan only under an active care relationship. A privacy decision says an internal risk score may exist in the database and stay out of public APIs.

Those rules are specific, local, and enforceable. The problem is that they are usually written outside the code path that moves the data.

Generic scanners can detect common dangerous APIs and familiar vulnerability classes. They are much weaker at understanding that this application treats one field as physician-visible PHI, another as staff-only operational metadata, and another as safe for redacted logging. The missing layer is a machine-readable declaration of field meaning.

Policy-carrying fields provide that layer. The field definition stays inside the ordinary schema or ORM system. The application continues to use its normal model layer. The difference is that fields carry annotations the toolchain can inspect.

In healthcare, that might mean a field is marked as PHI, physician-visible, nurse-visible, patient-visible, log-redacted, never-log, audit-required, or mutation-restricted. In fintech, the same pattern might apply to account numbers, transaction metadata, sanctions screening results, fraud flags, and internal risk reasons. The domain changes. The mechanism stays the same.
