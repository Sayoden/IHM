import random

sizeBoard = int(input("Donnez moi la taille du plateau : "))
nbBomb = int(input("Combien de bombes : "))

def generateMatrix(n,m,v):
    mat = []
    for i in range(n):
        tmp = []
        for i in range(m):
            tmp.append(v)
        mat.append(tmp)
    return mat

def generateBomb(mat:[], k):
    randCond = 0
    while randCond < k:
        rand = random.randint(0, len(mat) - 1)
        randInMat = random.randint(0, len(mat[rand]) - 1)
        if mat[rand][randInMat] != 0:
            mat[rand][randInMat] = 1
            randCond += 1
        print(randCond)
    return mat

mb = generateMatrix(sizeBoard, sizeBoard, 0)
db = generateMatrix(sizeBoard, sizeBoard, 0)

print(generateBomb(mb, nbBomb))


