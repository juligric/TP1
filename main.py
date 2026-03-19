# Fase 1 
print("¡Bienvenido al cofre mágico!")

nombre_explorador = input("¿Cuál es tu nombre, explorador? ")

nivel_valentia = int(input("En una escala del 1 al 10, ¿cuál es tu nivel de valentía? "))

monedas = int(input("¿Cuántas monedas de oro llevás en tu mochila? "))


# Fase 2
monedas_con_regalo = monedas + 15
print(f"Si abris el cofre tendrias {monedas_con_regalo} monedas de oro ")


# Fase 3 
nombre_programador = "Juli"  

if nombre_explorador == nombre_programador:
    print("¡Bienvenido, creador! El tesoro es tuyo sin preguntas")
else:
    if nivel_valentia > 7:
        print("Eres digno. ¡Podés pasar!")
    elif nivel_valentia >= 4:
        print("Me servís como guardia, pero no para el tesoro")
    else:
        print("¡Corré antes de que sea tarde!")


# Fase 4
edad = int(input("Antes de abrir el cofre ¿cuántos años tenés? "))

if edad > 18 and monedas_con_regalo > 100:
    print("¡COFRE ABIERTO!")
else:
    print("¡ACCESO DENEGADO!")