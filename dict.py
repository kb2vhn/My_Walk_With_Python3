# John wood
# Aug 30, 2020

# Dictionaries
# I am going to put a list of names into the dictonary and have it count the names
print('\n')
namesToCount = dict()
names = ['John', 'Chrissy', 'James', 'John']
for name in names:
    namesToCount[name] = namesToCount.get(name, 0) + 1
print(namesToCount) 

# lets make it look better
print('\nThis looks better I think\n')
for key in namesToCount:
    print(key, namesToCount[key])

# take a file and find the word that is used the most
print('\nReadme most used word\n')
fileOpen = open('README.md')

wordCount = dict()
for line in fileOpen:
    words = line.split()
    for word in words:
        wordCount[word] = wordCount.get(word, 0) + 1

mostUsedWord = None
numberOfTimesUsed = None
for word, count in wordCount.items():
    if numberOfTimesUsed is None or count > numberOfTimesUsed:
        mostUsedWord = word
        numberOfTimesUsed = count

print(mostUsedWord, numberOfTimesUsed)