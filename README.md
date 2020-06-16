# antlr4-first-try
Из около-дарта в питон

# Файлы
* Dart.g4 - грамматика
* DartCustomVisitor.py - посетитель, в котором происходит обработка dart кода
* input.dart - код на dart

# Выполнение
В терминале:
## Первое, что нужно сделать - активировать виртуальное окружение

### Windows (вместе с кавычками)
```
'env/Scripts/activate'
```

### Linux
```
source env/bin/activate
```

## Далее, передаем файл main.py интерпретатору с дополнительным аргументом - input.dart
```
python main.py input.dart
```
