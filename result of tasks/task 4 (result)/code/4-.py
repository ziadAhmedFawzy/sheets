age1 = int(input("please enter your age1 : "))
age2 = int(input("please enter your age2 : "))
age3 = int(input("please enter your age3 : "))

if age1 > age2 and age1 > age3:
    print("the oldest is", age1)
elif age2 > age1 and age2 > age3:
    print("the oldest is", age2)
else:
    print("the oldest is", age3)

if age1 < age2 and age1 < age3:
    print("the youngest is", age1)
elif age2 < age1 and age2 < age3:
    print("the youngest is", age2)
else:
    print("the youngest is", age3)
