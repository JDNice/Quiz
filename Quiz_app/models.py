from typing import List

from django.db import models

class MultipleChoiceAnswer(models.Model):
    answer = models.TextField('Answer')
    def __str__(self):
        return  self.answer


class MultipleChoice(models.Model):
    question = models.TextField('question')
    choices = models.ManyToManyField(MultipleChoiceAnswer)
    correct_answer = models.ManyToManyField(MultipleChoiceAnswer, related_name="correct", blank=True)

    def __str__(self):
        return self.question

class Quiz(models.Model):
    tittle = models.CharField('Title', max_length=100)
    questions = models.ManyToManyField(MultipleChoice)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.tittle