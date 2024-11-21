#LOOPS


#loops are used TO print long list of numbers by a small code

#exmaple
i = 1
while i<10:
    print (i)
    i +=1 #i=i+1
 # and if wants to print these numbers in a single line put print(x,end=",") you can put dot comma or space and it will appear between the numbers 

#example 2 
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

 # Using the range Function with the for Loop
for x in range(0,15):
      print (x)

for x in range(10):
     print (x)

#Nested Loops  -- A loop withon a loop


#Nested loop
a= [1,2,3]
b=[4,5,6]
for c in a:
    for d in b:
        print (c,d)

# Another Example 

for a in range (2):   # 0,1,
    
      for b in range(3) :  #0,1,2
             print("outer loop" ,a , "Inner Loop" , b)
          