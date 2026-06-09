## 8. Proof Artifacts

Application-specific controls must produce evidence because their authority comes from local reasoning. If a generic scanner flags `eval`, the reviewer already understands the broad danger. If a local invariant tool flags a tenant-boundary violation, the reviewer needs to know why the tool believes the path violates this application’s ownership model. Without that proof, the finding becomes backlog noise.

A proof artifact should be small enough to review and complete enough to challenge.

For a route-to-effect invariant, the artifact should name the route or entrypoint, request-controlled values, actor source, resource lookup, tenant or ownership binding, dangerous effect, missing or weaker guard, comparable safe paths when available, and source spans for every claim.

For a serializer exposure invariant, the artifact should name the route or caller, serializer or response builder, field, field classification, audience, exposure policy, and the path by which the field reaches the response.

For a dependency reachability invariant, the artifact should name the package and version, vulnerable symbol or behavior, known exploit preconditions, reachable application call paths if any, configuration evidence, compensating controls, and final triage state.

Proof artifacts make agentic tooling usable in security workflows. The agent can help produce them, and each claim must remain inspectable through evidence.
