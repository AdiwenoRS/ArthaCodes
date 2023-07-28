from os import system 
from numpy import average

print('Soal IPA\n\nKerjakan dengan teliti!\n\n')

soal1 = '1. Apa itu gravitasi?'
print(soal1)
print('  a. keadaan benda yang memiliki massa dorong mendorong dari pusat massa tersebut\n  b. keadaan benda yang memiliki massa tarik menarik dari pusat massa tersebut')
jawab1 = str(input('Masukkan jawaban: '))

soal2 = '\n2. siapa penemu gravitasi?'
print(soal2)
print('  a. Albert Einstein\n  b. Isaac Newton')
jawab2 = str(input('Masukkan jawaban: '))

soal3 = '\n3. Apa itu gaya?'
print(soal3)
print('  a. Adalah interaksi antar benda massa yang membuatnya berubah\n  b. Adalah interaksi apapun yang membuat benda bermassa bergerak')
jawab3 = str(input('Masukkan jawaban: '))

def clear():
    if 0==0:
        _ = system('cls')
clear() 

if jawab1=='b':
    cor1=1
    soal1 = ('1. Apa itu gravitasi? (BETUL)\nJawabanmu : b. keadaan benda yang memiliki massa tarik menarik dari pusat massa tersebut')
else:
    cor1=0
    soal1 = ('1. Apa itu gravitasi? (SALAH)\njawabanmu : a. keadaan benda yang memiliki massa dorong mendorong dari pusat massa tersebut\nYang benar : b. keadaan benda yang memiliki massa tarik menarik dari pusat massa tersebut')
    
if jawab2=='b':
    cor2=1
    soal2 = ('\n2. siapa penemu gravitasi? (BETUL)\nJawabanmu : b. Isaac Newton')
else:
    soal2 = ('\n2. siapa penemu gravitasi? (SALAH)\nJawabanmu : a. Albert Einstein\nYang benar : b. Isaac Newton')
    cor2=0
if jawab3=='b':
    cor3=1
    soal3 = ('\n3. Apa itu gaya? (BETUL)\nJawabanmu : b. Adalah interaksi apapun yang membuat benda bermassa bergerak')
else:
    cor3=0
    soal3 = ('\n3. Apa itu gaya? (SALAH)\nJawabanmu : a. Adalah interaksi antar benda massa yang membuatnya berubah\nYang benar : b. Adalah interaksi apapun yang membuat benda bermassa bergerak')

jmlh = (cor1,cor2,cor3)
average = sum(jmlh)/len(jmlh)*100
print('\nSoal yang benar : ',sum(jmlh))
print('Nilai kamu : ',int(average))
print('\n', soal1,'\n\n', soal2, '\n\n', soal3)


