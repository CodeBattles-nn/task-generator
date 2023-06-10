# TaskGeneratorFramework

#### This program generate tests for CodeBattles problems

## Usage

### Create problem

```commandline
manager.py create {name}
```

Where {name} => name of problem

Folder with name {name} will be created in folder programs

### Configure tests

Go to the folder with you problem

- **main.py** - File with you program
- **tests.py** - Test file. For generate tests for CodeBattles database run it

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

### How get a tests as file
For add test to CodeBattles database test must be in json format.

- Run tests.py to export data. 
- *out.json* and *out_beautiful.json* files was created

*out.json*
```json
[["This", "This"], ["is", "is"], ["test", "test"], ["data", "data"]]
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