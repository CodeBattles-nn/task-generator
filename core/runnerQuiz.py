import json

from core.dataclasses import Question, Quiz


class Runner:

    def __init__(self, name: str):
        self.name = name

    def export(self):
        questions = Question.magic_get()
        name = self.name

        quiz = Quiz(name, questions)
        serialized = {
            **quiz.serialize(),
            "version": 2
        }

        with open("build.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(serialized, ensure_ascii=False))

        with open("build_beautify.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(serialized, indent=2, ensure_ascii=False))
