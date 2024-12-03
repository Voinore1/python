# 1
text = input("Введіть рядок: ")
cleanInput = ''.join(text.split()).lower()
inputList = list(cleanInput)
inputList.reverse()
reversedInput = ''.join(inputList)

if cleanInput == reversedInput:
    print("Цей рядок є паліндромом.")
else:
    print("Цей рядок не є паліндромом.")

# 2
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (4, 5, 8, 9)

sameElements = []

for element in tuple1:
    if element in tuple2 and element in tuple3:
        sameElements.append(element)

print("Спільні елементи:", sameElements)

# 3

text = input("Введіть текст: ")
reservedWordstr = input("Введіть зарезервовані слова: ")
reservedWords = []

for word in reservedWordstr.split(' '):
    text = text.replace(word, word.upper())


print("Змінений текст:", text)