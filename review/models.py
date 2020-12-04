from django.db import models
from django.contrib.auth.models import User


class Groups(models.TextChoices):
    HEAD = 'HED', 'Head'
    COLLEAGUE = 'COL', 'Colleague'
    MENTOR = 'MNT', 'Mentor'
    MENTEE = 'MTE', 'Mentee'


class Roles(models.TextChoices):
    DEVELOPER = 'DEV', 'Developer'
    HEAD = 'HED', 'Head'


class Positions(models.TextChoices):
    TRAINEE = 'TRA', 'Trainee'
    JUNIOR = 'JUN', 'Junior'
    MIDDLE = 'MID', 'Middle'
    SENIOR = 'SEN', 'Senior'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=Roles.choices)
    position = models.CharField(max_length=3, choices=Positions.choices)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.user.username}'


class Reviewers(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    group = models.CharField(max_length=3, choices=Groups.choices)

    def __str__(self):
        return f'{self.employee} {self.group}'


class Reviews(models.Model):
    reviewee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reviewers = models.ManyToManyField(Reviewers)
    date = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.reviewee, self.date
