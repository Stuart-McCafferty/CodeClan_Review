print("Okay, lets fix this!")
print("Turn on your computer")
status = input("Did it boot up? Y/N ")
if status == "Y":
    print("Log in with username and password")
    print("Computer fixed")
else:
    status = input("Is it plugged in? Y/N ")
    if status == "Y":
        print("The computer is broken")
    else:
        print("Plug it in")
        status = input("Did this fix the problem? Y/N ")
        if status == "Y":
            print("Log in with username and password")
            print("Computer fixed")
        else: 
            print("Computer broken")