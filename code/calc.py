print("*"*10, " Calculator", "*"*10)
print("Enter q as a sign for exit")
while True:
    s = input("Sign (+, -, *, /): ")
    if s == 'q': break
    if s in ('+', '-', '*', '/'):
        x = float(input("Input 1st sign> "))
        y = float(input("Input 2nd sign> "))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y!=0:
                print("%.2f" % (x/y))
            else:
                print("Division by zero!")
    else:
        print("Incorrect input")
