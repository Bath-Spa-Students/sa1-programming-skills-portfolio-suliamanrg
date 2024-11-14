 #define the correct password.
password=12345

#set the maximum number of attempts.
attempts=5

#initialize the attempt counter to 0.
counter=0

#start the loop to ask for the password.
while counter<attempts:
    enterpassword=(int(input("Enter the password:"))) 
    #check whether the entered password is correct.
    if enterpassword==password:
        print("Access Granted")
        break

    else:
        counter += 1 

    #calculate remaining attempts.
    attemptsremaining=attempts-counter

    #check feedback on remaining attempts.
    if attemptsremaining>0:
        print(f"Incorrect password. You have {attemptsremaining} attempts left")
    else:
        print("Maximum attempts reached. The authorities have been alerted.")
