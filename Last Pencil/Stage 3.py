pencil = int(input("How many pencils\n"))
name = input("who will be the first (John, Jack)\n")
print(pencil * "|")

while pencil != 0 :

    print(f"{name}'s turn:")
    y = int(input())
    if y > pencil:
        break
    else:
        pencil -= y

        print(pencil * "|")
        if name == "John":
            name = "Jack"
            
        else:
            name = "John"