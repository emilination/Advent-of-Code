
def triFusion(L):
    if len(L) == 1:
        return L
    else:
        return fusion( triFusion(L[:len(L)//2]) , triFusion(L[len(L)//2:]) )
    
def fusion(A,B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + fusion( A[1:] , B )
    else:
        return [B[0]] + fusion( A , B[1:] )
    
def q1(liste1,liste2):
    s = 0
    lis1 = triFusion(liste1)
    lis2 = triFusion(liste2)
    n = len(liste1)
    for i in range(n):
        s += abs(lis1[i]-lis2[i])
    return s

def q2(liste1,liste2):
    dico = {}
    n = len(liste1)
    s = 0
    for element in liste2:
        if element not in dico.keys():
            dico[element] = 1
        else:
            dico[element] += 1
    new1 = triFusion(liste1)
    if liste1[0] in dico.keys():
            s += dico[liste1[0]] * liste1[0]
    for i in range(1,n):
        if liste1[i] != liste1[i-1] and liste1[i] in dico.keys():
            s += dico[liste1[i]] * liste1[i]
    return s