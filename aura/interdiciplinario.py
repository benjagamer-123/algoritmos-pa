import pandas as pd

df = pd.read_csv("FutbolLiga.csv")

ff = pd.read_csv("UltimaFecha.csv")

print("Tabla completa:")
print(df.head(10))
print("-" * 83)

print("Fecha Final:")
print(ff.head(10))
print("-" * 116)

print(df.info())

print(ff.info())

#Dia -> Objet. Pasar a int

ff['Dia'] = ff['Dia'].str.replace(' de Diciembre', '.12').astype(float) 

print(ff.head(10))
print(ff.info())

ff['Goleadores'] = ff['Goleadores'].fillna('No hubo gol')

print(ff.head(10))

#10 equipos con mas goles a favor

OrdenPorgoles = df.sort_values(by='GF', ascending=False)

print(OrdenPorgoles.head(10))

#"grafico"

#10 equipos con mas goles en contra

OrdenPorgolesC = df.sort_values(by='GC', ascending=False)

print(OrdenPorgolesC.head(10))

#"grafico"

#Mas partidos ganados

OrdenPorgolesC = df.sort_values(by='Ganados', ascending=False)

print(OrdenPorgolesC.head(10))

#"Grafico"

media = df['Puntos'].mean()
mediana = df['Puntos'].median()
desviacion_std = df['Puntos'].std()
minimo = df['Puntos'].min()
maximo = df['Puntos'].max()

print(f"Media de puntos (Promedio): {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar (Std): {desviacion_std:.2f}")
print(f"Puntaje Mínimo (Min): {minimo}")
print(f"Puntaje Máximo (Max): {maximo}")


