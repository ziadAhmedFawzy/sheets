n1 = input("please enter your first number: ")
n2 = input("please enter your second number: ")
n3 = input("please enter your third number: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print("the biggest number is", n1)
elif n2 > n1 and n2 > n3:
    print("the biggest number is", n2)
else:
    print("the biggest number is", n3)
