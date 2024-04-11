number_friends = int(input("Enter the number of friends joining (including you):"))

if number_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(number_friends)]
    total_bill = int(input("\nEnter the total bill value:\n"))
    print({friend: round(total_bill / number_friends, 2) for friend in friends})