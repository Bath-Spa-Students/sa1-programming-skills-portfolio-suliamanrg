#This is the code to prompt user for pizza toppings.
while True:
    input_topping=input("Please enter the topping to add to your pizza :")
    if input_topping.lower()=='exit':
        break
    print(f"{input_topping.title()} topping will be added to your pizza.")