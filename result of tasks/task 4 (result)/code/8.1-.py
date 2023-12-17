num_of_deg = int(input("Enter the number of degrees : "))
count = 0
while count < num_of_deg:
    degree = int(input("please enter your degree : "))
    if degree > 80:
        print(f"{degree} : A")
    elif degree <= 80 and degree > 60:
        print(f"{degree} : B")
    elif degree <= 60 and degree > 50:
        print(f"{degree} : C")
    elif degree <= 50 and degree > 45:
        print(f"{degree} : D")
    elif degree <= 45 and degree > 25:
        print(f"{degree} : E")
    else:
        print(f"{degree} : F")
    count = count + 1
