## 9. Failure Modes

Application-specific enforcement can fail badly.

The first failure mode is overfitting. A tool may encode today’s structure too tightly and reject legitimate future changes. This is especially likely when an agent learns from too few examples. The fix is to keep invariants narrow, include fixtures, and record unresolved cases honestly.

The second failure mode is false authority. A generated control may look official because it runs in CI, even if its model is weak. The fix is to require proof artifacts and human review before treating a control as release-blocking.

The third failure mode is noisy enforcement. If a local control produces too many weak findings, developers will route around it. The fix is to support fail, warn, accept, and unresolved states so different signal strengths receive different treatment.

The fourth failure mode is hidden uncertainty. Dynamic dispatch, reflection, metaprogramming, framework magic, and unresolved imports can all hide relevant behavior. A good tool should emit unresolved evidence for unknown paths.

The fifth failure mode is policy drift. An invariant may be correct when written and wrong six months later, so local controls need owners who can update them as the application and risk model change.

The sixth failure mode is agent dependency. A generated tool has to be understandable and maintainable after the original agent session. The generated code must be readable, tested, documented, and versioned like any other security-critical artifact.
