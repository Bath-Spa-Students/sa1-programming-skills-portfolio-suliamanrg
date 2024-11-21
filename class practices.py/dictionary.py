#DICTIONARY


#dictionary in phyton is used to store data 
# Creation of  dictionary
dictionary = {}
print(dictionary)

#another way of creation of dictionary is
 
dictionary = dict()
print(dictionary, type(dictionary))

# To add something in the dictionary 
exp = {'name' : 'suli '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
print (exp)


# To add some value in dictionary 

my_dictionary  = {'name' : 'suli '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
print(my_dictionary,type(my_dictionary))
 # Name , age and nationality are keys , suli,19  and pakistan are values

#if we wants a specific value from the dictionary

dictionary  = {'name' : 'suli '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '} 
print(dictionary["name"],type(dictionary))


# items METHOD in dictionary


dictionary  =  {'name' : 'suli '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
print(dictionary.items())
#through this method we can get all the items stored in dictionary  


 # if we want the only the keys in the dictionary 

dictionary  =  {'name' : 'suli '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
print(dictionary.keys())

# Delete method 
#through deleted method we could delete a specific data from the dictionary

dictionary  = {'name' : 'suli '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
del dictionary ["place"]
print(dictionary.items())
#the output will be only the name and nationality

# POP METHOD
#through this method we can make one value prominent by adding .pop with the dictionary

dictionary  = { 'ame' : 'suli' ,
                'age' :  '19' , 
                'nationality ': 'pakistan' } 
print(dictionary.pop("name"))
print(dictionary.keys())
print(dictionary.values())