# John wood
# Aug 29, 2020

# numaric values
n = 0
while True:
    if n == 3:
        break
    print('Try number: {}'.format(n))
    n = n + 1

# find the smallest from a list
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        #break
    #print("Loop:", itervar, smallest)  # this was used to see if it was iterating
                                        # correctly
print("Smallest:", smallest)

# find the number from a list
found = False
print ('Before', found)
for value in [9, 41, 13, 3, 6]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found, value)

# List with numbers

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