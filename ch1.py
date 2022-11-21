# This is ch1
#Number
print(1,2,3)

#String
print('I Love Python')

#list
list = ['a',1,'b']
print(list)

#Tuple
tuple = ('c',2,'d')
print(tuple)

#Set
set = {'a', 'a', 'b', 'b'}
print(set)

#Dictionary
dict = {'a':1, 'b':2}
print(dict)

text = '''
AL KHOR - Enner Valencia scored two first-half goals as Ecuador beat hosts Qatar 2-0 in the opening match of the FIFA World Cup on Sunday.

The Fenerbahce forward converted a penalty before powering home a header to give Gustavo Alfaro's side a perfect start in Group A.

Despite having 47 percent of possession, the hosts didn't manage a single shot on target while Ecuador had three.

The result marked the first time that a host team has lost the opening game of the World Cup.
'''
print(text)

msg = 'abcdefghijklmnopqrstuvwxyz'
code = 'ZEBRASCDFGHIJKLMNOPQTUVWXY'
key = {}
for i in range(26):
    key[msg[i]] = code[i]
print(key)

encrypt_text = ''
for j in text:
    if j in msg:
        encrypt_text = encrypt_text + key[j]
    else:
        encrypt_text = encrypt_text + j

print(encrypt_text)
