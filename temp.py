# John wood
# Aug 29, 2020
# This is a temp python file to play with things before they go to a category

n = 0
while True:
    if n == 3:
        break
    print('Try number: {}'.format(n))
    n = n + 1

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        #break
    #print("Loop:", itervar, smallest)  # this was used to see if it was iterating
                                        # correctly
print("Smallest:", smallest)

found = False
print ('Before', found)
for value in [9, 41, 13, 3, 6]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found, value)



