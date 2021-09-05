from django.db import models


class Customer(models.Model):
    company_name = models.CharField(max_length=220)
    budget = models.PositiveIntegerField()
    employment = models.PositiveIntegerField()
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.company_name)
