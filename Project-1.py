# DESIGN A SIMPLE CALCULATOR WITH BASIC ARITHMETIC OPERATIONS [TASK-1]
num_1=float(input("Enter The First Number:\n"))
operator=input("Choose Operator(+,-,*,/,%,**):\n")
num_2=float(input("Enter The Second Number:\n"))
if operator=="+":
    print("Output:",num_1 + num_2)
elif operator=="-":
    print("Output:",num_1 - num_2)
elif operator=="*":
    print("Output:",num_1 * num_2)
elif operator=="/":
    print("Output:",num_1 / num_2)
elif operator=="%":
    print("Output:",num_1 % num_2)
elif operator=="**":
    print("Output:",num_1 ** num_2)
else:
    print("This Operation Is Invalid.")
    print("Please Choose Operators From The Given Above.")
