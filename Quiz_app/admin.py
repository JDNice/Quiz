from django.contrib import admin
from .models import Quiz, MultipleChoiceAnswer,MultipleChoice

admin.site.register(Quiz)
admin.site.register(MultipleChoiceAnswer)
admin.site.register(MultipleChoice)
