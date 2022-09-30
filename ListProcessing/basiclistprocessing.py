########################################
#
# Basic For Loops
#
# AxnetLabs, LLC
#
# Joe Axberg, 2022
#
#######################################



################# TAKE ITEMS FROM ONE LIST AND PUT THEM INTO ANOTHER  ###################
#
print("\n\n\n### TAKE ITEMS FROM ONE LIST AND PUT THEM INTO ANOTHER ###")
# The Lists...

list1 = [1,2,3,4,"George"]
list2 = []  #<--Empty list

print("\n\nBEFORE: ")
print("Here is List 1: ", list1, "\nHere is List 2: ", list2)

# Solution 1 - the true Python way

for listItem in list1:
    list2.append(listItem)

print("\nAFTER: ")
print("Here is List 1: ", list1, "\nHere is List 2: ", list2)


################# PROCESS EACH ITEM IN A LIST AND REPLACE WHAT WAS THERE ################
#
print("\n\n\n### PROCESS EACH ITEM IN A LIST AND REPLACE WHAT WAS THERE ###")
# Take each item in a list and slice off the first three letters and put back in the same list

listOfNames = ["Joseph", "Edwin", "Marsha", "Elizabeth"]

print("\n\nBEFORE: ", listOfNames)

print("\nrange(len(listOfNames)) creates this: ", list(range(len(listOfNames))))

for i in range(len(listOfNames)):  #<----this range will gen a list of numbers = the the # of times to loop
    listOfNames[i] = listOfNames[i][0:3] #<---use the 

print("\nAFTER: ", listOfNames)


################## TAKE AN ITEM FROM TWO LISTS AND PUT IN A NEW LIST
#
print("\n\n\n### TAKE AN ITEM FROM TWO LISTS AT ONCE AND PUT IN A NEW LIST ###\n")
# The lists
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
destinationList = []

# the zip function lets us iterate through two lists at once
# read it:  for item1 in list1 and item2 in list2 do this...
for item1, item2 in zip(list1, list2):           
    print(item1,item2)
    destinationList.append(str(item1) + item2)   #<---item1 is a number, so we need to cast to a string
                                                 # then concatenate together and append to the new list

print("\nThe destination list contains: ", destinationList)
print()


################## LIST OF LISTS ###############################
#
print("\n\n\n### LISTS OF LISTS ###\n")
# The list of lists
listOfLists = [[1,2,3],[4,5,6],[7,8,9],[0,0,0]]

for aList in listOfLists:           
    print(aList)

print()


################## PRINT OUT A LIST OF LISTS ###############################
#
print("\n\n\n### LISTS OF LISTS ###\n")
# The list of lists
listOfLists = [[1,2,3],[4,5,6],[7,8,9],[0,0,0]]

for aList in listOfLists:  
    for num in aList:      
        print("Inner List: ", aList, " current number in that list: ", num)

print()