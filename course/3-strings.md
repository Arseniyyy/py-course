## Введение:
Добро пожаловать на третью лекцию курса Python для начинающих! В предыдущих лекциях мы познакомились с основами Python, научились назначать переменные и работать с целыми и дробными числами. Теперь пришло время узнать больше о строках в Python!

В программировании строки являются одним из наиболее распространенных типов данных. В языке программирования Python строки являются мощным инструментом для работы с текстовыми данными. Они позволяют нам хранить, обрабатывать и манипулировать текстом на различные способы. В этой статье мы погрузимся в увлекательный мир строк в Python и исследуем различные методы, которые помогут нам работать с ними.

## Что такое строки в Python?
Строки в Python представляют собой последовательность символов, заключенных в одинарные или двойные кавычки. Например, "Привет, мир!" или 'Python - лучший язык программирования!'. Мы можем создавать строки, присваивать им значения, объединять их, разделять и выполнять множество других операций для работы с текстом.

## Создание и вывод строк:
Давайте начнем с создания строки. Для этого просто заключите текст в кавычки. Можно использовать одинарные или двойные кавычки. Вот пример:
```python
my_string = "Привет, мир!"
my_string = 'Привет, мир!'
print(my_string)  # Привет, мир!
```

## Операции со строками
К строкам можно применять некоторые стандартные операции:
```python
# Сложение
string1 = "I love "
string2 = "Python"

print(string1 + string2)  # I love Python

# Умножение
string = 'abc '
print(string * 3)  # abc abc abc
```
При умножении, строка просто повторяется указанное количество раз.

## Сравнение строк
Как и числа, строки можно сравнивать. Равенство строк не зависит от кавычек:
```python
# Сравним две строки на равенство
string1 = 'Equal'
string2 = "Equal"
string3 = '''equal'''

print(string1 == string2)  # Выведет True, так как две строчки равны, если в них все символы равны.
print(string1 == string3)  # False

# Теперь узнаем, какая строка больше
string1 = 'abc'
string2 = 'ac'

print(string1 > string2)  # False
```

Почему первая строка во втором примере оказалась меньше, ведь символов в ней больше, чем во второй? Когда строки сравниваются в Python, используется лексикографическое сравнение, то есть сравнение символов по их числовому значению в таблице символов Unicode.

В данном случае, когда мы сравниваем `abc` и `ac`, первые два символа у них одинаковые: `a`. Но следующий символ в первой строке `b` имеет большее числовое значение, чем символ второй строки `c`. Поэтому, сравнивая символы по очереди, мы можем сделать вывод, что `abc` будет идти перед `ac` в лексикографическом порядке.

Поэтому, выражение `abc` > `ac` возвращает `False`, так как `abc` не больше, а, наоборот, меньше `ac` в лексикографическом порядке.

Строки чувствительны к регистру:
```python
string_with_small_h = 'hello!'
string_with_capital_h = 'Hello!'

print(string_with_small_h == string_with_capital_h)  # False
```

## Символ перевода строки
Давайте представим, что у нас есть имена нескольких человек и мы хотим вывести каждое имя с новой строки. В таком случае, имеет смысл воспользоваться символом переноса строки: `\n`. Пример:
```python
print('Катя', 'Миша', 'Андрей', sep='\n')
```

Программа выведет:
```
Катя
Миша
Андрей
```

Данный код выводит три строки 'Катя', 'Миша' и 'Андрей' на отдельных строках. По умолчанию, `print()` разделяет значения пробелами и выводит их на одной строке. Однако, мы использовали аргумент `sep='\n'`, где `\n` представляет собой символ переноса строки.

Символ `\n` можно использовать самостоятельно, без аргументов:
```python
print('Катя', '\n', 'Андрей')
```
Вывод будет выглядеть так:
```
Катя
Андрей
```

## Индкесы
Индексы в строках Python - это числовые значения, которые назначаются каждому символу в строке. Они позволяют нам обращаться к отдельным символам или подстрокам внутри строки. Индексы начинаются с 0 для первого символа, 1 для второго символа и так далее.

