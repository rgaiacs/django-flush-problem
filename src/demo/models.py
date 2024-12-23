from django.db import models

class Foo(models.Model):
    bars = models.ManyToManyField(
        "Bar",
        blank=True
    )

class Bar(models.Model):
    foos = models.ManyToManyField(
        "Foo",
        blank=True,
        through="Foo_bars"
    )