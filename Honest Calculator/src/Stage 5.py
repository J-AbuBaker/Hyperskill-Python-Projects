msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
messages = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5,
            msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
operator = ['*', '-', '+', '/']
memory = 0


def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7

    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    user_input = input()
    x, oper, y = user_input.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    try:
        x, y = float(x), float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in operator:
        print(msg_2)
        continue
    else:
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        else:
            try:
                result = x / y
            except ZeroDivisionError:
                print(msg_3)
                continue
    print(result)
    print(msg_4)
    answer0 = input()
    if answer0 == 'y':
        if is_one_digit(result):
            msg_index = 10
            while True:
                print(messages[msg_index])
                answer2 = input()
                if answer2 == 'y':
                    if msg_index < 12:
                        msg_index += 1
                        continue
                    else:
                        memory = result
                        break
                if answer2 == 'n':
                    break
        else:
            memory = result
    elif answer0 == 'n':
        pass
    print(msg_5)
    answer1 = input()
    if answer1 == 'y':
        continue
    if answer1 == 'n':
        break
