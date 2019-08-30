#DADOS DA MATRIZ:
n=int(input('Número de linhas das matrizes: '))
m= int(input('Número de colunas das matrizes: '))

#INICIALIZANDO UMA MATRIZ:
M=[[0]*n,[0]*m]

#OPERAÇÃO:
for i in range (n): 
    for j in range (m): 
        M[i][j]=float(input('Elemento linha %i, coluna %i: ' %(i+1,j+1)))

maior= M[0][0]
for i in range (n):
    for i in range (m):
        if M[i][j]>maior:
            maior=M[i][j]

print (maior)


