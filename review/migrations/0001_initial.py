# Generated by Django 3.0.8 on 2020-12-04 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('DEV', 'Developer'), ('HED', 'Head')], max_length=3)),
                ('position', models.CharField(choices=[('TRA', 'Trainee'), ('JUN', 'Junior'), ('MID', 'Middle'), ('SEN', 'Senior')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Reviewers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('HED', 'Head'), ('COL', 'Colleague'), ('MNT', 'Mentor'), ('MTE', 'Mentee')], max_length=3)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.Employee')),
                ('reviewers', models.ManyToManyField(to='review.Reviewers')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
