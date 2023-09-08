
bandas = []

def registro_agrupacion():
    id = input("Ingrese el ID de la banda: ")
    nombre = input("Ingrese el nombre de la banda: ")
    genero = input("Ingrese el género de la banda: ")
    hora_presentacion = input("Ingrese la hora de presentación (en formato HH:MM): ")
    pago = float(input("Ingrese el pago para la banda: "))
    estado = int(input("Ingrese el estado de la banda (True=1/False=0): "))
    banda = {"id": id, "nombre": nombre, "genero": genero, "hora_presentacion": hora_presentacion, "pago": pago, "estado": estado}
    bandas.append(banda)
    print("Banda registrada con éxito.")

def no_presentadas():
    print("Bandas que no se han presentado:")
    bandas_no_presentadas = 0 
    for banda in bandas:
        if not banda['estado']:
            print(f"ID: {banda['id']}, Nombre: {banda['nombre']}, Hora de presentación: {banda['hora_presentacion']} - No se ha presentado.")
            bandas_no_presentadas = 1
    if not bandas_no_presentadas:
        print("Todas las bandas ya se han presentado.")


def cambiar_hora_presentacion():
    id_buscar = input("Ingrese el ID de la banda la cual la hora de presentación desea cambiar: ")
    nueva_hora = input("Ingrese la nueva hora de presentación (en formato HH:MM): ")
    for banda in bandas:
        if banda["id"] == id_buscar and not banda["estado"]:
            banda["hora_presentacion"] = nueva_hora
            print("Hora de presentación actualizada con éxito.")
            return
    print("No se encontró la banda o ya se ha presentado.")


def retirar_agrupacion():
    id_retirar = input("Ingrese el ID de la banda que desea retirar: ")
    for banda in bandas:
        if banda["id"] == id_retirar and not banda["estado"]:
            bandas.remove(banda)
            print("Banda retirada con éxito.")
            return
    print("No se encontró la Banda o ya se ha presentado.")


while True:
    print("*****Festival de Música*****")
    print("\nMenú del Festival de Música:")
    print("1. Registrar banda")
    print("2. Mostrar bandas no presentadas")
    print("3. Cambiar hora de presentación")
    print("4. Retirar banda")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    if opcion == "1":
        registro_agrupacion()
    elif opcion == "2":
        no_presentadas()
    elif opcion == "3":
        cambiar_hora_presentacion()
    elif opcion == "4":
        retirar_agrupacion()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