Давай рассмотрим пример строки "Hello, Python!". Мы можем обратиться к каждому символу этой строки, используя его индекс. Например:
```python
string = "Hello, Python!"

print(string[0])  # Вернёт символ "H"
print(string[7])  # Вернёт символ "P"
print(string[13])  #Вернёт "!"
```

Мы также можем использовать отрицательные индексы для обратного доступа к символам строки. Например:
```python
string = "Hello, Python!"

print(string[-1])  # Вернёт "!"
print(string[-6])  # Вернёт "y"
```

Диапазоны индексов в строках Python позволяют нам получать подстроки из исходной строки, выбирая определенный диапазон символов. Синтаксис для задания диапазонов индексов выглядит следующим образом: `start:end:step`, где `start` - начальный индекс, `end` - конечный индекс, а `step` - частота выбора или по-другому -- шаг (рассмотрим позже).

Важно отметить, что конечный индекс в диапазоне не включается в выборку. Это означает, что символ с индексом `end` не будет включен в полученную подстроку.

Давайте рассмотрим пример на строке "Hello, Python!":
```python
string = "Hello, Python!"
substring = string[7:13]
print(substring)
```
В этом примере мы используем диапазон индексов `[7:13]`, чтобы получить подстроку "Python". Начальный индекс 7 указывает на символ "P", а конечный индекс 13 указывает на символ "n". Подстрока "Python" будет включать все символы, начиная с индекса 7 до индекса 12.

Мы также можем использовать необязательные значения начального или конечного индекса. Если мы не указываем начальный индекс, то диапазон начинается с самого начала строки. Если мы не указываем конечный индекс, то диапазон продолжается до конца строки. Например:
```python
substring1 = string[:5]  # Получаем подстроку "Hello"
substring2 = string[7:]  # Получаем подстроку "Python!"
```

В первом примере мы не указали начальный индекс, поэтому подстрока будет содержать символы с начала строки до индекса 4, не включая его. Во втором примере мы не указали конечный индекс, поэтому подстрока будет содержать символы с индекса 7 до конца строки.

Шаг (step) в индексации строк в Python является необязательным параметром и позволяет указать, с каким шагом извлекать символы из строки. Шаг определяет, через сколько символов будет выбран следующий символ.

Синтаксис для указания шага в индексации строк выглядит следующим образом: [начало:конец:шаг]. Шаг может быть положительным или отрицательным целым числом.

Если шаг положительный, то символы будут выбираться слева направо с указанным шагом.
Если шаг отрицательный, то символы будут выбираться справа налево с указанным шагом.
Примеры использования шага:

```python
text = "Hello, World!"

# Извлекаем символы с шагом 2
result = text[::2]
print(result)  # "HloWrd"

# Извлекаем символы с шагом -1 (в обратном порядке)
result = text[::-1]
print(result)  # "!dlroW ,olleH"

# Извлекаем символы с шагом 3, начиная с индекса 2 и до индекса 8
result = text[2:8:3]
print(result)  # "l,"

# Извлекаем символы с шагом -2, начиная с индекса 5 и до конца строки
result = text[5:: -2]
print(result)  # " Wrd"

# Извлекаем символы с шагом 1, начиная с индекса 3 и до индекса 10
result = text[3:10]
print(result)  # "lo, Wor"
```

Использование шага в индексации строк дает большую гибкость при извлечении символов и позволяет выбирать нужные нам подстроки с определенным шагом или в определенном порядке.

