
busquedaLineal = [10, 20, 30, 40, 50]

i = 0

numeroEncontrar = int(input("Buscar numero: "))

b = -1

for i in busquedaLineal:
    b = b+1
    if numeroEncontrar == i:
        print(f"se encontro en la casilla",b)
        break
    elif b == 4:
        print("tu numero no fue encontrado, prueba otra vez")