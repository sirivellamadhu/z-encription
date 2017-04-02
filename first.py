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

key = 'FERT325'

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
print(V1)


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
print(V2)

#F1.index('A')


text = 'GOODMORNING'

