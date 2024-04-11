msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

operator = ['*', '-', '+', '/']
memory = 0

while True:
    print(msg_0)
    user_input = input()
    x, oper, y = user_input.split()
    if x == 'M':
        x = memory
    elif y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in operator:
        print(msg_2)
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
      result = x * y
    elif oper == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print(msg_3)
        continue
    print(float(result))
    print(msg_4)
    answer = input()
    if answer == 'y':
        memory = result
    elif answer == 'n':
        pass
    print(msg_5)
    ans = input()
    if ans == 'y':
        continue
    elif ans == 'n':
        break
