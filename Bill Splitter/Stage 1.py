# write your code here
number_of_friends = int(
    input('Enter the number of friends joining (including you):\n'))
print()
if number_of_friends <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend(including you), each on a new line:')
    friends = {input(): 0 for _ in range(number_of_friends)}
    print()
    print(friends)
