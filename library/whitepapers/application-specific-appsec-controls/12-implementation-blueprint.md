## 12. Implementation Blueprint

A team can start small.

The first application-specific AppSec control should be narrow, painful, and repeated. It should come from a class of issues the team has already seen more than once.

Good first candidates include tenant-scoped resource lookup, public serializer field exposure, webhook verification order, dependency reachability documentation, audit logging before irreversible effects, admin-only state transitions, unsafe direct use of request-controlled identifiers, or repeated suppressions from a generic scanner.

The first implementation should prioritize proving the loop over elegance.

Pick one invariant. Gather five safe examples and two unsafe examples. Ask the agent to summarize the repeated structure. Write the invariant in plain language. Generate a first checker. Add fixtures. Run it. Inspect false positives. Simplify. Add a proof artifact. Decide whether the control should fail, warn, or only report. Put it in CI or review.

Start with one narrowly scoped control that catches one real class of repeated local security failure.

Once that works, the pattern compounds. Each new invariant becomes easier because the repository now has a place for local controls, fixtures, documentation, and review decisions.

Over time, the application accumulates a repository-local enforcement layer that reflects its own security model.
