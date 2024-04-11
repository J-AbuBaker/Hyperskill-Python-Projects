import random

number_friends = int(
    input("Enter the number of friends joining (including you):\n"))

if number_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for i in range(number_friends)}
    total_bill = int(input("\nEnter the total bill value:\n"))
    lucky_one = input(
        '\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_one == 'Yes':
        names = [key for key, value in friends.items()]
        lucky = random.choice(names)
        print(f"\n{lucky} is the lucky one!\n")
        for friend in friends:
            if friend == lucky:
                friends[friend] = 0
            else:
                friends[friend] = round(total_bill / (number_friends - 1), 2)

        print(friends)
    else:
        print("No one is going to be lucky")
        print({friend: round(total_bill / number_friends, 2)
                for friend in friends})
