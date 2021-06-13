from django.shortcuts import render


def start(request):
    return render(request, 'Quiz_app/StartScreen.html')


def question(request):
    return render(request, 'Quiz_app/QuestionPage.html', {'title': 'question1'})
