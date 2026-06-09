## 3. Application-Specific AppSec Controls

An application-specific AppSec control is a repository-owned enforcement mechanism for a local security invariant.

The control might be a static rule, a framework-aware analyzer pass, a Semgrep or CodeQL query, a generated test, a CI gate, a review bot, a code generation constraint, or a repository linter. It might also be a migration checker, a serializer exposure inventory, a dependency reachability note generator, or a domain-specific rule embedded in the build. The mechanism is secondary. The control has to encode a local expectation and produce evidence when the expectation appears to drift.

A good control has four parts.

First, it has an invariant statement narrow enough to test. “Authorization should be good” is too broad to enforce, while “All organization invoice mutations must use an actor-scoped invoice lookup before mutation” gives the tool a concrete relationship to check.

Second, it has positive examples. The control should know what compliant paths look like. These examples may be fixtures, real source spans, known-safe routes, or generated test cases.

Third, it has negative examples. The control should be tested against intentionally violating paths, known historical bugs, or synthesized cases that demonstrate the failure mode.

Fourth, it has a reviewable finding artifact. When the control fires, it should explain the route, actor source, resource lookup, effect, missing binding, comparable safe paths, and remaining uncertainty.

These properties let a team turn repeated AppSec judgment into infrastructure. A valuable first control is narrow, explicit, testable, and reviewable. Perfection matters less than catching one high-value invariant violation with low noise. In practice, that local analyzer may be more useful than a general scanner that produces hundreds of findings no one trusts.
