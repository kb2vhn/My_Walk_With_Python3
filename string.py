# John Wood 
# Aug 28, 2020
# I haven't used git it a long time so trying to relearn how it to do things
# Testing my Git setup on chromebook using Visual Studio Code
# had an issue tring to push had to keep authorizing VS Code, hope that installing the gnome keyring will fix it 
# this worked for the last push lets see if it works for this one
# Good I have it working correctly

# The following is of the top of my head
print ('Testing')               # print a single word 
print ("Some things to test")   # print a string
print ("""This
is 
a multi line string.""")        # print a multi-line string

# simple string declared not very robust
str = "hello world!"
print ('\n')            # print new line this is an ugly way to do it too
print (str)             # print full string 
print (str[0])          # print only the first character of the string
print (str[2:7])        # print the 3rd to 5th (note that the 5th is not counted like normal computer math
                        # this is a litteral count number)
print (str[2:])         # print from the third character to the end of the string
print ((str +" ")*3)    # print the string with a space 3 times
print (str + "TEST")    # add test to the string just for this print
print (str)             # print the string again to show no changes to the string


# python list are similar to an array but can hold different data types

print("List" '\n')          # this looks a bit better but still not that good
alist = ["abcd", 786, 2.23, "john", 70.2]
tinylist = [123, "wood"]
print (alist)               # print the list
print (alist[0])            # print the first element of the list
print (alist[1:3])          # print the second element of the list to the third counted element
print (alist[2:])           # print the third element till the end
print (tinylist *2)         # print tinylist twice
print (alist + tinylist)    # print both list concatenated
print (alist)               # print the original list to prove no data change
print (tinylist)

# Tuples are basicaly a read only list they cannot change once declared
print ('\n')                # nice but why have extra lines
print ("Tuple" '\n')        # not too bad but still not that good
tuple =('ABCD', 256, 5.56, 'John')
tinytuple = (64, 'JJ')
print (tuple)
print (tuple[0])
print (tuple[1:3])
print (tuple[2:])
print (tinytuple *2)
print (tuple + tinytuple)

print ("\nString formating") # this might be better not so sure

who = 'John'
how_many = 12

print (who, 'bought', how_many, 'apples today!') # this is a bad way to concantante the string
print ('{} bought {} apples today!'.format(who, how_many)) # this looks much better and remindes me of working with c++

# print a simple message and iterate through a simple list
welcome_message = 'Hello'
names = ['John', 'James', 'Chrissy']

for name in names:
    print (welcome_message, name)


