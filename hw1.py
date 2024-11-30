curentYear = 2024
birthYear = int(input("Enter your birth year: "))
print(f"Your age is {curentYear - birthYear}")

fleshGb = int(input("Enter amount of Gb on your flash stick: "))
print(f"You can install {(fleshGb * 1024) // 820} 820mb programs")

choise = int(input("Enter 0-9 number: "))
match choise:
    case 1:
        print("!")
    case 2:
        print("@")
    case 3:
        print("#")
    case 4:
        print("$")
    case 5:
        print("%")
    case 6:
        print("^")
    case 7:
        print("&")
    case 8:
        print("*")
    case 9:
        print("(")
    case 0:
        print(")")

year = int(input("Enter a year: "))
print("Leap year") if (year % 100 == 0 and year % 4 != 0) or year % 400 == 0  else print("Not leap year")


minimum = int(input("Enter minimum: "))
maximum = int(input("Enter maximum: "))
suma = 0
for num in range(minimum, maximum):
    suma += num
print(f"Suma of your range is {suma}")

number = int(input("Enter number: "))
count = 0
while number > 0:
        number //= 10
        count += 1
print(f"Number of digits {count}")


positiv = 0
negative = 0
odd = 0
even = 0
nulls = 0
numsStr = input("Enter 10 numbers with spaces (1 2 3 4 5 ...):")
nums = map(int, numsStr.split())
for i in nums:
    if i > 0: positiv += 1
    elif i == 0: nulls += 1
    else: negative += 1

    if i % 2 == 0: even += 1
    elif i % 2 == 1: odd += 1

print(f"Odds: {odd}")
print(f"Even: {even}")
print(f"Negative: {negative}")
print(f"Positive: {positiv}")
print(f"Nulls: {nulls}")
