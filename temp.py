# John wood
# Aug 29, 2020
# This is a temp python file to play with things before they go to a category

# List

nList = [] # or could do nList = list()
nList.append('python')
nList.append('C++')
print(len(nList))
print(nList)
nList.sort()
print (nList)

numList =[3, 54, 23, 2, 22]
print(len(numList))                     # count
print(max(numList))
print(min(numList))
print(sum(numList))
print(sum(numList)/(len(numList)))      # get the average
print(numList)
numList.sort()
print(numList)

# ask for some numbers to add

print('\nPlease Enter a Number to add, when done type done')
addNumList = list()
while True:
    i = input('What is your number? ')
    if i == 'done':
        break
    i = float(i)                    # must add a specific type or it will fail
    addNumList.append(i)
print('Total: ', sum(addNumList))