# John wood
# Aug 31, 2020
# this example is on freecodecamp

# xml schema

import xml.etree.ElementTree as ET
data = ''' <person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('\nName:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

print('\n')
data = ''' <stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="31">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('User Number', item.get('x'))
    print('UID', item.find('id').text)
