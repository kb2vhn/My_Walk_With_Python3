# John Wood
# Aug 29, 2020
# open a file to look at comments the first method works only if the line
#   starts with a # 
# the second method works, it finds everything but I have to better format it 
# the second was just changed today Aug 30, 2020 and is what I wanted to do

# look at the file and print all lines that start with #
print('\nStartswith() Method\n')
openFile = open('string.py')    # this assumes that string.py is in the current working dir
for fileOut in openFile:
    if fileOut.startswith('#'):
        print(fileOut.strip())

# I want to see all comments so that didn't work lets try this
print('\nFind() Method\n')

k = ''
j = None
openFile = open('string.py') # this assumes that string.py is in the current working dir
for nfile in openFile:
    j = nfile.find('#') # finds the location on the line for the comment block
    #print(j) # This is just testing to see that the find was findig things
    k = k + nfile[j:].strip() # changed on Aug 30, 2020

kn = k.split('#') 
for t in kn:
    print(t) # Now it is printing how I wanted it to ugly var's though

# Aug 30, 2020
# Regular Expressions the reg ex gives me exactly what I want!
import re

openFile = open('string.py') # this assumes that string.py is in the current working dir
for nfile in openFile:
    nfile = nfile.strip()
    if re.search('#', nfile):
        print(nfile)

# Aug 30, 2020
# take a file and find the word that is used the most
print('\nReadme most used word is:')
fileOpen = open('README.md')

wordCount = dict()
for line in fileOpen:
    words = line.split()
    for word in words:
        wordCount[word] = wordCount.get(word, 0) + 1

mostUsedWord = None
numberOfTimesUsed = None
for word, count in wordCount.items(): # itmes uses key, value so var names can be anything
    if numberOfTimesUsed is None or count > numberOfTimesUsed:
        mostUsedWord = word
        numberOfTimesUsed = count

print(mostUsedWord, numberOfTimesUsed)
