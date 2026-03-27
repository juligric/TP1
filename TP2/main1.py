def inicio():
    print(" Iniciando sistemas...")
    print("Bienvenido")
    nombre = input("Ingrese el nombre del Capitán/a: ")
    print(f"Saludos, Capitán/a {nombre}")
    return nombre  

def calcular_combustible(carga_base, reserva=50):
    total = carga_base + reserva
    print(f"Combustible total: {total}")

def chequeo_sistema(nombre, nivel):
    if nivel >= 70:
        return "OPERATIVO"
    else:
        return "FALLIDO"

def calcular_estadisticas(aprobados, fallidos):
    total = aprobados + fallidos
    if total > 0:
        porcentaje = (aprobados / total) * 100
    else:
        porcentaje = 0
    return total, porcentaje

capitan = inicio()

cantidad = int(input("¿Cuántos sistemas desea verificar?: "))

operativos = 0
fallidos = 0

for i in range(cantidad):
    nombre_sistema = input("Nombre del sistema: ")
    
    while True:
        nivel = int(input("Nivel de energía (0-100): "))
        if 0 <= nivel <= 100:
            break
        else:
            print("Error: el nivel debe estar entre 0 y 100")

    estado = chequeo_sistema(nombre_sistema, nivel)
    print(f"{nombre_sistema}: {estado}")

    if estado == "OPERATIVO":
        operativos += 1
    else:
        fallidos += 1

total, porcentaje = calcular_estadisticas(operativos, fallidos)


carga = int(input("Ingrese la carga base: "))

usar_reserva = input("¿Desea ingresar reserva? (s/n): ")

if usar_reserva == "s":
    reserva = int(input("Ingrese la reserva: "))
    calcular_combustible(carga, reserva)
else:
    calcular_combustible(carga)

# --- REPORTE FINAL ---
print("--- REPORTE FINAL ---")
print(f"Total de sistemas revisados: {total}")
print(f"Porcentaje de éxito: {porcentaje:.2f}%")
print(f"Misión finalizada. Buen trabajo, Capitán/a {capitan} ")