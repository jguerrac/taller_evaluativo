

def calcular_costo_salpicon(frutas):
    costo_total = 0
    for fruta in frutas:
        costo_total += fruta["precio_unitario"] * fruta["cantidad"]
    return costo_total

def frutas_ordenadas_por_costo(frutas):
    return sorted(frutas, key=lambda x: x["precio_unitario"] * x["cantidad"], reverse=True)

def fruta_economica_y_costosa(frutas):
    frutas.sort(key=lambda x: x["precio_unitario"])
    fruta_economica = frutas[0]
    fruta_costosa = frutas[-1]
    return fruta_economica, fruta_costosa

def main():
    print("SALPICONES CESDE")
    n = int(input("Ingrese la cantidad de frutas: "))
    frutas = []

    for i in range(n):
        id = i + 1
        nombre = input(f"Ingrese el nombre de la fruta {id}: ")
        precio_unitario = float(input(f"Ingrese el precio unitario de la fruta {id}: "))
        cantidad = int(input(f"Ingrese la cantidad de la fruta {id}: "))
        frutas.append({"id": id, "nombre": nombre, "precio_unitario": precio_unitario, "cantidad": cantidad})

    costo_total = calcular_costo_salpicon(frutas)
    print(f"El costo total del salpicón es: {costo_total}")

    frutas_ordenadas = frutas_ordenadas_por_costo(frutas)
    print("Frutas ordenadas por costo (de mayor a menor):")
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']}: {fruta['precio_unitario'] * fruta['cantidad']}")

    fruta_economica, fruta_costosa = fruta_economica_y_costosa(frutas)
    print(f"La fruta más economica es {fruta_economica['nombre']} con un precio de {fruta_economica['precio_unitario']}")
    print(f"La fruta más costosa es {fruta_costosa['nombre']} con un precio de {fruta_costosa['precio_unitario']}")

if __name__ == "__main__":
    main()
