import pandas as pd

datos = {'Nombre':['Alice', 'Bob' ,'Charly'],
         'Edad':[25, 30, 35],
         'Ciudad':['A', 'B', 'C']}

df = pd.DataFrame(datos)
print(df)
