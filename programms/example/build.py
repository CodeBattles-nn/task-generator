import random

from core.runner import Runner

runner = Runner()

examples = [
    ["1\n5", "5"],
    ["-5\n10", "-50"],
]

input_data = []

for i in range(20):
    a = random.randint(-10 ** 5, 10 ** 5)
    b = random.randint(-10 ** 5, 10 ** 5)
    input_data.append(f"{a}\n{b}")

out = runner.run_many(input_data)
runner.save_tests(out, input_data)
runner.save_examples(examples)
runner.build(indent=2)
print("[+] Done")
