# Тема 1. Работа с Git.
Отчёт по теме #1 выполнил:
- Исаков Степан Юрьевич
- ИВТ-23-1

| Задание | Лаб_раб |
| ------- | ------- |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |
| Задание 11 | + |
| Задание 12 | + |
| Задание 13 | + |
| Задание 14 | + |
| Задание 15 | + |

Знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_1.png)

## Выводы.
Git успешно установлен.

## Лабораторная работа №2
### Настройка.

``` git
git config --global user.name "IsakovStepan"

git config --global usermail "sunlessvl@outlook.com"

git config --list
```

### Результат.
![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_2.png)

## Выводы.
Установлено имя и почта пользователя, успешно пройдена проверка.

## Лабораторная работа №3
### Создание репозитория.

``` git
cd /Users/haahahhah/Software_Engineering/

git init
```

### Результат.
![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_3.png)

## Выводы.
Создан пустой репозиторий по указанному пути.

## Лаборторная работа №4
### Подготовка файлов.
``` git
git add proba.txt

git status
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_4.png)

## Выводы.
proba.txt подготовлен к комиту.
## Лаборторная работа №5
### Фиксация изменений.
``` git
git commit -m "Первый коммит"

git log -n 5

git log --oneline
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_5.png)

## Выводы.
Коммит осуществляется через команду git commit -m с комментарием. 
## Лаборторная работа №6
### Удалённый репозеторий.
``` git
git pull origin main

git stash

git stash apply

git stash pop
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_6.png)

## Выводы.
С помощью git remote add можно связать локальный репозиторий гит с удаленным репозиторием GitHub.
## Лаборторная работа №7
### Ветвление.
``` git
git branch TestBranch

git checkout TestBranch

git merge faeture
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_7.png)

## Выводы.
Через команду git branch происходит ветвление. Для работы с ветками необходимо провести checkout.
## Лаборторная работа №8
### Фетч
``` git
git fetch https://github.com/IsakovStepan/SoftwareEngineering
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_8.png)

## Выводы.
Фетч позволяет проверить конфликтность перед слиянием или преобразованием. 
## Лаборторная работа №9
### Удаление локальных и удалённых репозиториев, веток и файлов.
``` git
git branch -d TestBranch
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_9.png)

## Выводы.
Один из способов удалить файл или ветку.
## Лаборторная работа №10
### Отслеживание изменений в коммитах.
``` git
git log

git diff
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_10.png)

## Выводы.
Можно отслеживать изменения через команды log и diff.
## Лаборторная работа №11
### Возвращение файла в изначальное состояние.
``` git
git checkout main --testfile.txt

git commit -m "Восстановление файла к предыдущему состоянию"
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_11.png)

## Выводы.
Команда git checkout main --path заменит текущую версию файла на состояние из указанного коммита
## Лаборторная работа №12
### Возвращение к предыдущему коммиту.
``` git
git reser --soft HEAD^
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_12.png)

## Выводы.
## Лаборторная работа №13
### Установка.
``` git
git commit --amend
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_13.png)

## Выводы.
--amend открывает редактор
## Лаборторная работа №14
### Разрешение конфликтов при слиянии
``` git
git merge TestBranch1

git add testfile.txt

git commit

git merge Test Branch1

git branch -d TestBranch1
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_14.png)

## Выводы.
Чтобы решить конфликты при слиянии нужно:
1. Запустить команду слияния
2. Открыть файлы с конфликтами с помощью метки HEAD и 'имя_ветки'
3. Разрешить конфликты
4. Продолжить операцию слияния
5. Завершить слияние
## Лаборторная работа №15
### .gitignore
``` git
*.log
node_modules/
.env
temp/*
```

### Результат.
![!Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_1/pic/Tema_1_15.png)

## Выводы.
С помощью .gitignore можно исключить ненужные файлы, сократить размер репозитория, улучшить безопасность и сохранить чистоту репозитория.