Теперь рассмотрим распространённую ошибку при работе с индексами. Попробуйте запустить этот код:
```python
string = 'Out'

print(string[3])
```
Вы увидите ошибку: `IndexError: string index out of range`. Попробуйте понять эту ошибку, воспользовавшись данной [ссылкой](https://rollbar.com/blog/python-indexerror-string-index-out-of-range/#:~:text=outside%20its%20range.-,What%20Causes%20IndexError%3A%20string%20index%20out%20of%20range,-This%20error%20occurs). Статья на английском языке, так что воспользуйтесь переводчиком. Если у вас не получится -- ничего страшного. Ниже будет дано объяснение.

## IndexError: string index out of range
Почему же возникает эта ошибка? Всё просто. Python нам говорит, что нет такого индекса в строке. А есть индексы 0, 1 и 2, так как строка состоит из трёх символов. Другими словами, мы пытаемся получить доступ к символу, которого в строке не существует.

## Методы строк
Python предоставляет множество встроенных методов для работы со строками.

В Python для многих задач существуют встроенные функции, которые предлагают быстрые решения. Вместо того, чтобы писать длинные программы, мы можем воспользоваться уже готовыми методами.

Эти функции называются методами. Методы можно применять к значениям, переменным или выражениям, указывая их после точки. Например, если у нас есть строка "котлета", мы можем использовать метод `.count('кот')`, чтобы посчитать, сколько раз подстрока "кот" встречается в данной строке.

### Метод `find()`
Метод find() в строках Python - это некая "шпионская лупа", которая помогает нам искать определенные части текста. Когда мы вызываем этот метод, он начинает расследование искомой подстроки внутри строки и возвращает нам первую позицию, где она была обнаружена.

Давай представим, что у нас есть строка "Hello, how are you?" и мы хотим найти слово "how". Метод find() выполняет свою секретную миссию, просматривает каждую букву строки и в конечном итоге выясняет, что "how" находится на позиции 7. Именно с буквы "h", которая находится на седьмой позиции, начинается слово "how", поэтому метод вернёт цифру 7:
```python
print("Hello, how are you?".find('how'))  # 7
```

Так что метод `find()` секретно сообщает нам индекс 7, где можно обнаружить эту подстроку.

Но вот загадка: что произойдет, если мы попробуем найти подстроку, которой нет в исходной строке? Вместо того, чтобы оставить нас в затруднении, метод `find()` делает следующий ход и возвращает значение -1, чтобы сказать нам: "Сорри, но этой подстроки тут нет!":
```python
string = 'Собака, лев, тигр'
print(string.find('кот'))  # -1
```

Несколько примеров:
```python
print('Вася нашёл раз котёнка,'.find('котё'))  # 15
print('От папы он спрятал его,'.find('кот'))  # -1
print('Кормил он кота колбасой,'.find('ко'))  #	10
print('Пока тот Васю не укусил.'.find('к'))  # 2
```

Все это дело делает метод `find()` мощным инструментом для работы с текстом, помогая нам разгадывать загадки и обнаруживать скрытые сокровища внутри строк.

### Метод `rfind()`
Метод `rfind()` в строках Python используется для поиска последнего вхождения заданной подстроки в строку. Он возвращает индекс первого символа последнего вхождения или -1, если подстрока не найдена.

Вот синтаксис метода rfind():
```
string.rfind(substring, start, end)
```
- `substring` - подстрока, которую мы ищем в строке.
- `start` (необязательный) - индекс, с которого начинается поиск. Если не указан, поиск будет производиться по всей строке.
end (необязательный) - индекс, на котором заканчивается поиск. Если не указан, поиск будет производиться до конца строки.

Давайте рассмотрим несколько примеров:
```python
print('Динозавр: ТОП-ТОП-ТОП!'.find('ТОП'))  # 10
print('Динозавр: ТОП-ТОП-ТОП!'.rfind('ТОП'))  # 18
print('Динозаврик: топ-топ-топ!'.find('топ'))  # 12
print('Динозаврик: топ-топ-топ!'.rfind('топ'))  # 20
```

Во втором примере метод `rfind()` возвращает индекс первого символа последнего вхождения подстроки в строку. То же самое происходит в четвёртом примере.

Метод `rfind()` полезен, когда нам нужно найти последнее вхождение подстроки в строке, особенно при работе с большими текстовыми данными или обработке журналов.

### Метод `count()`
В мире строк Python существует функция с волшебным именем `count()`. Она обладает невероятной способностью подсчитывать скрытые сокровища - количество вхождений подстроки в строку. Отправляйся с нами в увлекательное путешествие по числам и символам!

Вот как выглядит синтаксис этой функции:
```python
string.count(substring, start, end)
```
- `substring` - та таинственная подстрока, которую мы ищем в нашей строке.
- `start` (необязательный аргумент) - пункт отправления для нашего поиска. Если его пропустить, мы отправимся от самого начала строки.
- `end` (необязательный аргумент) - это место окончания нашего приключения. Если мы его упустим, путь приведет нас до самого конца строки.

Давайте познакомимся с этой функцией поближе через несколько примеров:
```python
print("Дракон: огонь-огонь!".count("огонь"))  # 2
print("Волшебство: абракадабра!".count("а"))  # 5
print("Секретный код: 12345678".count("7"))  # 1
```

В первом примере функция `count()` находит две подстроки "огонь" в строке "Дракон: огонь-огонь!". Она знает, как проникнуть в самые глубины строки и найти все вхождения.

Во втором примере функция `count()` считает четыре буквы "а" в строке "Волшебство: абракадабра!". Она умна и может различать регистр символов, поэтому каждая буква "а" будет учтена.

В третьем примере функция `count()` открывает секретный код "12345678" и находит одну семерку. Она точно знает, как найти редкие символы в огромном тексте.

Теперь давайте рассмотрим примеры с аргументами `start` и `end`:
- Подсчет количества букв "а" в первой половине строки:
```python
text = "абракадабра"
number_of_a = text.count("а", start=0, end=len(text) // 2)
print(number_of_a)  # Вывод: 2
```
Попробуйте самостоятельно найти информацию о функции `len()` в этой [статье](https://realpython.com/len-python-function/#:~:text=Remove%20ads-,Using%20len()%20With%20Built%2Din%20Sequences,-A%20sequence%20is).

- Подсчет количества слов в предложении, начиная с третьего символа:
```python
sentence = "Я люблю программирование на Python"
count_words = sentence.count(" ", start=2) + 1
print(count_words)  # 5
```

- Подсчет количества букв "о" в конце строки:
```python
text = "Hello, world!"
count_o = text.count("o", start=-3)
print(count_o)  # 0
```

Так что, когда нам понадобится узнать, сколько раз подстрока встречается в строке, функция `count()` будет нашим верным счетчиком, помогая нам обнаружить скрытые паттерны и сокровища. Она предоставляет нам магическую силу подсчета, чтобы мы могли покорить любые тайны строкового мира!

### Метод `replace()`
Метод `replace()` в языке программирования Python играет роль магического волшебника, который помогает нам заменить одни части строки на другие. Он позволяет создать новую строку, в которой все желаемые вхождения заданной подстроки будут заменены на новую подстроку, словно слова танцуют на своих местах.

У него есть свой уникальный синтаксис:
```python
string.replace(old, new, count)
```
- `old` - это загадочная подстрока, которую мы хотим вытеснить.
- `new` - это свежая искрящаяся подстрока, которой мы хотим заменить старую.
- `count` (необязательный аргумент) - это число, которое указывает сколько раз нужно совершить замену. Если оно не указано, то замена будет осуществлена для всех вхождений.

Давайте заглянем в некоторые примеры, чтобы узнать больше о волшебных возможностях метода `replace()`:
```python
text = "Привет, мир!"
new_text = text.replace("и", "е")
print(new_text)  # "Привет, мер!"

sentence = "Я люблю Python"
new_sentence = sentence.replace("люблю", "обожаю")
print(new_sentence)  # "Я обожаю Python"

message = "AAAAAA"
new_message = message.replace("A", "B", 3)
print(new_message)  # "BBBAAA" (Только первые три A заменены)
```

В первом примере метод `replace()` превращает все "и" в "е" в строке "Привет, мир!" и создает новую строку "Привет, мер!". Старые буквы подчиняются магии замены.

Во втором примере метод `replace()` заменяет первое вхождение слова "люблю" на слово "обожаю" в предложении "Я люблю Python". Это как смена настроения - одно слово уступает место другому.

В третьем примере метод `replace()` производит замену только первых трех "A" на "B" в строке "AAAAAA". Остальные "A" остаются нетронутыми, словно украденные сокровища.

Метод `replace()` - это наш верный спутник, который помогает нам легко менять части строки. Он полезен, когда мы хотим вносить изменения в текстовые данные или проводить маленькие магические акты волшебства со строками.

## Задачи:

### Верхний регистр
Давай создадим вместе программу, которая возьмет обычную строку и превратит ее в потрясающий капитализированный (переведённый в верхний регистр) текст, словно он возвышается над остальными. Наверняка вы заметили, что в теории к этому уроку не сказано, как перевести строку в верхний регистр. Вам предстоит сделать это самостоятельно. В этом вам поможет данная [ссылка](https://thehelloworldprogram.com/python/python-string-methods/#:~:text=Performing%20the%20.,of%20the%20characters%20to%20lowercase). Перейдите на этот сайт, воспользуйтесь переводчиком, чтобы прочитать текст, найдите нужный кусок кода, запустите его. Посмотрите, что выводится на экран. Используя полученные знания, решите задачу.

#### Формат ввода:
Строка.

#### Формат вывода:
Строка, полностью переведённая в верхний регистр.

#### Пример ввода:
```
Hello, Python!
```
#### Пример вывода:
```
HELLO, PYTHON!
```

### Сколько символов?
Напишите программу, которая принимает входные данные в виде строки и выводит количество символов в строке.

#### Формат ввода:
Строка

#### Формат вывода:
Количество символов в строке.

#### Пример ввода:
```
Привет!
```

#### Пример вывода:
`7`

### Каждый второй символ
Напишите программу, которая принимает входные данные в виде строки и выводит каждый второй символ из строки.

#### Формат ввода:
Строка.

#### Формат вывода:
Строка, состоящая только из вторых символов введённой строки.

#### Пример ввода:
```python
Everything is Python
```

#### Пример вывода:
```python
vrtigi yhn
```

### Строка вверх-ногами
Напишите программу, которая принимает входные данные в виде строки и выводит строку в обратном порядке.

#### Формат ввода:
Строка.

#### Формат вывода:
Введённая строка в обратном порядке.

#### Пример ввода:
```python
Я строка
```

#### Пример вывода:
```python
акортс Я
```

### Инициалы
Напишите программу, которая принимает входные данные в виде двух строк, содержащих полное имя человека. Сначала вводится имя, потом фамилия. Выведите на экран инициалы человека в формате "Фамилия, И.", где И - это первая буква имени.

#### Формат ввода:
Имя и фамилия. Каждое слово на новых строках.

#### Формат вывода:
Фамилия И.

#### Пример ввода:
```
Пётр Иванов
```

#### Пример вывода:
```
Иванов П.
```

### Куда подевались пробелы?
Напишите программу, которая принимает входные данные в виде строки, и выводит ее с удаленными пробелами.

#### Формат ввода:
Строка с пробелами.

#### Формат вывода:
Строка без пробелов.

#### Пример ввода:
```python
А где пробелы?
```
#### Пример вывода:
```python
Агдепробелы?
```

### Кто крадёт символы?
Напишите программу, которая принимает входные данные в виде строки и выводит первые три символа, последние три символа, а затем средний символ (строка всегда имеет нечетную длину).

#### Формат ввода:
Строка.

#### Формат вывода:
3 строки. Первая содержит первые 3 символа, вторая - последние 3 символа, а третья - символ посередине.

#### Пример ввода:
```
Кто крадёт символы?
```

#### Пример вывода:
```
Кто
лы?
т
```

### Сбой
В таинственном космическом агентстве произошёл небольшой сбой в программе управления роботами-исследователями. На каждом роботе записаны два числа, но их значения стерлись. Команде требуется твои навыки, чтобы восстановить эти числа и вычислить их сумму!

Тебе будут предоставлены две загадочные строки. В каждой из них спрятаны два числа, разделенные пробелом. Твоя задача — извлечь эти числа из строк, сложить их и сообщить команде полученную сумму.

После выполнения задания ты сможешь быть уверенным, что помог космическому агентству продолжить свои исследования!

#### Формат ввода:
Два числа, разделённые пробелом на двух разных строках.

#### Формат вывода:
Сумма всех чисел.

#### Пример ввода:
```
8 4
6 2
```

#### Пример вывода:
```
20
```

### Непереносимость слов
В сказочной стране Алфавитоляндии люди не переносят слово "нет" и отрицательные частицы: "не" и "ни". Но об этом не знают туристы, которые приезжают отдохнуть на солнечных пляжах этой страны. Помоги туристу исправить своё предложение. Каждое вхождение слова "нет" замени словом "да". "ни" и "не" должны быть заменены пустой строкой. Слова могут начинаться как с маленькой так и с заглавной буквы.

#### Формат ввода:
Предложение со словом "нет"

#### Формат вывода:
Изменённое предложение

#### Пример ввода 1:
```
Я не люблю пляж
```

#### Пример вывода:
```
Я люблю пляж
```

#### Пример ввода 2:
```
Нет, я не пойду на экскурсию сегодня
```

#### Пример вывода 2:
```
Да, я пойду на экскурсию сегодня
```


### Последнее и первое слово
Ты попал в таинственную локацию, где в каждой комнате есть загадочная запись на стене. Каждая запись представляет собой строку, а твоя задача - найти магические индексы, которые откроют тебе путь к следующей комнате. Магические индексы - это индексы первого и последнего вхождения определенного слова в строке. Подсказка: чтобы решить задачу, понадобится метод `index()`, информацию о котором вы можете прочитать [здесь](https://www.w3schools.com/python/ref_string_index.asp#:~:text=Definition%20and%20Usage).

Твоя задача - найти эти магические индексы и продолжить свое путешествие.

#### Формат ввода:
Предложение со словом, индексы которого надо найти, а также само слово

#### Формат вывода:
Два индекса, каждый на новой строке

#### Пример ввода 1:
```
чёрная комната, чёрная дверь
чёрная
```

#### Пример вывода 1:
0
16

#### Пример ввода 2:
```
Отгадай загадку: Что это такое - зелёное, на дереве растет и листьями шуршит?
зелёное
```

#### Пример вывода 2:
33
33

### Компьютерный вирус
Ты исследуешь странный компьютерный вирус, который "съедает" символы в текстовом файле. Вирус начинает съедать первый символ, затем последний, затем снова первый, и так далее, продолжая этот процесс. Тебе дана строка текста и число N, которое представляет собой количество символов, которые вирус "съел". Твоя задача - определить, какая часть текста осталась после того, как вирус "съел" N символов.

#### Формат ввода:
Строка и число N

#### Формат вывода:
Изменённая вирусом строка

#### Пример ввода 1:
```
Сегодня хороший день.
3
```

#### Пример вывода 1:
```
годня хороший день
```

#### Пример ввода 2:
```
Сегодня хороший день.
4
```

#### Пример вывода 2:
```python
годня хороший ден
```

### Скучное эссе
Вася пишет сообщение другу, но кажется, что оно немного скучное. Чтобы добавить больше эмоций, он решил удвоить все восклицательные знаки в своём сообщении. Тебе дана строка, содержащая сообщение. Твоя задача - вывести две строки. В первой строке должен быть итоговый результат после удвоения восклицательных знаков, а во второй строке должно быть указано количество восклицательных знаков, которое пришлось добавить.

#### Формат ввода:
Строка с эссе Васи

#### Формат вывода:
Две строки. В первой - итоговый текст с удвоенными восклицательными знаками, во второй - количество добавленных восклицательных знаков.

#### Пример ввода:
```
Как же я люблю лето! Это самое лучшее время года!
```

#### Пример вывода:
```
Как же я люблю лето!! Это самое лучшее время года!!
2
```

