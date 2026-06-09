## 5. The Enforcement Pipeline

A practical workflow for agentic invariant enforcement has seven stages.

### 5.1 Observe

Start with what the code already does.

The source may be a recurring review comment, a previous incident, a known bug class, a repeated framework convention, a scanner finding that requires human interpretation, or a senior engineer’s intuition that “this class of path should always do X before Y.”

At this stage, the agent can help gather examples. It can search for similar routes, find naming patterns, identify helper usage, inspect call sites, and produce a rough map of how the application currently expresses the behavior.

At this stage, the work product is evidence. The useful material is examples, counterexamples, helper names, call paths, and review notes that may later justify a rule.

### 5.2 State the invariant

The next step is to write the invariant plainly.

A useful invariant should name the subject, the condition, the effect, and the required relationship.

Examples follow.

“Any route that mutates an invoice must load the invoice through an actor-and-organization-scoped query before the mutation.”

“Any public serializer for account data must exclude recovery credentials, fraud flags, internal notes, and encrypted seed material.”

“Any partner webhook handler must verify the request signature before parsing the body or performing any state-changing effect.”

“Any critical dependency finding may be marked non-blocking only when the vulnerable symbol is unreachable or the exploit preconditions are unsatisfied under deployed configuration.”

The invariant should be narrow enough that a tool can be wrong in understandable ways. If the rule is too broad, every violation becomes an argument. If the rule is narrow, violations become reviewable.

### 5.3 Identify evidence

The agent should collect examples and counterexamples.

Positive evidence includes compliant code paths, standard helpers, established service objects, safe serializers, accepted dependency review notes, or historical fixes.

Negative evidence includes known bugs, synthetic violating fixtures, intentionally unsafe examples, or code paths that lack the expected structure.

The key is to avoid relying on vibes. A local invariant becomes credible when it is supported by the application’s own repeated behavior.

### 5.4 Generate the control

The control should be as simple as possible.

Sometimes a Semgrep rule is enough. Sometimes a CodeQL query is appropriate. Sometimes the control should be a custom AST walker. Sometimes it should be a framework-aware analyzer that understands routes, middleware, serializers, and ORM calls. Sometimes it should be a generated test that asserts all routes in a family use the approved helper. Sometimes it should be a codegen constraint that makes the unsafe path difficult to express.

The agent can draft multiple versions. The human should choose the one with the best maintenance profile.

The design question should focus on the smallest enforcement artifact that catches the repeated failure with acceptable noise.

### 5.5 Test against fixtures

A control without fixtures is just another opinion.

Every application-specific AppSec control should include known-good and known-bad cases. Representative fixtures matter more than large fixtures.

A tenant-boundary rule might include one safe route using the actor-scoped helper, one unsafe route using direct lookup, one route that loads through an intermediate service, and one intentionally unresolved dynamic case.

A serializer exposure rule might include one public serializer, one internal serializer, one inherited serializer, and one serializer that exposes a banned field through a nested object.

A dependency reachability control might include one reachable vulnerable symbol, one present-but-unreachable dependency, one configuration-gated path, and one unknown case that must be routed to the unresolved state.

Fixtures are what make the control repeatable. They let the team change the rule without forgetting what it was supposed to protect.

### 5.6 Produce reviewable findings

A finding should carry enough proof for a reviewer to understand and challenge it without reconstructing the entire path from scratch.

For an authorization invariant, the finding should identify the route, externally controlled parameters, actor source, resource lookup, tenant or ownership binding, dangerous effect, and missing or weaker guard.

For a serializer invariant, it should identify the route or caller, serializer, exposed field, field classification, audience, and policy expectation.

For a dependency invariant, it should identify the package, vulnerable symbol, reachable call path if known, exploit preconditions, runtime configuration, and reason the finding is blocking, warning, accepted, or unresolved.

The control should hand reviewers the smallest artifact that makes the issue inspectable, including the local facts that explain why this path matters in this application.

### 5.7 Integrate with fail, warn, and accept modes

Not every control should fail every build.

Some invariant violations are release blockers. Some are warnings. Some require security review. Some are accepted risks with expiration dates. Unknowns should route to a human review state.

A useful enforcement tool needs at least four states.

Fail means the invariant violation is clear and the risk is unacceptable for merge or release.

Warn means the path is suspicious, but the evidence is incomplete or the impact is limited.

Accept means the risk is documented, time-bounded, and approved.

Unresolved means the tool lacks enough evidence to prove compliance or violation, and the uncertainty itself is the output.

Block-only AppSec tooling eventually gets bypassed, while tooling that distinguishes failure, warning, acceptance, and uncertainty can fit into normal engineering workflows.
