# TaskGeneratorFramework

#### Программа для генерации задач в систему CodeBattles  

## Использование

### Создать задачу
вводим в консоль
```commandline
manager.py create {name} 
```

где {name} => название папки с  задачей

Папка с именем {name} будет создана в папке **programs**

| Флаг | Описание                        |
|------|---------------------------------|
| -e   | Генерировать примеры            |
| -f   | Генерировать файлы метадаты     |

Флаги должны быть после названия задачи

### Конфигурация

Перейдите в папку со своей задачей

- **main.py** - Файл с решением задачи (На его основе будут генерироаться ответы)
- **build.py** - Файл настроек и сборки. Для сборки файла для экспорта запустите этот файл
- **meta** - Папка с метаданными (Появляется только если используется флаг -f)

#### Настройка входных данных

Давайте посмотрим на файл **build.py** файл

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

Для изменения входных данных измините перменную *input_data*

Для примера внизу показана программа, которая использует для генерации тестов случайные 10 чисел (от 1 до 10000)

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

### Сборка
> Для добавления задачи на сайт CodeBattles нужно скопировать файл **build.json**


- Запустите build.py для сборки задачи.


Полный файл собранной задачи (build.json)
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
При использовании различных флагов структура файлов может немного отличаться

### Настройка метаданных
Для настройки (имени, описания и т.д...) Измените файлы в папке *meta*.
Эта папка создается только если вы выбрали флаг **-f** при создании

структура папки с методанными
```
meta
| - description.txt
| - in_data.txt
| - name.txt
| - out_data.txt
```
