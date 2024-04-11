pencil_numbers = input('How many pencils would you like to use: ')

while True:
    if not pencil_numbers.isnumeric():
        print('The number of pencils should be numeric')
        pencil_numbers = input()
        continue
    elif pencil_numbers == '0':
        print('The number of pencils should be positive')
        pencil_numbers = input()
        continue
    else:
        break

p = input(f'Who will be first (John, Jack): ')
while True:
    if p != 'John' and p != 'Jack':
        print("Choose between 'John' and 'Jack'")
        p = input()
        continue
    else:
        break


pencil_numbers = int(pencil_numbers)

while True:
    print(pencil_numbers * ('|'))
    if p == 'Jack':
        print(f"{p}'s turn:")
        p = 'John'
        if pencil_numbers % 4 == 0:
            print('3')
            pencil_numbers -= 3
        elif pencil_numbers % 4 == 3:
            print('2')
            pencil_numbers -= 2
        elif pencil_numbers % 4 == 2:
            print('1')
            pencil_numbers -= 1
        elif pencil_numbers % 4 == 1:
            print('1')
            pencil_numbers -= 1
        elif pencil_numbers == 1:
            print('1')
            pencil_numbers -= 1
        if pencil_numbers <= 0:
            print(f'{p} won!')
            break

    else:
        print(f"{p}'s turn!")
        p = 'Jack'
        while True:
            taken = input()
            if not taken.isnumeric():
                print("Possible values: '1', '2' or '3'")
                continue
            elif int(taken) != 1 and int(taken) != 2 and int(taken) != 3:
                print("Possible values: '1', '2' or '3'")
                continue
            elif int(taken) > pencil_numbers:
                print('Too many pencils were taken')
                continue
            else:
                break
        pencil_numbers -= int(taken)
        if pencil_numbers <= 0:
            print(f'{p} won!')
            break
