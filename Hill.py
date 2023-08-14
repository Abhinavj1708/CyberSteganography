import string

alphabets = {k:v for k, v in zip(range(26), string.ascii_uppercase)}

def matrixgen(content, row, col):
    M = []
    k = 0
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(content[k])
            k += 1
        M.append(temp)
    return M

def chkptlength(pt, size):
    correction = []
    for i in range(len(pt)%size):
        pt += 'Q'
        correction.append('Q')
    return pt, len(pt)//size, correction

def tonumber(pt, row, col):
    for i in range(row):
        for j in range(col):
            pt[i][j] = list(alphabets.values()).index(pt[i][j])
    return pt

def toletter(M):
    K = [['' for x in range(len(M[0]))] for y in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            K[i][j] = alphabets[M[i][j]]
    return K

def tostring(C):
    text = ''
    for i in range(len(C)):
        for j in range(len(C[0])):
            text += C[i][j]
    return text

def matrixmul(K, P):
    C = [[0 for x in range(len(P[0]))] for y in range(len(K))]
    for i in range(len(K)):
        for j in range(len(P[0])):
            for k in range(len(P)):
                C[i][j] += (K[i][k] * P[k][j])
                C[i][j] %= 26
    return C 

def imatrix(M):
    if len(M) ==  2:
        d = (M[0][0]*M[1][1] - M[0][1]*M[1][0]) % 26
        if d == 0:
            print('**The key matrix has determinant zero**')
            exit()
        for i in range(26):
            if (d*i)%26 == 1:
                di = i
        adj = M
        adj[0][0], adj[1][1] = adj[1][1], adj[0][0]
        adj[0][1] *= (-1)
        adj[1][0] *= (-1)
        for i in range(2):
            for j in range(2):
                adj[i][j] = (adj[i][j]*di)%26
        return adj
    if len(M) == 3:
        d = (M[0][0]*(M[1][1]*M[2][2] - M[2][1]*M[1][2]) - M[0][1]*(M[1][0]*M[2][2]- M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])) %26
        if d == 0:
            print('**The key matrix has determinant zero**')
            exit()
        for i in range(26):
            if (d*i)%26 == 1:
                di = i
                break
        cof = [[0 for i in range(len(M))] for j in range(len(M[0]))]
        n = 1
        for i in range(3):
            for j in range(3):
                cof[i][j] = (M[(i+1)%3][(j+1)%3]*M[(i+2)%3][(j+2)%3] - M[(i+1)%3][(j+2)%3]*M[(i+2)%3][(j+1)%3])
        for i in range(3):
            for j in range(3):
                M[i][j] = (di*cof[j][i])%26
        return M
            
def rmcorrections(M, correction):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] in correction:
                M[i][j] = ''
                correction.remove(correction[0])
    return M

def encrypt(text):
    plaintext = text.upper().replace(' ','')
    n = 3
    K = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    plaintext, l, chk = chkptlength(plaintext, n)
    print(f'\nThe key matrix is {K}')
    P = matrixgen(plaintext, n, l)
    print(f'The plaintext matrix is {P}')
    P = tonumber(P, n, l)
    C = matrixmul(K, P)
    print(f'\nThe cipher matrix is {C}')
    cipher = tostring(toletter(C))
    print(f'The encoded text is {cipher}')
    return cipher, K, chk, C

def decrypt(cipher, C, K, chk):
    iK = imatrix(K)
    print(f'\nThe inverse key matrix is {iK}')
    D = matrixmul(iK, C)
    print(f'The decoded matrix is {D}')
    decipher = toletter(D)
    decipher = tostring(rmcorrections(decipher, chk))
    print(f'The decoded text is {decipher}')
    return decipher