# TaskGeneratorFramework

#### This program generate tests for CodeBattles problems

## Usage

### Create problem

```commandline
manager.py create {name} 
```

Where {name} => name of problem

Folder with name {name} will be created in folder programs

| Flag | Description                     |
|------|---------------------------------|
| -e   | Problem examples generated      |
| -f   | Full folder with metadata files |

Flags must be after name

### Configuration

Go to the folder with you problem

- **main.py** - File with you program
- **build.py** - Test file. For generate tests for CodeBattles database run it
- **meta** - folder with problem`s metadata (Only if use -f flag on create)

#### How to configure input data

Let`s see to a tests.py file

```python
from core.runner import Runner

runner = Runner()

input_data = ["This", "is", "test", "data"]

out = runner.run_many(input_data)
runner.save_tests(out, input_data)

```

For change input data change a *input_data* variable.
For example, random 10 test with random nums in stdin

```python
import random

from core.runner import Runner

runner = Runner()

input_data = [random.randint(1, 10000) for i in range(10)]

out = runner.run_many(input_data)
runner.save_tests(out, input_data)

```

### Build

For add problem to CodeBattles database test must be in json format.

- Run build.py to export data.
- *out.json* and *out_beautiful.json* files was created (in build folder)

*out.json*

```json
[
  [
    "This",
    "This"
  ],
  [
    "is",
    "is"
  ],
  [
    "test",
    "test"
  ],
  [
    "data",
    "data"
  ]
]
```

This out may be added in database

*out_beautiful.json*

```json
[
  [
    "This",
    "This"
  ],
  [
    "is",
    "is"
  ],
  [
    "test",
    "test"
  ],
  [
    "data",
    "data"
  ]
]
```

Full build file (build.json)
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
If you are used flags build folder can contain other files 

### Configure metadata
For configure problem (set name, description...) edit files in folder meta.
This folder creates if you are create problem with flag **-f**

Meta folder
```
meta
| - description.txt
| - in_data.txt
| - name.txt
| - out_data.txt
```