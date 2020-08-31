# John wood
# Aug 30, 2020

# Regular Expressions this is some simple search and findall
import re
try:
    openFile = open('string.py') # this assumes that string.py is in the current working dir
except:
    print('Unable to locate file')
    quit()
for nfile in openFile:
    nfile = nfile.strip()
    if re.search('#', nfile):
        print(nfile)


print('\nFind email addresses in a string')
f = 'From john.wood@whatever.org sent by john.wood@whatever.net test string'
ret = re.findall('From \S+@\S+', f)
ret_1 = re.findall('From .*@([^ ]*)', f)
print(ret) # find from email address in the f string
print('\nFrom host',ret_1)

ret2 = re.findall('^From (\S+@\S+)', f) # return just the from address
print(ret2)

ret3 = re.findall('\S+@\S+', f) # return all email addresses in the string
ret_3 = re.findall('@([^ ]*)', f)
print(ret3)
print('\nall host',ret_3)