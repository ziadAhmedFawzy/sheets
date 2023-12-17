total_classes = int(input("enter your classes held : "))
classes_attended = int(input("enter your classes attended : "))

percent_classes_attended = int((classes_attended / total_classes) * 100)

if percent_classes_attended > 75:
    print("you are allow to sit in exam")
else:
    print("you are not allow to sit in exam")
