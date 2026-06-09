## 2. Generic Scanners and Local Invariants

Generic scanners have to survive many codebases. That constraint shapes their behavior.

They prefer patterns that are broadly meaningful. They look for dangerous functions, known APIs, dependency metadata, language-specific syntax, framework conventions, and common vulnerability signatures. This makes them valuable as a baseline layer. A security program without general SAST, dependency scanning, secret scanning, and basic configuration checks is leaving obvious coverage on the floor.

But the same universality that makes generic tools deployable also limits what they can know.

A generic scanner may recognize an ORM call and even recognize that a request parameter flows into a query. Correct scoping for this application’s ownership model requires local context. A scanner may detect a serializer that emits many fields. Audience-specific field policy has to be encoded somewhere before the tool can enforce it. A scanner may flag a dependency CVE. Reachability through the application’s real execution paths requires deeper application-specific analysis.

That context is the difference between pattern detection and invariant enforcement. Vulnerability classes travel across applications, while invariants express the local rules a specific system depends on.

Kern's description of Secure by Design at Google is the closest predecessor to
this framing. Security posture emerges from the developer ecosystem, and
important security properties should be stated as invariants for the system and
its tooling to uphold
([Kern, 2024](https://research.google/pubs/secure-by-design-at-google/)).

For direct object references, the portable vulnerability class warns that authorization may be missing. The local invariant is more precise. Every route that reads or mutates tenant-owned invoices must bind actor, organization, and invoice before the first database effect, and the object used at the effect must be the bound object.

For sensitive data exposure, the portable class warns that serializers can emit fields carelessly. The local invariant names the actual exposure policy. Public account responses may expose email and display name, but never recovery tokens, internal notes, fraud flags, password metadata, or encrypted seed material, regardless of serializer inheritance.

For dependency risk, the portable class says that CVEs should be remediated. The local invariant describes when a finding blocks release. The vulnerable symbol must be reachable, the exploit preconditions must be satisfied, and attacker-controlled input must reach the vulnerable behavior under deployed configuration.

Local invariants are what senior reviewers actually enforce. They are why two code paths that both “have authentication” can receive very different security judgments. They are why a critical CVE can be urgent in one service and documented risk in another. They are why the same serializer pattern can be harmless internally and dangerous on a public route.

The argument of this paper is that agentic tooling makes these local invariants cheap enough to encode.
