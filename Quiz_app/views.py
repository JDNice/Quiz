from django.shortcuts import render
from .models import Quiz, MultipleChoice, MultipleChoiceAnswer
from .services import *
from .TestQuizWithoutDB import *
from .forms import AnswerForm


def start(request):
    quiz = TestQuiz.quiz_dto
    TestQuiz.question_id = 1
    TestQuiz.answers = []
    return render(request, 'Quiz_app/StartScreen.html', {'quizname': quiz.title})


def question(request):
    if request.method == 'POST':
        if 'answer' in request.POST :
            TestQuiz.question_id += 1
            answers = request.POST.getlist('answer')
            answered_question = request.POST['c_question']
            TestQuiz.answers.append(AnswerDTO(answered_question,answers))
    if TestQuiz.question_id < len(TestQuiz.quiz_dto.questions):
        end = False
    elif TestQuiz.question_id == len(TestQuiz.quiz_dto.questions):
        end = True
    else:
        return result(request)
    questions = TestQuiz.quiz_dto.questions
    current_question: QuestionDTO
    for q in questions:
        if q.uuid == TestQuiz.quiz_dto.uuid+'-'+str(TestQuiz.question_id):
            current_question=q
            break
    current_choices = (x for x in current_question.choices if current_question.uuid + '-' in x.uuid)
    return render(request, 'Quiz_app/QuestionPage.html', {'question': current_question,
                                                          'choices': current_choices,
                                                          'end': end})


def result(request):
    TestQuiz.question_id = 0
    qrs = QuizResultService(TestQuiz.quiz_dto,TestQuiz.answers_dto)
    score = qrs.get_result()
    print(TestQuiz.answers)
    TestQuiz.answers =[]
    return render(request, 'Quiz_app/ResultPage.html', {'score': score})
