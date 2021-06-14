from .dto import *
from .services import QuizResultService


# 1-b;2-a;3-a;4-c,d;5-a,c - правильные ответы
class TestQuiz:
    question_id = 0
    choices: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-1-1",
            "Вещественная переменная",
            False
        ),
        ChoiceDTO(
            "1-1-2",
            "Целочисленная переменная",
            True
        ),
        ChoiceDTO(
            "1-1-3",
            "Логическая переменная",
            False
        ),
        ChoiceDTO(
            "1-1-4",
            "Символьная строка",
            False
        ),

        ChoiceDTO(
            "1-2-1",
            "Вещественная переменная",
            True
        ),
        ChoiceDTO(
            "1-2-2",
            "Целочисленная переменная",
            False
        ),
        ChoiceDTO(
            "1-2-3",
            "Логическая переменная",
            False
        ),
        ChoiceDTO(
            "1-2-4",
            "символьная строка",
            False
        ),

        ChoiceDTO(
            "1-3-1",
            "Логическая переменная",
            True
        ),
        ChoiceDTO(
            "1-3-2",
            "Целочисленная переменная",
            False
        ),
        ChoiceDTO(
            "1-3-3",
            "Вещественная переменная",
            False
        ),
        ChoiceDTO(
            "1-3-4",
            "Символьная строка",
            False
        ),

        ChoiceDTO(
            "1-4-1",
            "string",
            False
        ),
        ChoiceDTO(
            "1-4-2",
            "char",
            False
        ),
        ChoiceDTO(
            "1-4-3",
            "bool",
            True
        ),
        ChoiceDTO(
            "1-4-4",
            "float",
            True
        ),
        ChoiceDTO(
            "1-5-1",
            "PhP",
            True
        ),
        ChoiceDTO(
            "1-5-2",
            "C#",
            False
        ),
        ChoiceDTO(
            "1-5-3",
            "Ruby",
            True
        ),
        ChoiceDTO(
            "1-5-4",
            "AVR Assembly",
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

    answers: List[AnswerDTO] = []

    answers_dto = AnswersDTO(
        "1",
        answers
    )

