from typing import Any, List


class Question:
    __static_id = 0
    __collection = []

    def __init__(self, question: str, answers: List[Any], correct_answers: List[Any]):
        self.id = Question.__static_id
        self.question = question
        self.answers = answers
        self.correct_answers = correct_answers

        Question.__static_id += 1

        Question.__collection.append(self)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'question': self.question,
            'answers': self.answers,
            'correct_answers': self.correct_answers,
            "type": "select"
        }

    @classmethod
    def magic_get(cls) -> list:
        return Question.__collection


class Quiz:
    def __init__(self, name: str, questions: List[Question]):
        self.name = name
        self.questions = questions

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'questions': list(map(lambda question: question.serialize(), self.questions)),
            'type': "quiz"
        }
