from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey


class Section(SortableMixin):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quote(SortableMixin):
    content = models.CharField(max_length=1500)
    section = SortableForeignKey(Section, on_delete=models.CASCADE, related_name="quotes")
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    is_positive = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.content
