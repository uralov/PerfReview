# Generated by Django 3.1.4 on 2020-12-04 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20201204_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('HED', 'Head'), ('COL', 'Colleague'), ('MNT', 'Mentor'), ('MTE', 'Mentee')], max_length=3)),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='review',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='reviewer',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewers',
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, choices=[('TRA', 'Trainee'), ('JUN', 'Junior'), ('MID', 'Middle'), ('SEN', 'Senior')], max_length=3, null=True),
        ),
        migrations.DeleteModel(
            name='Reviewer',
        ),
        migrations.AddField(
            model_name='survey',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review'),
        ),
        migrations.AddField(
            model_name='survey',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.employee'),
        ),
        migrations.AddField(
            model_name='answer',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.survey'),
        ),
    ]
