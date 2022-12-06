# 文件读取
f = open('work/novel1.txt')
text = f.read()
f.close()
print(text[100:500])

#变成小写
text1 = text.lower()
print(text1[100:500])

#统计字母词频
counter = {}
amount_letter = 0
for i in text1:
    if 'a' <=i <='z':
        amount_letter = amount_letter + 1
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] = counter[i] + 1

print(counter)
print(amount_letter)

#统计字母占比
frequence = {}

for x in counter:
    if x not in frequence:
        frequence[x] = counter[x] / amount_letter

print(frequence)

code_file = open('work/code.txt')
code_text = code_file.read()
code_file.close()
print(code_text[100:500])

counter_code = {}
amount_letter_code = 0

for j in code_text:
    if j >= 'A' and j<='Z':
        amount_letter_code = amount_letter_code + 1
        if j not in counter_code:
            counter_code[j] = 0
        else:
            counter_code[j] = counter_code[j] + 1
print(counter_code)
print(amount_letter_code)

frequence_code = {}
for y in counter_code:
    frequence_code[y] = counter_code[y] /amount_letter_code

print(frequence_code)

sort_f = sorted(frequence.items(), key=lambda kv:kv[1], reverse=True)
print(sort_f)
sort_code = sorted(frequence_code.items(), key=lambda kv:kv[1], reverse=True)
print(sort_code)

question = '''RLVK, RLVK, RLVK.  QDAOA VZP KLQDFKC AIPA QL RL, PL ZIFBA PLLK EACZK QZIHFKC ZCZFK.  `RFKZD'II JFPP JA UAOX JTBD QL-KFCDQ, F PDLTIR QDFKH!'  (RFKZD VZP QDA BZQ.)  `F DLMA QDAX'II OAJAJEAO DAO PZTBAO LS JFIH ZQ QAZ-QFJA.  RFKZD JX RAZO!  F VFPD XLT VAOA RLVK DAOA VFQD JA!  QDAOA ZOA KL JFBA FK QDA ZFO, F'J ZSOZFR, ETQ XLT JFCDQ BZQBD Z EZQ, ZKR QDZQ'P UAOX IFHA Z JLTPA, XLT HKLV. ETQ RL BZQP AZQ EZQP, F VLKRAO?'  ZKR DAOA ZIFBA EACZK QL CAQ OZQDAO PIAAMX, ZKR VAKQ LK PZXFKC QL DAOPAIS, FK Z ROAZJX PLOQ LS VZX, `RL BZQP AZQ EZQP?  RL BZQP AZQ EZQP?' ZKR PLJAQFJAP, `RL EZQP AZQ BZQP?' SLO, XLT PAA, ZP PDA BLTIRK'Q ZKPVAO AFQDAO NTAPQFLK, FQ RFRK'Q JTBD JZQQAO VDFBD VZX PDA MTQ FQ.  PDA SAIQ QDZQ PDA VZP RLYFKC LSS, ZKR DZR GTPQ EACTK QL ROAZJ QDZQ PDA VZP VZIHFKC DZKR FK DZKR VFQD RFKZD, ZKR PZXFKC QL DAO UAOX AZOKAPQIX, `KLV, RFKZD, QAII JA QDA QOTQD:  RFR XLT AUAO AZQ Z EZQ?' VDAK PTRRAKIX, QDTJM! QDTJM! RLVK PDA BZJA TMLK Z DAZM LS PQFBHP ZKR ROX IAZUAP, ZKR QDA SZII VZP LUAO.'''

question = question.replace('A', 'e')
question = question.replace('Q', 't')
question = question.replace('Z', 'a')
print(question)

question = question.replace('F', 'i')
question = question.replace('I', 'l')
question = question.replace('O', 'r')
question = question.replace('L', 'o')
question = question.replace('D', 'h')
print(question)

question = question.replace('X', 'y')
question = question.replace('P', 's')
print(question)

question = question.replace('M', 'p')
question = question.replace('S', 'f')
question = question.replace('V', 'w')
print(question)

question = question.replace('K', 'n')
question = question.replace('R', 'd')
question = question.replace('C', 'g')
question = question.replace('B', 'c')
question = question.replace('T', 'u')
question = question.replace('U', 'v')
question = question.replace('J', 'm')
question = question.replace('E', 'b')
question = question.replace('H', 'k')
print(question)