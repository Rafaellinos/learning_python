from django.db import models


# Create your models here.

class Airport(models.Model):
    code = models.CharField(
        max_length=3,
    )

    city = models.CharField(
        max_length=64,
    )

    def __repr__(self):
        return f"Code: {self.code or 'not set'}, City: {self.city or 'not set'}"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="departures",
    )  # Cascade se o Airport for deletado, delete o fligth tbm

    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="arrivals", #  usado: ex: Airport(record).arrivals.all()
    )

    duration = models.IntegerField()

    def __str__(self):
        return f"Origin: {self.origin or 'not set'}, " \
               f"Destination: {self.destination or 'not set'}, " \
               f"Duration: {self.duration or 'not set'}"

    def __repr__(self):
        return f"Origin: {self.origin or 'not set'}, " \
               f"Destination: {self.destination or 'not set'}, " \
               f"Duration: {self.duration or 'not set'}"
