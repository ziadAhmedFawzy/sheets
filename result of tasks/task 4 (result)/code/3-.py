salary = int(input("enter your salary here : "))
ser_by_year = int(input("enter your years of services here : "))
bonus = 8

if ser_by_year > 7:
    bonus_of_salary = salary * (bonus / 100)
    salary = salary + bonus_of_salary
    print("your salary after bonus is : ", salary)
