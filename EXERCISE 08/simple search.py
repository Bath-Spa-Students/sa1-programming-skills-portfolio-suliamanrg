#the list of names.
listnames = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Input the search term.
searchterm = input("Enter a name to search: ")

#Checking if the searchname is in the list and display the result.
if searchterm in listnames:
    print(f"'{searchterm}' was found in the list.")
else:
    print(f"'{searchterm}' was not found in the list.")
