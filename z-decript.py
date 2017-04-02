__author__ = 'sirivella madhu'
# required softwares: python3.

# welcome note!

print('Welcome to z-encription method:')
print('Required inputs:')
print('\t 1.Encription-key')
print('\t 2.text-word')
print('*** do not use special characters white-space and repeated charecters ***')

#input key and text

raw_key = input('Enter encription key:')
raw_text = input('Enter text-word:')
key = raw_key.upper()
text = raw_text.upper()


# define variables

F1 = [['A','B','C','D','E','F'],
      ['G','H','I','J','K','L'],
      ['M','N','O','P','Q','R'],
      ['S','T','U','V','W','X'],
      ['Y','Z','0','1','2','3'],
      ['4','5','6','7','8','9']]

F2 = [['A','B','C','D','E','F'],
      ['G','H','I','J','K','L'],
      ['M','N','O','P','Q','R'],
      ['S','T','U','V','W','X'],
      ['Y','Z','0','1','2','3'],
      ['4','5','6','7','8','9']]

F3 = [['A','B','C','D','E','F'],
      ['G','H','I','J','K','L'],
      ['M','N','O','P','Q','R'],
      ['S','T','U','V','W','X'],
      ['Y','Z','0','1','2','3'],
      ['4','5','6','7','8','9']]

V1 = [['A','B','C','D','E','F'],
      ['G','H','I','J','K','L'],
      ['M','N','O','P','Q','R'],
      ['S','T','U','V','W','X'],
      ['Y','Z','0','1','2','3'],
      ['4','5','6','7','8','9']]

V2 = [['A','B','C','D','E','F'],
      ['G','H','I','J','K','L'],
      ['M','N','O','P','Q','R'],
      ['S','T','U','V','W','X'],
      ['Y','Z','0','1','2','3'],
      ['4','5','6','7','8','9']]

#assignig values for key-generated table1 or variable table1

i = 0
j = 0

for letter in key:
    if i > 5:
        i = 0
        j += 1

    V1[j][i] = letter
    i += 1

#print(i)
#print(j)

for row in F1:
    for elem in row :
        if elem not in key :
            if i > 5:
                i = 0
                j += 1

            #print(elem)
            #print(i,j)
            V1[j][i] = elem
            i += 1

#assignig values for key-generated table2 or variable table2

i = 5
j = 5

for letter in key:
    if i < 0:
        i = 5
        j -= 1

    V2[j][i] = letter
    i -= 1

#print(i)
#print(j)

for row in F1:
    for elem in row :
        if elem not in key :
            if i < 0:
                i = 5
                j -= 1

            #print(elem)
            V2[j][i] = elem
            i -= 1

#printing key-generated tables and fixed tables

for m in range(6):
    for n in range(6):
        print(F1[m][n], end=' ')
    print('\t', end=' ')
    for n in range(6):
        print(V1[m][n], end=' ')
    print()
    print()
print()


for m in range(6):
    print('           ', end='\t ')
    for n in range(6):
        print(F2[m][n], end=' ')
    print()
    print()
print()

for m in range(6):
    print('           ', end='\t ')
    for n in range(6):
        print(V2[m][n], end=' ')
    print('\t', end=' ')
    for n in range(6):
        print(F3[m][n], end=' ')
    print()
    print()
print()

#encription process and encripted message

print('The encripted data for "' + text +'" is :')
tab = 1
for cha in text:
    if tab%2!=0 :
        tab += 1
        for m in range(6):
            for n in range(6):
                if V1[m][n] == cha:
                    print(F1[m][5-n]+F2[m][n],end='')

    else:
        tab += 1
        for m in range(6):
            for n in range(6):
                if V2[m][n] == cha:
                    print(F2[m][n]+F3[m][5-n], end='')

print()


raw_ciphertext = input('Enter encryption-text or ciphertext:')
ciphertext = raw_ciphertext.upper()

#decription process
print('The Decryption data for "' + ciphertext +'" is :')

tab = 0

for cipher in ciphertext:
    tab += 1
    if tab%4 == 2:
        for m in range(6):
            for n in range(6):
                if F2[m][n] == cipher:
                    #print('v1',cipher,m,n,tab)

                    print(V1[m][n],end='')


    if tab%4 == 3:
        for m in range(6):
            for n in range(6):
                if F3[m][n] == cipher:
                    #print('v2',cipher,m,n,tab)
                    print(V2[m][n],end='')


print()
print('Thank you!')

