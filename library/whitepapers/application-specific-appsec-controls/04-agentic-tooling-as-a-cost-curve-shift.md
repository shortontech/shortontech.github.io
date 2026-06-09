## 4. Agentic Tooling as a Cost-Curve Shift

The main change is cost. Application-specific security enforcement has always been possible. A strong security engineer could read a codebase, learn its local rules, and write a custom checker. The limiting factor was cost, because custom analysis required time, tooling fluency, language expertise, framework knowledge, test design, and maintenance discipline. Agentic tooling lowers several of those costs at once.

The agent can help map the codebase. It can identify route handlers, serializers, database access patterns, authorization helpers, and repeated naming conventions. It can compare sibling paths and surface repeated structures. It can draft a proposed invariant from examples. It can write the first version of a rule, generate fixtures, run the tool, inspect failures, revise the implementation, and document the result.

The agent becomes useful without becoming authoritative. The human engineer still supplies judgment about which invariant matters, whether the examples are representative, whether the checker is overfitted, whether the false positives are acceptable, and whether the finding artifact proves what it claims. The agent supplies throughput.

The distinction between agentic review and agentic tooling is durability. Agentic review asks a model to inspect code and produce an answer. Useful answers can still be ephemeral, difficult to regression test, and unlikely to improve the repository after the conversation ends.

Agentic tooling asks a model to help create an enforcement artifact. The artifact stays in the repository. It can be tested, reviewed, versioned, tuned, and improved. It can run on every pull request, fail a build, warn a reviewer, generate a decision record, or attach evidence to a security ticket. The agent's most valuable contribution is the machinery that makes future human judgments cheaper.
