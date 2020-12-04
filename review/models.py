from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.CharField(max_length=3, choices=Role.choices)
    position = models.CharField(max_length=3, choices=Position.choices, null=True, blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.user.username}'


class Review(models.Model):
    reviewee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()

    @property
    def avg_criterias_score(self):
        avg_criterias_score = {}
        for survey in self.surveys.all():
            for answer in survey.answers.all():
                if answer.criteria not in avg_criterias_score:
                    avg_criterias_score[answer.criteria.name] = []
                avg_criterias_score[answer.criteria.name].append(answer.score)
        for k, v in avg_criterias_score.items():
            avg_criterias_score[k] = sum(v) / len(v)
        return avg_criterias_score

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.reviewee} on {self.date}'


class Survey(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='surveys')
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    group = models.CharField(max_length=3, choices=Group.choices)
    due_date = models.DateField()

    @property
    def avg_score(self):
        return self.answers.aggregate(Avg("score"))['score__avg']

    def __str__(self):
        return f'{self.review} for {self.reviewer} due to {self.due_date}'


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
    # TODO remove null=True
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='answers', null=True)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    score = models.IntegerField(choices=Score.choices)
    comment = models.TextField()

    def __str__(self):
        return f'{self.criteria} {self.score} {self.comment}'
