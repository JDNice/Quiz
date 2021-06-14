from django.shortcuts import render
from .models import Quiz, MultipleChoice, MultipleChoiceAnswer
from .services import *
from .TestQuizWithoutDB import *
from .forms import AnswerForm


def start(request):
    quiz = TestQuiz.quiz_dto
    return render(request, 'Quiz_app/StartScreen.html', {'quizname': quiz.title})


def question(request):
    if request.method == 'POST':
        if 'answer' in request.POST:
            TestQuiz.question_id += 1
            answers = request.POST.getlist('answer')
            answered_question = request.POST['c_question']
            TestQuiz.answers_dto.answers.append(AnswerDTO(answered_question, answers))
    if TestQuiz.question_id < len(TestQuiz.quiz_dto.questions):
        end = False
    elif TestQuiz.question_id == len(TestQuiz.quiz_dto.questions)-1:
        end = True
    else:
        return result(request)

    current_question = TestQuiz.quiz_dto.questions[TestQuiz.question_id]
    current_choices = (x for x in current_question.choices if current_question.uuid + '-' in x.uuid)

    return render(request, 'Quiz_app/QuestionPage.html', {'question': current_question,
                                                          'choices': current_choices,
                                                          'end': end})


def result(request):

    TestQuiz.question_id = 0
    qrs = QuizResultService(TestQuiz.quiz_dto, TestQuiz.answers_dto)
    print(TestQuiz.answers)
    score = qrs.get_result() * 100
    print(score)
    TestQuiz.answers_dto = AnswersDTO("1", [])
    return render(request, 'Quiz_app/ResultPage.html', {'score': score})
