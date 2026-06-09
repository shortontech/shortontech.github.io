## 11. SecureSentry as a Verification Case

SecureSentry is the prototype that made this model concrete. It is a Sentry-aware
static analyzer built to test whether application-specific invariants could be
modeled against a large real application rather than a toy benchmark. Its output
posture is explicit. Findings are source-backed review artifacts for human
validation.

The analyzer encodes narrow proof policies over Sentry-specific concepts. These
include organization, project, and team boundaries, membership lifecycle, durable
credential authority, external identity cleanup, service hook secrets, external
storage cleanup, cross-service context export, internal proxy request steering,
impersonation-sensitive mutation, and secondary-channel disclosure.

This maps directly onto the enforcement pattern in this paper. A recurring
review concern becomes a spec. The spec defines the local invariant, the semantic
model, implementation slices, acceptance tests, and risk controls. The analyzer
extracts facts such as ownership models, lifecycle markers, query shapes, object
uses, boundary provenance, and proof gaps. The resulting review artifact names
the missing proof and points to source-backed evidence.

Several invariant packs illustrate the difference between generic scanning and
local enforcement. The `OrganizationMember` live-invariant pack checks whether a
role-bearing membership row is approved and live before it is treated as
authority. The `ServiceHook` secret contract pack checks whether creator-known
signing material survives creator removal without rotation, invalidation, or a
documented owner-independent contract. The bulk lifecycle pack looks for bulk
deletion of owner rows where per-instance cleanup may be the only proven
external-storage cleanup path. The cross-service context export pack checks
whether exported organization context has matching membership and authority proof
and treats internal service boundaries as claims that need supporting evidence.

The findings are therefore phrased as TP-shaped review candidates. For example,
the EventAttachment finding identifies a row deletion path, a V1 blob cleanup
path, and the proof needed to downgrade the concern. The Seer context finding
identifies the membership lookup, exported organization/user context, and the
missing approved/live membership proof. That format demonstrates the core claim
of this paper in concrete form. Reviewable artifacts should make local security
reasoning inspectable without asking the reviewer to trust an agent's final
judgment.

SecureSentry also shows how an invariant enforcement app matures. Early signals
should be treated as candidates for review. The team runs them against code,
commit history, fixtures, and real review examples, measures false positives,
and refines the invariant until the finding shape is stable. Once a check has
produced little to no false positives for long enough to earn trust, it can
graduate from signal to lintable error. After that, it belongs in CI/CD, where
the repository rejects regressions automatically and removes the need to
rediscover the same local rule during every review.

The graduation path depends on trust built over repeated runs. A good control
should be run across many commits, especially older commits where the team
already understands the expected risk shape. If the tool repeatedly finds the
same meaningful proof gap without spurious noise, it becomes executable memory
for the application's security model.

SecureSentry also shows why agentic tooling matters. Building this kind of
analyzer requires repeated movement from code reading to invariant writing to
fact extraction to fixture design to finding review. Agentic tooling lowers the
cost of that loop. The endpoint is a tested repository control that remembers a
security judgment and produces evidence when the code drifts away from it.
