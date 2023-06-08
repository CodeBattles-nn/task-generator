from core.runner import Runner

runner = Runner()

input_data = ["This", "is", "test", "data"]

out = runner.run_many(input_data)
runner.save_to_out(out, input_data)
