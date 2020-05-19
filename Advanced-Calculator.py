# Advanced Calculator Project


# Functions to run calculator:

def engine(a_list):
    num = int(a_list[0])
    for i, j in enumerate(a_list):
        if "-" in j and j.endswith("-"):
            if j.count("-") % 2 == 0:
                num += int(a_list[i + 1])
            else:
                num -= int(a_list[i + 1])
        if "+" in j:
            num += int(a_list[i + 1])
    return num


# Running the calculator:

run = True

while run:

    a = input()
    b = []

    if " " in a:
        b = [i for i in a.split()]
        print(engine(b))

    elif a == "/exit":
        print("Bye!")
        break

    elif a == "/help":
        print("The program adds and subtracts numbers")

    elif a == "":
        continue

    else:
        print(a)
