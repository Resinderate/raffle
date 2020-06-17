from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quote(models.Model):
    content = models.CharField(max_length=1500)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="quotes")

    def __str__(self):
        return self.content
