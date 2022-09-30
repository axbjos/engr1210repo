########################################
#
# Basic For Loops
#
# AxnetLabs, LLC
#
# Joe Axberg, 2022
#
#######################################

''' 
Demonstration of basic FOR loops in Python

Remember that in Python FOR Loops should be thought of as being FOR EACH loop.

for <each item> in <a list of items>:
    do these this
    do that

Python will repeatedly do all of the "do's"   The number of loops equals the
number of items in the list.  

'''

################### THE MOST BASIC PYTHON LOOP #######################
# The most basic loop
# The following code will create a loop that executes 4 times
# Why? Because there are four items in the list
# Say it this way "For every X in the List"
for x in [1,2,3,4]:
    print(x)

# This code will also execute the loop four times (why?)
for x in [0,0,0,0]:
    print(x)


################ TRACKING HOW MANY TIMES YOU LOOPED ##################
# Keep track of how many times you looped
counter = 0    #<--declare a variable to keep track of how many times you looped
# don't know what it is yet though, so we set to zero
for num in [1,2,3,4,5]:
    print(num)
    counter = counter + 1

print("The number of times looped was: ", counter)


################ PUT THE LIST INTO A VARIABLE ######################
# Put the list of numbers into a Variable
listOfNums = [1,2,3,4,5]
counter = 0
for num in listOfNums:
    print(num)
    counter = counter + 1

print("The number of times looped was: ", counter)
# however.....
# you could just find the number of times a loop will execute by finding
# out how long it is
print("The number of times it should've looped was: ", len(listOfNums))
# putting "len" around the list name will tell you how many items there are.


################# A LIST CAN BE ANYTHING ######################
# A list can be litterally be a list of ANYTHING in Python.
theListOfStuff = [1,"Joe", 25.50, "Dave", "b", 100536]

# notice how the choice of variable names here make it instantly
# apparent what is going on
for eachItem in theListOfStuff:
    print(eachItem)

print("The number of Items in the List was: ", len(theListOfStuff))


################ HEAD EXPLODY WAY ############################
# we could also do this - this is a head-explody version
theListOfStuff = [1,"Joe", 25.50, "Dave", "b", 100536]   #<--here is our list again

listOfStuffLength = len(theListOfStuff)   #<--this var knows how long the list is...

print("This loop should execute: ", listOfStuffLength, " times.")

# Use the length of the theListOfStuff to create a range of numbers
timesToLoop = range(listOfStuffLength)

print("In case your wondering here is what is in timesToLoop: ", timesToLoop)

# now loop
for i in timesToLoop:
    print(theListOfStuff[i])
    # do you see what's happening?
    # first time through the loop:
    # theListOfStuff[0]
    # next time....
    # theListOfStuff[1]
    # and so on....

# don't always need the range in a variable tho...
for i in range(listOfStuffLength):
    print(theListOfStuff[i])


################## COUNT THROUGH TWO LISTS AT ONCE #################

counter = 0
list1 = ["Do", "you", "see", "what's", "going", "on!"]
list2 = [1,2,3,4,5,6]

for i in range(len(list2)):
    counter = counter + 1
    print("Loop", counter, "we have this number ", list2[i], " from list2, and this word: " , list1[i], " from list1")



#################### TWO DIFFERENT WAYS #######################

# just iterate through the list

list1 = [1,2,3,4,5]

for i in list1:   #<- The FOR EACH way - for each i in list1
    print(i) 


for i in range(len(list1)):  #<- find out how long the list is and loop that many times
    print(list1[i])          #<- print out the list by using i as the index.


