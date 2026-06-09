## 13. Relationship to Shift-Left Security

Shift-left security often fails because it pushes responsibility left without moving enough judgment, context, or tooling left with it.

Developers are told to own security while the security team remains the only group with enough context to make hard calls. This creates frustration on both sides. Developers receive scanner output they cannot interpret, security teams receive pull requests too late to influence architecture, and the decision machinery remains centralized even when everyone agrees security should happen earlier.

Kern argues that developer ecosystems should take responsibility for ensuring
key security properties. Application-specific controls are a
repository-scale version of that idea. They move local security expectations
into tools, fixtures, gates, and review artifacts that developers can actually
use while building the system
([Kern, 2024](https://research.google/pubs/secure-by-design-at-google/)).

Application-specific controls make shift-left more concrete by giving developers narrow, inspectable security work products supported by local tooling.

Instead of asking every developer to become broadly security-fluent, the program can assign narrow security lanes and support them with tools. One developer can own serializer exposure for a service. Another can own dependency reachability notes. Another can own tenant-boundary fixtures. Another can own converting repeated AppSec findings into local checks.

The senior AppSec engineer still owns standards, review quality, escalation, and final judgment. The work product changes. The security team reviews artifacts and spends less time rediscovering every issue from scratch.

This is where agentic tooling and Human Swarm Mode meet. AI compresses the learning loop for each lane, developers become useful narrow security operators, local controls turn their lane knowledge into enforcement, and expert review keeps the system honest.

Distributed AppSec ownership becomes credible when it is grounded in artifacts.
