run = True

while run:

    a = input()
    num = 0
    b = []

    if " " in a:
        b = [i for i in a.split()]
        for i in b:
            num += int(i)
        print(num)

    elif a == "/exit":
        print("Bye!")
        break

    elif a == "/help":
        print("The program calculates the sum of numbers")

    elif a == "":
        continue

    else:
        print(a)
