msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
operation_sign = ['+', '-', '*', '/']


def check_if_numbers(N1, N2):
    try:
        float(N1)
        float(N2)
    except ValueError:
        return True
    else:
        return False


while True:
    print(msg_0)
    user_input = input().split()
    oper = user_input[1]
    N1 = user_input[0]
    N2 = user_input[2]
    result_of_exception = check_if_numbers(N1, N2)
    if result_of_exception is False:
        if oper in operation_sign:
            break
        else:
            print(msg_2)
    else:
        print(msg_1)
