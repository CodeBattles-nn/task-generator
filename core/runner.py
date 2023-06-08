import json
import subprocess


class Runner:

    def __init__(self, running=None):
        if running is None:
            running = ['python', 'main.py']
        self.running_command = running

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
        out = []
        for i in input_data:
            out.append(self.run(i))

        return out

    def save_to_out(self, out, inp):
        to_file = []

        if isinstance(out, str):
            inp = str(inp)
            to_file.append((inp, out))

        else:
            inp = map(str, inp)
            to_file = list(zip(inp, out))

        with open("out.json", "w+") as f:
            f.write(json.dumps(to_file))

        with open("out_beautiful.json", "w+") as f:
            f.write(json.dumps(to_file, indent=2))
