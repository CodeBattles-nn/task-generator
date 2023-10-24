import json
import os
import subprocess

from core.printUtil import clear_print


class Runner:

    def __init__(self, running=None):
        if running is None:
            running = ['python', 'main.py']
        self.running_command = running
        self.examples = []
        self.tests = []

    def run(self, input_data):
        process = subprocess.Popen(self.running_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, universal_newlines=True)

        process.stdin.write(f"{input_data}\n")
        process.stdin.flush()
        new_line_counter = 0
        buffer = []
        while new_line_counter <= 3:
            text = process.stdout.readline()
            buffer.append(text)
            new_line_counter += len(text.strip()) == 0

        stdout = "\n".join(buffer).strip()

        return stdout

    def run_many(self, input_data):
        print("[/] Tests are running")
        out = []
        for i, stdin_text in enumerate(input_data):
            out.append(self.run(stdin_text))
            clear_print(f"{i + 1}/{len(input_data)}",)

        print()
        print("[+] Tests was built")

        return out

    def save_tests(self, out, inp):
        self.try_create_dir("build")
        to_file = []

        if isinstance(out, str):
            inp = str(inp)
            to_file.append((inp, out))

        else:
            inp = map(str, inp)
            to_file = list(zip(inp, out))

        with open("build/tests.json", "w+") as f:
            f.write(json.dumps(to_file))

        with open("build/tests_beautiful.json", "w+") as f:
            f.write(json.dumps(to_file, indent=2))

        self.tests = to_file

    def save_examples(self, to_file):
        self.try_create_dir("build")

        with open("build/examples.json", "w+") as f:
            f.write(json.dumps(to_file))

        with open("build/examples_beautiful.json", "w+") as f:
            f.write(json.dumps(to_file, indent=2))

        self.examples = to_file

    def try_create_dir(self, name):
        try:
            os.mkdir(name)
        except:
            pass

    def try_open_file(self, name, mode="r"):
        try:
            with open(name, mode) as f:
                return f.read()
        except Exception as e:
            print(e)
            return ""

    def build(self, indent=None):

        print("[/] Building export")

        name = self.try_open_file("meta/name.txt")
        description = self.try_open_file("meta/description.txt")
        in_data = self.try_open_file("meta/in_data.txt")
        out_data = self.try_open_file("meta/out_data.txt")

        to_export = {
            "name": name,
            "description": description,
            "in": in_data,
            "out": out_data,
            "examples": self.examples,
            "tests": self.tests
        }

        with open("build.json", "w+") as f:
            f.write(json.dumps(to_export, indent=indent))

        print("[+] Export was built")
