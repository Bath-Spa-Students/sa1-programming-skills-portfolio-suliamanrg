 #This code is for inputing the user's first name
firstname=input("Enter your first name:")

#This code is for inputing the user's second name.
secondname=input("Enter your second name:")

#This is the code for inputing user's hometown.
hometown=input("Enter your hometown:")

#This code is for inputing user's age.
while True:
    try:
        age=int(input("Enter your age:"))
        break
    except ValueError:
        print("Invalid input for age. Enter the number.")

#This is code for storing information.
information={"FirstName":firstname,"SecondName":secondname,"Hometown":hometown,"Age":age}

#This is code for displaying the values.
print(f"First Name: {information['FirstName']}\nSecond Name: {information['SecondName']}\nHometown: {information['Hometown']}\nAge: {information['Age']}")












