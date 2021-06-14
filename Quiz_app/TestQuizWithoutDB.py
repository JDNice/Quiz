from .dto import *
from .services import QuizResultService
from typing import List, NamedTuple

from Quiz_app.services import QuizResultService

# 1-b;2-a;3-a;4-c,d;5-a,c - правильные ответы
class TestQuiz:
    question_id = 0
    choices: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-1-1",
            "A. Вещественная переменная",
            False
        ),
        ChoiceDTO(
            "1-1-2",
            "B. Целочисленная переменная",
            True
        ),
        ChoiceDTO(
            "1-1-3",
            "C. Логическая переменная",
            False
        ),
        ChoiceDTO(
            "1-1-4",
            "D. Символьная строка",
            False
        ),

        ChoiceDTO(
            "1-2-1",
            "A. Вещественная переменная",
            True
        ),
        ChoiceDTO(
            "1-2-2",
            "B. Целочисленная переменная",
            False
        ),
        ChoiceDTO(
            "1-2-3",
            "C. Логическая переменная",
            False
        ),
        ChoiceDTO(
            "1-2-4",
            "D. Символьная строка",
            False
        ),

        ChoiceDTO(
            "1-3-1",
            "A. Логическая переменная",
            True
        ),
        ChoiceDTO(
            "1-3-2",
            "B. Целочисленная переменная",
            False
        ),
        ChoiceDTO(
            "1-3-3",
            "C. Вещественная переменная",
            False
        ),
        ChoiceDTO(
            "1-3-4",
            "D. Символьная строка",
            False
        ),

        ChoiceDTO(
            "1-4-1",
            "A. string",
            False
        ),
        ChoiceDTO(
            "1-4-2",
            "B. char",
            False
        ),
        ChoiceDTO(
            "1-4-3",
            "C. bool",
            True
        ),
        ChoiceDTO(
            "1-4-4",
            "D. float",
            True
        ),
        ChoiceDTO(
            "1-5-1",
            "A. PhP",
            True
        ),
        ChoiceDTO(
            "1-5-2",
            "B. C#",
            False
        ),
        ChoiceDTO(
            "1-5-3",
            "C. Ruby",
            True
        ),
        ChoiceDTO(
            "1-5-4",
            "D. AVR Assembly",
            False
        ),
    ]

    questions: List[QuestionDTO] = [
        QuestionDTO(
            "1-1",
            "1. Переменная int:",
            choices
        ),
        QuestionDTO(
            "1-2",
            "2. Переменная float:",
            choices
        ),
        QuestionDTO(
            "1-3",
            "3. Переменная bool:",
            choices
        ),
        QuestionDTO(
            "1-4",
            "4. Типы переменных в Python(выбрать несколько вариантов):",
            choices
        ),
        QuestionDTO(
            "1-5",
            "5. Какие из языков являются скриптовыми?(выбрать несколько вариантов):",
            choices
        ),
    ]

    quiz_dto = QuizDTO(
        "1",
        "Программирование для начинающих",
        questions
    )

    answers: List[AnswerDTO]=[]

    answers_dto = AnswersDTO(
        "1",
        answers
    )

