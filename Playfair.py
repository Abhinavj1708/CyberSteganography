import string
alphabets = string.ascii_uppercase

def keygeneration(key, chk):
    if chk:
        ch = 'I'
    else:
        ch = 'J'
    k = []
    Krow = []
    Kcol = []
    temp = []
    key = key + list(alphabets)
    for i in key:
        if i not in k:
            if i != ch:
                k.append(i)
    for i in k:
        if i is not list:
            temp.append(i)        
        if len(temp) == 5:
            Krow.append(temp)
            temp = []
    print(f'Generated Key:\n{Krow}')
    temp = []
    for i in Krow:
        for j in i:
            temp.append(j)
    Kcol = [[] for x in Krow]
    for i in range(25):
        Kcol[i%5].append(temp[i])
    return Krow, Kcol

def ptcorrection(pt):
    ch = []
    for i in range(1,len(pt)):
        if pt[i-1] == pt[i]:
            pt[i-1:i+1] = [pt[i-1], 'X', pt[i]]
            ch.append('X')
    if len(pt) % 2 != 0:
        pt += 'Q'
        ch.append('Q')
    print(f'\nCorrected text for encrypting is {"".join(pt)}')
    temp = []
    P = []
    for i in pt:
        temp.append(i)
        if len(temp) == 2:
            P.append(temp)
            temp = []
    print(f'Encrypting format: {P}')
    return P, ch

def ijcheck(pt):
    if 'J' in pt:
        return True
    return False

def cipher(text, key):
    plaintext = list(text.upper().replace(' ',''))
    key = list(key.upper().replace(' ',''))
    chk = ijcheck(plaintext)
    key1, key2 = keygeneration(key, chk)
    pt, corrections = ptcorrection(plaintext)
    
    pos = [[] for x in pt]
    temp = []
    for i in key1:
        for j in i:
            temp.append(j)
    for i in range(len(pt)):
        for j in key1:
            if pt[i][0] in j and pt[i][1] in j:
                pos[i].append(key1[key1.index(j)][(j.index(pt[i][0])+1)%5])
                pos[i].append(key1[key1.index(j)][(j.index(pt[i][1])+1)%5])
                break
        for j in key2:
            if pt[i][0] in j and pt[i][1] in j:
                pos[i].append(key2[key2.index(j)][(j.index(pt[i][0])+1)%5])
                pos[i].append(key2[key2.index(j)][(j.index(pt[i][1])+1)%5])
                break
        if len(pos[i]) == 0:
            pos[i].append(key1[temp.index(pt[i][0])//5][temp.index(pt[i][1])%5])
            pos[i].append(key1[temp.index(pt[i][1])//5][temp.index(pt[i][0])%5])
    temp = []
    for i in pos:
        for j in i:
            temp.append(j)
    C = ''.join(temp)
    print(f'\nEncrypted text is {C}')
    return C, key1, key2, corrections

def decipher(C, key1, key2, correct):
    C = list(C)
    ct = []
    temp = []
    for i in C:
        temp.append(i)
        if len(temp) == 2:
            ct.append(temp)
            temp = []
    print(f'Decrypting format: {ct}')
    temp = []
    for i in key1:
        for j in i:
            temp.append(j)
    pos = [[] for x in ct]
    for i in range(len(ct)):
        for j in key1:
            if ct[i][0] in j and ct[i][1] in j:
                pos[i].append(key1[key1.index(j)][(j.index(ct[i][0])+4)%5])
                pos[i].append(key1[key1.index(j)][(j.index(ct[i][1])+4)%5])
                break
        for j in key2:
            if ct[i][0] in j and ct[i][1] in j:
                pos[i].append(key2[key2.index(j)][(j.index(ct[i][0])+4)%5])
                pos[i].append(key2[key2.index(j)][(j.index(ct[i][1])+4)%5])
                break
        if len(pos[i]) == 0:
            pos[i].append(key1[temp.index(ct[i][0])//5][temp.index(ct[i][1])%5])
            pos[i].append(key1[temp.index(ct[i][1])//5][temp.index(ct[i][0])%5])
    temp = []
    for i in pos:
        for j in i:
            temp.append(j)
    P = ''.join(temp)
    print(f'\nDecrypted text is {P}')
    for i in temp:
        if i in correct:
            temp.remove(i)
    P = ''.join(temp)
    print(f'Corrected decrypted text is {P}')
    return P
