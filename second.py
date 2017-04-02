__author__ = 'sirivella madhu'

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

key = 'STAIC123'

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
            V1[j][i] = elem
            i += 1



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



for m in range(6):
    for n in range(6):
        print(F1[m][n], end='  ')
    print('\t', end=' ')
    for n in range(6):
        print(V1[m][n], end='  ')
    print()
    print()
print()


for m in range(6):
    print('\t' + '\t'+ '\t'+ '\t', end='\t ')
    for n in range(6):
        print(F2[m][n], end='  ')
    print()
    print()
print()

for m in range(6):
    print('\t' + '\t' + '\t' + '\t', end='\t ')
    for n in range(6):
        print(V2[m][n], end='  ')
    print('\t', end=' ')
    for n in range(6):
        print(F3[m][n], end='  ')
    print()
    print()
print()

text = 'ATTACKBANK'

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
print('Thank you!')




