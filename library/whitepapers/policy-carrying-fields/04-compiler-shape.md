## 4. The Compiler Shape

Application-specific security tooling does not need mystical analysis. Much of the work is ordinary compiler and graph work applied to application code.

The analyzer reads the schema or model layer and extracts policy-bearing fields. It reads routes, handlers, service methods, serializers, background jobs, logging calls, and mutation sinks. It builds facts about where fields are loaded, transformed, checked, serialized, logged, or written. Then it connects those facts into a graph that can be queried.

Tarjan's algorithm is a useful example because real applications are not clean trees. Service methods call helpers, helpers call other services, serializers call methods, and framework hooks create cycles. Strongly connected components let the analyzer collapse cyclic regions of the call graph into units it can reason about. The result is not perfect understanding. It is a tractable structure for asking local questions.

For a `NeverLog` field, the question is whether any path from the field reaches a logging sink without an approved suppression or redaction step. For a `LogRedacted` field, the question is whether the path passes through an approved redaction helper before logging. For a `PhysicianMutates` field, the question is whether a mutation path has evidence of active treatment relationship, write-scoped role, and audit emission before the write.

AI helps because building these analyzers is repetitive. It can draft the AST extractor, generate graph fixtures, implement the first query, inspect false positives, and turn examples into tests. The useful endpoint is still a versioned control the repository can run again.
