## 2. Add Policy to the Existing ORM

The practical version of this idea does not replace the ORM. It adds policy to the ORM surface the application already trusts.

In Django, Flask-SQLAlchemy, Rails, and similar frameworks, that surface is usually the model definition. The model already defines field type, nullability, relationships, indexes, defaults, and validation hints. Policy metadata belongs beside those properties because the field is where the application gives data its durable shape.

The shape is simple. A normal Django model field can be wrapped by a policy-aware field class or extended with metadata the application already expects tooling to understand.

```python
class PatientNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    diagnosis = PolicyTextField(
        policy=[PHI, PhysicianSees, LogRedacted],
    )

    treatment_plan = PolicyTextField(
        policy=[PHI, PhysicianSees, PhysicianMutates, AuditRequired],
    )

    internal_risk_flag = PolicyCharField(
        max_length=64,
        null=True,
        policy=[StaffOnly, NeverLog],
    )
```

This is not a new persistence model. The application still reads and writes normal model objects. The annotations give tools enough information to ask whether access, mutation, serialization, and logging paths respect the declared policy.

The field class can expose metadata to static analyzers, serializers, logging checks, test fixtures, and CI rules. In Django, the metadata can live on the field object, in `Meta`, in a companion registry, or in generated model metadata. The exact storage mechanism matters less than making the policy inspectable from the same model surface developers already use.

The important lesson is that model-level field policy can become executable security infrastructure when the analyzer understands it.
