def greetings(x): #input
    print("Hello " + x)



conures = ("Coco","Cookie","Popito") #list

message = "Hello"
for c in conures:
    #greetings(c)
    message = message + " " + c
print (message)

numbers = [1,2,3,4,5,6,3,44,55,67,34]
#create a functions to print n numbers
#for n in numbers:
    #print (n)

#Create a function called sumAll(n) to sum n numbers
s = 0
for n in numbers:
    s = s + n
print (s)