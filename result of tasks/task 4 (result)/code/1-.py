n1 = int(input("enter num1 :"))
n2 = int(input("enter num2 :"))
n3 = int(input("enter num3 :"))

if n1 > n2 and n1 > n3:
    print(n1, "is greatest")
elif n2 > n1 and n2 > n3:
    print(n2, "is greatest")
else:
    print(n3, "is greatest")

if n1 < n2 and n1 < n3:
    print(n1, "is smallest")
elif n2 < n1 and n2 < n3:
    print(n2, "is smallest")
else:
    print(n3, "is smallest")
