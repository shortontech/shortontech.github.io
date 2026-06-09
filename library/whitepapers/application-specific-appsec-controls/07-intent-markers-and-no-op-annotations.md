## 7. Intent Markers and No-Op Annotations

Application-specific controls become easier when developers can mark intent.

An intent marker is a runtime-neutral annotation, decorator, attribute, structured comment, or metadata entry that states what security invariant a path is supposed to satisfy.

The marker makes a security claim machine-readable without changing whether the implementation is actually secure.

For example:

```python
@tenant_bound(resource="invoice", tenant="organization")
@audit_required(effect="billing.mutation")
def update_invoice(request, organization_id, invoice_id):
    ...
```

The annotation may be a no-op at runtime. The enforcement tool reads it and asks whether the implementation satisfies the claim.

Where is the actor loaded? Where is the tenant loaded? Where is the invoice loaded? Is the invoice lookup scoped to the actor and tenant? Does the object that was checked reach the mutation? Is an audit record written before or after the irreversible effect? Are unresolved dynamic calls recorded?

The intent marker is an assertion that the enforcement tool must verify against the implementation.

It lets developers declare what kind of review a path requires. It gives tools a stable surface to inspect. It reduces guesswork. It creates a bridge between human design intent and static enforcement. It can be adopted incrementally because no-op markers do not change runtime behavior.

It also creates accountability. A handler marked `tenant_bound` that does not actually bind tenant and resource violates a stated local contract, which is more precise than a generic missing-best-practice warning.

The broader principle is that application-specific security controls should support both inferred invariants and explicit developer-declared invariants, with verification applied to both.
