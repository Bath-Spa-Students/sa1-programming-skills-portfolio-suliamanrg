# Function for checking if a number is even or odd
def check_even_odd(user_number):
    # If the number is evenly divisible by 2, it's even
    if user_number % 2 == 0:
        return f"{user_number} is even."
    else:
        # If not, it's odd
        return f"{user_number} is odd."

# Main function for handling user's input and display the result
def main():
    # Asking the user to enter a number
    try:
        input_number = int(input("Please enter a number: "))
        # Calling the check_even_odd function and geting the result 
        result = check_even_odd(input_number)
        # displaying the result 
        print(result)
    except ValueError:
        # For displaying the error message if the user inputs non integer value.
        print("Invalid input. Please enter a numerical value.")

# Only run the main function if this script is run directly
if __name__ == "__main__":
    main()
