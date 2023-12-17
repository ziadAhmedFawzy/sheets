t = int(input("pleas enter temp : "))

cel_or_fer = input("if your temperature is celsius write (C) or fahrenheit write (f): ")

if cel_or_fer.lower() == "c":
    f = t * (9 / 5) + 32
    print(f)
elif cel_or_fer.lower() == "f":
    c = (t - 32) * 5/9
    print(c)
else:
    print("enter c or f only..")
