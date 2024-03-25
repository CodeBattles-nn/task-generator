# Task Generator

#### A framework for generating tasks in the CodeBattles platform.

## Usage

### Create the task
Enter into the console
```css
manager.py create {name} 
```

where {name} => the name of the task folder

A folder named {name} will be created in the **programs folder**

| Flag | Description                        |
|------|---------------------------------|
| -e   | Create the examples            |
| -f   | Generate metadata files     |

The flags should be after the task name.

### Configuration

Go to the folder with your task

- **- **main.py ** - A file with the solution of the problem (Answers will be generated based on it).
- **build.py ** - Settings and build file. To build a file for export, run this file.
- **meta** - Folder with metadata (Appears only if the -f flag is used).



#### Setting up input data

Let's take a look at the file **build.py ** file:

```python
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
```

To change the input data, change the *input_data variable*.

For example, a program is shown below that uses random 10 numbers (from 1 to 10000) to generate tests.

```python
from core.runner import Runner

runner = Runner()

examples = [
    ["10", "10"],
    ["1561", "1561"],
]

input_data = [random.randint(1, 10000) for i in range(10)]

out = runner.run_many(input_data)
runner.save_tests(out, input_data)
runner.save_examples(examples)
runner.build(indent=2)
print("[+] Done")
```

### Build
> To add a task to the CodeBattles website, you need to copy the **build file.json**


- Launch build.py to build the task.


The complete file of the built task (build.json).
```json
{
  "name": "",
  "description": "",
  "in": "",
  "out": "",
  "examples": [],
  "tests": [
    [
      "15",
      "30"
    ],
    [
      "13",
      "26"
    ]
  ]
}
```

___
When using different flags, the file structure may vary slightly

### Setting up metadata
For customization (name, description, etc...) Edit the files in the *meta* folder.
This folder is created only if you selected the **-f** flag when creating.

The structure of the metadata folder
```css
meta
├── description.txt
├── in_data.txt
├── name.txt
└── out_data.txt
```
