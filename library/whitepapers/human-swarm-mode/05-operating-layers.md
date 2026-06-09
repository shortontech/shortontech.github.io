## Operating Layers

Human Swarm Mode has five operating layers: expert command, problem queues,
niche learners supported by AI, reviewable artifacts, review and culling, and
eventual lane expertise.

### Expert Command

At the center are one or more senior experts, engineers, or domain experts.
Their job is not to do every task. Their job is to define the problem frontier,
decompose it into queues, establish standards of evidence, review results,
reject bad reasoning, and decide which paths deserve more investment.
In practical terms, they own taste, direction, and correctness.

Expert command is necessary because AI capability is uneven across tasks.
Dell'Acqua et al. describe this as a jagged technological frontier: AI can
improve performance on some knowledge-work tasks while degrading it on others.
The expert's job is to know where AI can be trusted, where it must be
constrained, and where human judgment must remain primary
([Dell'Acqua et al., 2023](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700)).

### Problem Queues

The work is broken into small, inspectable problem units. Each unit has a clear
question, expected artifact, acceptance condition, and review path.

Examples:

- Explain why this subsystem drifts under temperature change.
- Build a test fixture for this repeated failure mode.
- Summarize the five most relevant papers on this process constraint.
- Compare three commercially available components against this tolerance
  requirement.
- Reproduce this simulation result and identify parameter sensitivity.
- Create a calibration checklist that a technician can follow without
  improvising.
- Document every observed failure mode in this process lane.

The unit of work is not "become an expert in lithography." The unit is a
bounded uncertainty that one operator can own until it is resolved, explicitly
bounded, or escalated to someone with broader authority.

### Niche Learners

The swarm consists of smart people selected for learning speed, curiosity,
discipline, mechanical intuition, math tolerance, documentation habits, and
willingness to be corrected.

They do not need traditional credentials for every lane. They need a narrow
target, good tools, fast feedback, and clear evidence standards.

A strong swarm may include technical-school graduates, machinists, software
generalists, physics undergraduates, self-taught engineers, manufacturing
workers, military technicians, hobbyists, failed startup builders, and people
who were filtered out by school but not by reality.

Selection should therefore emphasize whether a person can learn, measure,
document, and improve in a narrow lane, not whether they already carry the
prestige markers of a finished expert.

### AI as Work Infrastructure

AI supports every operator as a personal tutor and productivity layer. It
explains unfamiliar concepts, generates study paths, summarizes literature,
drafts experiments, builds small tools, checks assumptions, creates
documentation, and helps translate between disciplines.

AI is not treated as the source of truth. It is treated as acceleration
infrastructure. Claims still require evidence. Results still require review.
Measurements still beat generated prose.

AI assistance should therefore be treated as infrastructure, not authority.
Dell'Acqua et al. show that AI can produce large gains inside its capability
frontier while harming performance outside it. Human Swarm Mode treats that as
a design constraint: operators may use AI aggressively for explanation,
drafting, simulation, and comparison, but claims must still terminate in
evidence ([Dell'Acqua et al., 2023](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700)).

Peng et al.'s controlled GitHub Copilot experiment similarly supports the narrow
claim that AI can accelerate bounded software tasks, while leaving open the
broader question of long-term competence and maintainability
([Peng et al., 2023](https://arxiv.org/abs/2302.06590)).

### Artifact-Based Review

Every work unit produces an artifact that can be reviewed without replaying the
entire thought process. The artifact may be a memo, simulation, dataset, test
fixture, measurement log, failure-mode catalog, annotated bibliography,
reproducibility script, or decision record.

Artifact discipline is what prevents swarm mode from becoming chaos. The team
does not accept confidence, fluency, or vibes as substitutes for evidence; it
requires artifacts that can be inspected, challenged, and reproduced.

The senior expert does not have to evaluate an operator's worth in the abstract.
They can ask a narrower and more useful question: does this artifact prove what
it claims, and can another person verify it?
