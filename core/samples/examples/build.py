from core.runner import Runner

runner = Runner()

examples = [
    ["Hello", "Hello"],
    ["i++", "i++"],
]

input_data = ["This", "is", "test", "data"]

out = runner.run_many(input_data)
runner.save_tests(out, input_data)
runner.save_examples(examples)
runner.build(indent=2)
print("[+] Done")
