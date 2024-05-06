from core.dataclasses import Question
from core.runnerQuiz import Runner

NAME = "Сложный квиз"

question_1 = Question(
    question="Сколько будет 5+5?",
    answers=[
        1,
        10,
        11,
        4,
    ],
    correct_answers=[10]
)

question_2 = Question(
    question="Почему канализационные люки круглые?",
    answers=[
        "Так их проще делать",
        "Это заговор",
        "Для того, чтобы они не упали внутрь себя",
    ],
    correct_answers=[
        "Для того, чтобы они не упали внутрь себя",
    ]
)

runner = Runner(name=NAME)
runner.export()
