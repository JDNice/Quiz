# Generated by Django 3.2.4 on 2021-06-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='answer')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100, verbose_name='Title')),
                ('questions', models.ManyToManyField(to='Quiz_app.MultipleChoice')),
            ],
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='choices',
            field=models.ManyToManyField(to='Quiz_app.MultipleChoiceAnswer'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='correct_answer',
            field=models.ManyToManyField(blank=True, related_name='correct', to='Quiz_app.MultipleChoiceAnswer'),
        ),
    ]
