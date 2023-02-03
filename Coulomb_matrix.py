import pandas as pd
from scipy.spatial import distance_matrix
    
data = [[26.49,31.78,30.51], [28.3,31.68,30.31], [26.55,33.57,30.61]]
atoms = ['O', 'Ha', 'Hb']
df = pd.DataFrame(data, columns=['x', 'y', 'z'], index=atoms)
print(f"The input positions of three atoms : \n{df}\n")

dis_matrix = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
print(f"The distance matrix is : \n{dis_matrix}\n")

Zi = [8,1,1]
res = pd.DataFrame()

for i in range(3):
    for j in range(3):
        if i == j:                          #diagonal, i == j
            res.loc[i,j] = Zi[i] * Zi[j]
        else:                               #others, i!=j
            res.loc[i,j] = (Zi[i] * Zi[j])/dis_matrix.iloc[i][j]


print(f"Coulomb matrix looks like follows: \n {res}\n")