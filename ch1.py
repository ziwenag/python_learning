### This is ch1 note

## 1.1 pyton的数据类型, python data type
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

## 1.2, 一个加密示例 a encryption demo
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

## 1.3, 一个解密示例 , a dencryption demo
msg = 'abcdefghijklmnopqrstuvwxyz'
code = 'ZEBRASCDFGHIJKLMNOPQTUVWXY'

de_key = {}
for m in range(26):
    de_key[code[m]] = msg[m]
print(de_key)

decrypt_text = ''
for n in encrypt_text:
    if n in code:
        decrypt_text = decrypt_text + de_key[n]
    else:
        decrypt_text = decrypt_text + n
print(decrypt_text)

