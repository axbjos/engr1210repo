##########################################
# Open a file for reading
theFile = open("somedata.csv", 'r')

# Read in the whole file (not usually recommended)
theContentsOfTheFile = theFile.read()   #<- this will read in everything at once.
print("\n\nFirst read: \n", theContentsOfTheFile)

# Notice that if you attempt to read the file again, nothing happens
# The read is a kind of One-n-Done deal

tryToReadAgain = theFile.read()
print("\nTry to read again: \n", tryToReadAgain)

# You should that the above has nothing.  To read it again, you'll need to 
# close the file and open it back up

# remember to close
theFile.close()


########################################
# Iterate over the lines of a file

# Open a file for reading
theFile = open("somedata.csv", 'r')

# use a loop

aListOfAllLines = theFile.readlines()   #<- this will create a list of all the lines in the file

print("Contents of the file as a list: ", aListOfAllLines, "\n")

print("Iterating through the lines: \n")
# now iterate
for line in aListOfAllLines:
    print(line)

theFile.close()


#### HERE IS AN EVEN EASIER WAY.  JUST HAVE PYTHON ITERATE THOUGH THE LINES IN THE FILE

# Open a file for reading
theFile = open("somedata.csv", 'r')

print("\n\nIterating through the lines again: \n")
for line in theFile.readlines():  #<- this works because, as we saw, readlines creates a list
    print(line)

theFile.close()


### do some stuff to the stuff in the file

# Open a file for reading
theFile = open("somedata.csv", 'r')

listOfFirstNames = []  #<- holding list for our data being gathered

print("\n\nIterating through the lines again: \n")
for line in theFile.readlines():  #<- this works because, as we saw, readlines creates a list
    currentLine = line.split(",")
    listOfFirstNames.append(currentLine[0]) #<- grab the first name in position 0 of the list
    print("Here is the line: ", line)

print("Here is the contents of listOfFirstNames: ", listOfFirstNames)

theFile.close()


### do some stuff to the stuff in the file and write out to a new file

# Open a file for reading
theFile = open("somedata.csv", 'r')
theOtherFile = open("firstnames.csv", 'w')

listOfFirstNames = []  #<- holding list for our data being gathered

print("\n\nIterating through the lines again: \n")
for line in theFile.readlines():  #<- this works because, as we saw, readlines creates a list
    currentLine = line.split(",")
    listOfFirstNames.append(currentLine[0]) #<- grab the first name in position 0 of the list and append to our list of names
    theOtherFile.write(currentLine[0]+"\n")      #<- also write it out to the other file.
    print("Here is the line: ", line)

print("Here is the contents of listOfFirstNames: ", listOfFirstNames)

theFile.close()
theOtherFile.close()