# John Wood
# Aug 29, 2020
# open a file to look at comments the first method works only if the line
#   starts with a # 
# the second method works, it finds everything but I have to better format it

# look at the file and print all lines that start with #
print('\nStartswith() Method\n')
openFile = open('string.py')
for fileOut in openFile:
    if fileOut.startswith('#'):
        print(fileOut.strip())

# I want to see all comments so that didn't work lets try this
print('\nFind() Method\n')

#i = None
#with open('string.py', 'r') as f:
 #  i = f.read()
  # symbleFind = i.find('#')
   #if symbleFind is not -1:
    #   print(i[symbleFind:].strip())

j = None
openFile = open('string.py')
for nfile in openFile:
    j = nfile.find('#') # finds the location on the line for the comment block
    #print(j) # This is just testing to see that the find was findig things
    if j is not None or -1: # shows all comments but looks ugly
        print(nfile[j:].strip())

