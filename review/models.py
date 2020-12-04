from django.db import models
from django.contrib.auth.models import User


class Group(models.TextChoices):
    HEAD = 'HED', 'Head'
    COLLEAGUE = 'COL', 'Colleague'
    MENTOR = 'MNT', 'Mentor'
    MENTEE = 'MTE', 'Mentee'


class Role(models.TextChoices):
    DEVELOPER = 'DEV', 'Developer'
    HEAD = 'HED', 'Head'


class Position(models.TextChoices):
    TRAINEE = 'TRA', 'Trainee'
    JUNIOR = 'JUN', 'Junior'
    MIDDLE = 'MID', 'Middle'
    SENIOR = 'SEN', 'Senior'


class Score(models.IntegerChoices):
    NONE = 0, 'No data to decide'
    WAY_BELOW_EXPECTATIONS = 1, 'Way below expectations'
    BELOW_EXPECTATIONS = 2, 'Below expectations'
    MEET_EXPECTATIONS = 3, 'Meet expectations'
    ABOVE_EXPECTATIONS = 4, 'Above expectations'
    WAY_ABOVE_EXPECTATIONS = 5, 'Way above expectations'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=Role.choices)
    position = models.CharField(max_length=3, choices=Position.choices)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.user.username}'


class Reviewer(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    group = models.CharField(max_length=3, choices=Group.choices)

    def __str__(self):
        return f'{self.employee} {self.get_group_display()}'


class Review(models.Model):
    reviewee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reviewers = models.ManyToManyField(Reviewer)
    date = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.reviewee} on {self.date}'


class Criteria(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Expectation(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    position = models.CharField(max_length=3, choices=Position.choices)
    description = models.TextField()

    def __str__(self):
        return f'{self.criteria} {self.position}'


class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    score = models.IntegerField(choices=Score.choices)
    comment = models.TextField()

    def __str__(self):
        return f'{self.criteria} {self.score} {self.comment}'
