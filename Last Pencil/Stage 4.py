pencil = input("How many pencils\n")

while not pencil.isnumeric() or pencil == "0":
    if not pencil.isnumeric():
        print("The number of pencils should be numeric")
        pencil = input()
    if pencil == "0":
        print("The number of pencils should be positive")
        pencil = input()   
        
remained_pencils = int(pencil)

user_name = input("who will be the first (John, Jack)\n").capitalize().strip()

while user_name != "John" and user_name != "Jack":
    print("Choose between 'John' and 'Jack'")
    user_name = input()

print(remained_pencils * "|")
if user_name == "John":
    print(f"{user_name}'s turn!")
    user_name = "Jack"
else:
    print(f"{user_name}'s turn!")
    user_name = "John"


while remained_pencils != 0:

    pencil = input()
    while pencil.isalpha() or pencil > "3" or pencil <= "0":
        print("Possible values: '1', '2' or '3'")
        pencil = input()
        
    if remained_pencils < int(pencil):
        print("Too many pencils were taken")
        pencil = input()
        
    remained_pencils -= int(pencil)
    if remained_pencils != 0:
        print(remained_pencils * "|")

    if remained_pencils == 0:
        if user_name == "John":
            print("John won!")
        else:
            print("Jack won!")
        break

    if remained_pencils != 0:
        if user_name == "John":
            print(f"{user_name}'s turn!")
            user_name = "Jack"
        else:
            print(f"{user_name}'s turn!")
            user_name = "John"


