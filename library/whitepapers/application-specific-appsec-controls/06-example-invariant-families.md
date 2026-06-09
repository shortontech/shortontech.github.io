## 6. Example Invariant Families

### 6.1 Tenant boundary invariants

Tenant boundary failures are among the clearest examples of application-specific security risk.

A generic scanner can look for direct object references. A local control can enforce the application’s actual ownership model.

In one application, tenant binding may require `organization_id` to match a route parameter and a session claim. In another, it may require membership in a workspace. In another, it may require account hierarchy, reseller delegation, regional partition, or project-level permission. The invariant is local.

A useful tenant-boundary control asks whether actor, tenant, and resource are bound before the first sensitive effect. Authentication establishes an actor. Authorization still has to connect that actor to the resource.

A finding might say the following.

The route accepts `invoice_id` from the request. The handler loads `Invoice.find(invoice_id)` directly. The current actor is available as `request.user`. Comparable invoice mutation routes use `Invoice.for_actor(request.user).for_org(org_id).find(invoice_id)`. This path reaches `invoice.update(...)` without evidence that the invoice belongs to the actor’s organization.

That is the difference between a generic IDOR warning and an application-specific invariant finding.

### 6.2 Serializer exposure invariants

Serializer exposure is another local invariant family.

Serializer exposure enforcement starts with an application decision about sensitive fields, permitted audiences, and serializer roles. The relevant roles may be public, internal, administrative, or partner-facing.

An application-specific control can maintain a field exposure policy and compare serializers against it. It can detect direct exposure, inherited exposure, nested exposure, and accidental inclusion through broad model-shape serialization.

The strongest version of this control models audience and transformation. A field may be safe for internal admin views and unsafe for customer-facing APIs. A field may be safe after transformation and unsafe in raw form. A field may be safe when redacted and unsafe when serialized directly.

The finding artifact should show the serializer, the field, the audience, the route or caller, and the violated exposure expectation.

### 6.3 Webhook verification invariants

Webhook handlers often have a strict local rule. Verify authenticity before trusting the body.

A generic scanner has limited visibility into the difference between parsing, validation, signature verification, idempotency checks, and state-changing effects in a given framework. An application-specific control can encode the expected sequence.

For a partner webhook family, the invariant might read as follows.

Verify signature before parsing trusted fields. Validate event type before dispatch. Enforce idempotency before mutation. Log rejection without persisting attacker-controlled data.

The control can inspect the handler’s call order, known verification helpers, parsing functions, dispatch paths, and mutation sinks. It can flag handlers that parse before verification, mutate before idempotency, or silently accept unknown event types.

The control should enforce the application’s accepted webhook sequence.

### 6.4 State transition invariants

Many security bugs are invalid state transitions.

A reimbursement needs approval before moving from `submitted` to `paid`. A deployment needs review before moving from `draft` to `production`. A user needs an existing owner or break-glass path before becoming an organization owner. A document needs private attachments removed before becoming public.

These rules belong to the product more than to any universal vulnerability taxonomy.

A local control can model transition families and required preconditions. It can compare peer paths, identify missing review checks, detect audit omissions, and flag direct state assignments that bypass service-layer transitions.

The finding should name the state transition, the effect, the expected preconditions, and the path that bypasses them.

### 6.5 Dependency reachability invariants

Dependency scanning produces too much raw material and not enough judgment.

A critical CVE in a container image becomes a critical application risk through reachability and exploitability. It may be present but unreachable, require a configuration the application does not use, or be mitigated by sandboxing, runtime flags, or disabled features. It may also be fully reachable and urgent.

The local invariant should require evidence-backed downgrades.

A dependency finding can be downgraded only when reachability, exploit preconditions, runtime configuration, and compensating controls are documented with evidence.

Agentic tooling can help here by generating reachability notes, scanning imports and call paths, checking container usage, reading configuration, and producing a structured decision artifact.

The resulting control encodes the team’s dependency triage discipline in the repository so that reachability, exploitability, configuration, and compensating controls are reviewed consistently.
