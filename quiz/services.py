from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        # your code here
        # найти количество правильных ответов
        if self.quiz_dto.uuid == self.answers_dto.quiz_uuid:
            right_answers = 0
            for question in self.quiz_dto.questions:
                for answer in self.answers_dto.answers:
                    if question.uuid == answer.question_uuid:
                        right_choices_counter = 0
                        right_choices_amount = 0
                        for choice in question.choices:
                            if choice.is_correct:
                                right_choices_amount += 1
                                if choice.uuid in answer.choices:
                                    right_choices_counter += 1
                        if right_choices_counter == right_choices_amount:
                            right_answers += 1
            return right_answers / len(self.quiz_dto.questions)
        else:
            return 0

        # к-во правильных ответов/кол-во вопросов
