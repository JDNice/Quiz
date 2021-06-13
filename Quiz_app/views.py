from django.shortcuts import render
from .models import Quiz, MultipleChoice, MultipleChoiceAnswer
from .services import *
from .TestQuizWithoutDB import *
from .forms import AnswerForm


def start(request):
    quiz = TestQuiz.quiz_dto
    TestQuiz.question_id = 1
    return render(request, 'Quiz_app/StartScreen.html', {'quizname': quiz.title})


def question(request):
    #form = AnswerForm()
    #context = {'form':form}
    if TestQuiz.question_id < len(TestQuiz.quiz_dto.questions):
        end = False
    elif TestQuiz.question_id == len(TestQuiz.quiz_dto.questions):
        end = True
    else:
        return result(request)
    questions = TestQuiz.quiz_dto.questions
    current_question = next(x for x in questions if x.uuid == TestQuiz.quiz_dto.uuid + '-' + str(TestQuiz.question_id))
    current_choices = (x for x in current_question.choices if current_question.uuid + '-' in x.uuid)
    return render(request, 'Quiz_app/QuestionPage.html', {'question': current_question,
                                                          'choices': current_choices,
                                                          'end': end})


def next_question(request):
    TestQuiz.question_id += 1
    return question(request)


def result(request):
    TestQuiz.question_id = 0
    return render(request, 'Quiz_app/ResultPage.html', {'score': TestQuiz.quiz_result_service.get_result()})
