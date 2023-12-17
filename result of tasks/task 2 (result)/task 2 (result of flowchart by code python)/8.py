number = input("please enter your number here: ")

number = int(number)

if number > 8 and number < 101:
    if int(number) % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("please enter your number between 9 and 100 only")
