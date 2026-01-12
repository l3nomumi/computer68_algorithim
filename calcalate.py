def MainMenu():
    print("" \
    "Press Enter Q = Exit\n " \
    "C = calculate")
    inp = input(" : ")
    if(inp == "Q" or inp == "q"):
        exit
    elif(inp == "C" or inp == "c"):
        Calculate()
    else:
        MainMenu()


def Calculate():
    print("+ = Plus\n" \
    "- = Minus\n"\
    "* = Multiply\n"\
    "/ = Divide\n"\
    "** = Power\n"\
    "M = Main/Home")
    inp = input(": ")

    if(inp == "+"):
        inp = input("N : ")
        total = 0
        N = int(inp)
        for x in range(N):
            total += int(input("Number : "))
        print("Total = ", total)
        Calculate()
    elif(inp == "-"):
        inp = input("N : ")
        total = 0
        N = int(inp)
        for x in range(N-1):
            total -= int(input("Number: "))
        print("Total = ", total)
        Calculate()
    elif(inp == "*"):
        inp = input("N : ")
        total = 1
        N = int(inp)
        for x in range(N):
            total *= int(input("Number: "))
        print("Total = ", total)
        Calculate()
    elif inp == "/":
        N = int(input("N : "))
        total = float(input("Number : "))
        for _ in range(N - 1):
            num = float(input("Number : "))
            if num == 0:
                print("divide")
                Calculate()
                return
            total /= num
        print("Total =", total)
        Calculate()
    elif inp == "**":
        num = int(input("Number: "))
        print("total =", num ** 2)
    
    elif(inp == "M" or inp == "m"):
        MainMenu()
    else:
        Calculate()


MainMenu()