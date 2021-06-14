from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        if self.quiz_dto.uuid == self.answers_dto.quiz_uuid:  # проверка, что ответы для нужного теста
            right_answers = 0
            for answer in self.answers_dto.answers:
                for question in self.quiz_dto.questions:
                    if answer.question_uuid == question.uuid:  # нашли нужный вопрос
                        choosen_variants = answer.choices
                        needed_variants = []
                        for choice in question.choices:
                            if choice.is_correct and answer.question_uuid + '-' in choice.uuid:
                                needed_variants.append(choice.uuid)
                        if choosen_variants == needed_variants:
                            right_answers += 1
            return right_answers / len(self.quiz_dto.questions)
        else:
            return 0
