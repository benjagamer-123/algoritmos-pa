import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import numpy as np
import os

df = pd.read_csv("FutbolLiga.csv")

ff = pd.read_csv("UltimaFecha.csv")

print("Tabla completa:")
print(df.head(10))
print("-" * 83)

print("Fecha Final:")
print(ff.head(10))
print("-" * 116)

print(df.info())
print("-" * 83)

print(ff.info())

#Dia -> Objet. Pasar a int

ff['Dia'] = ff['Dia'].str.replace(' de Diciembre', '.12').astype(float) 

print(ff.head(10))
print("-" * 116)
print(ff.info())
print("-" * 116)

ff['Goleadores'] = ff['Goleadores'].fillna('No hubo gol')

print(ff.head(10))
print("-" * 116)

#10 equipos con mas goles a favor

OrdenPorgoles = df.sort_values(by='GF', ascending=False)

print(OrdenPorgoles.head(10))
print("-" * 83)

#"grafico"

plt.bar(df['Equipos'], df['GF'], color='skyblue')
plt.title('Equipos y sus Goles a Favor')
plt.xlabel('Equipos')
plt.ylabel('Goles a Favor')
plt.show()

#10 equipos con mas goles en contra

OrdenPorgolesC = df.sort_values(by='GC', ascending=False)

print(OrdenPorgolesC.head(10))
print("-" * 83)

plt.bar(df['Equipos'], df['GC'], color='Red')
plt.title('Equipos y sus Goles en contra')
plt.xlabel('Equipos')
plt.ylabel('Goles recibidos')
plt.show()

#"grafico"

#Mas partidos ganados

OrdenPorgolesC = df.sort_values(by='Ganados', ascending=False)

print(OrdenPorgolesC.head(10))
print("-" * 83)

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

bins = range(0, 60, 10)

plt.hist(df['Puntos'], bins=bins, color='skyblue', edgecolor='black')

plt.xticks(range(0, 60, 10))

plt.title('Distribución de puntajes del torneo')
plt.xlabel('Rangos de puntaje')
plt.ylabel('Cantidad de equipos')
plt.grid(axis='y', alpha=0.75)
plt.show()

def generar_informe(df, nombre_pdf="informe_liga.pdf"):
    """Genera un informe PDF con estadísticas y un histograma del DataFrame."""

    # --- 1. Calcular estadísticas ---
    media = df['Puntos'].mean()
    mediana = df['Puntos'].median()
    desviacion = df['Puntos'].std()
    minimo = df['Puntos'].min()
    maximo = df['Puntos'].max()

    # --- 2. Crear y guardar histograma de puntos ---
    bins = range(int(minimo), int(maximo) + 10, 10)
    plt.figure(figsize=(8, 5))
    plt.hist(df['Puntos'], bins=bins, color='skyblue', edgecolor='black')
    plt.title('Distribución de puntajes de la Liga')
    plt.xlabel('Rangos de puntaje')
    plt.ylabel('Cantidad de equipos')
    plt.grid(axis='y', alpha=0.75)
    plt.xticks(bins)
    plt.tight_layout()

    # Guardar el gráfico en la misma carpeta que el script
    ruta_imagen = os.path.join(os.getcwd(), "histograma.png")
    plt.savefig(ruta_imagen)
    plt.close()

    # --- 3. Crear y guardar grafico de barras de goles ---

    bins = range(int(10), int(10) + 10, 10)
    plt.bar(df['Equipos'], df['GC'], color='Red')
    plt.title('Equipos y sus Goles en contra')
    plt.xlabel('Equipos')
    plt.ylabel('Goles recibidos')

    # Guardar el gráfico en la misma carpeta que el script
    ruta_imagen2 = os.path.join(os.getcwd(), "histograma2.png")
    plt.savefig(ruta_imagen2)
    plt.close()

    # --- 3. Crear PDF ---
    estilos = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Informe de Resultados de la Liga</b>", estilos["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Estadísticas Generales:</b>", estilos["Heading2"]))
    story.append(Paragraph(f"Media: {media:.2f}", estilos["Normal"]))
    story.append(Paragraph(f"Mediana: {mediana:.2f}", estilos["Normal"]))
    story.append(Paragraph(f"Desviación estándar: {desviacion:.2f}", estilos["Normal"]))
    story.append(Paragraph(f"Puntaje mínimo: {minimo}", estilos["Normal"]))
    story.append(Paragraph(f"Puntaje máximo: {maximo}", estilos["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Gráfico de distribución de puntajes:</b>", estilos["Heading2"]))
    story.append(Spacer(1, 12))
    story.append(Image(ruta_imagen, width=400, height=250))
    story.append(Image(ruta_imagen2, width=400, height=250))
    story.append(Spacer(1, 24))

    pdf = SimpleDocTemplate(nombre_pdf, pagesize=A4)
    pdf.build(story)

    print(f"Informe generado correctamente: {nombre_pdf}")


generar_informe(df)
