a1 = "1. Say Hello"
a2 = "2. Say bye"
a3 = "3. Exit"

print ("\n", a1, "\n", a2, "\n", a3)

while True:
    a = int(input())
    if a == 1:
        print ("Hello!")
    elif a == 2:
        print ("Bye!")
    elif a == 3:
        break
    else:
        print("ERROR!!!")