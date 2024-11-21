#FUNCTIONS


# Void function 
def print_message():
    print("Sulaiman")
# Calling function 
print_message()

# Local variable 
def print_message():
    message ="pakistan"  # Local variable 
    print(message)
# Calling function 
print_message()
# If i call this message it shows an error 

def print_message():
    message ="welcome"  # Local variable 
    print(message)
    print(message)     # message is not defined bcz local varaible life is inside of program 

print_message()


#Diffenrent functions have same local variables name - No syntax error 

def print_message():
  message ="sulaiman"
  print(message)
  
def print_message_2():
  message ="is the best"
  print(message)

print_message()
print_message_2()

# Paasing argument to variable   

def print_message_2(hello):  # parameter 
  print(hello)

msg ="welcome to my code"
print_message_2(msg)  # Argument 

#Example  parameter x store value and get double 
def main():
    value =23
    show_double(value)
    
def show_double(x):
      print(x*2)

main()

# Passing Multiple arguments 