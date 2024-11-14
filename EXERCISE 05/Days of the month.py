# define the days in each month (default for non-leap years)
daysofmonth = { 1: 30, 2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31 }

#function to get the number of days in a specific month
try:
    # ask the user to input the month number
    monthname = int(input("Enter the month number (1-12): "))
    
    # validate the month number
    if monthname < 1 or monthname > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
        exit()
    # check whether the month is February and handle leap year
    if monthname == 2:
        # ask whether it's a leap year
        leapyear = input("Is it a leap year? (yes or no): ").strip().lower()
        if leapyear == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days in a non-leap year.")
    else:
        # output the number of days for the selected month
        print(f"The month {monthname} has {daysofmonth[monthname]} days.")

except ValueError:
    print("Invalid input. Please enter a number.")
