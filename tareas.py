import os

# --- ZONA DE FUNCIONES (HERRAMIENTAS) ---

def cargar_tareas():
    # Esta función busca si existe un archivo de respaldo
    if os.path.exists("tareas.txt"):
        archivo = open("tareas.txt", "r") # "r" es Read (Leer)
        contenido = archivo.read()
        archivo.close()
        
        # Si el archivo tiene texto, lo convertimos en lista
        if contenido:
            return contenido.split(",") 
    
    return [] # Si no existe archivo, devolvemos lista vacía

def guardar_tareas(lista_tareas):
    # Esta función abre el archivo y guarda lo que haya en la lista
    archivo = open("tareas.txt", "w") # "w" es Write (Escribir)
    texto = ",".join(lista_tareas) # Une la lista con comas
    archivo.write(texto)
    archivo.close()


# --- INICIO DEL PROGRAMA ---

# 1. En lugar de empezar vacíos, cargamos lo que haya en el archivo
tareas = cargar_tareas() 

while True:
    print("\n--- GESTOR DE TAREAS (CON MEMORIA) ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nueva_tarea = input("¿Qué tienes que hacer?: ")
        tareas.append(nueva_tarea)
        
        # ¡GUARDAMOS DE INMEDIATO!
        guardar_tareas(tareas) 
        print("✅ Tarea guardada en el disco duro.")

    elif opcion == "2":
        print("\n📝 TUS TAREAS:")
        if len(tareas) == 0:
            print("📭 Tu lista está vacía.")
        else:
            for tarea in tareas:
                print(f"- {tarea}")

    elif opcion == "3":
        tarea_a_borrar = input("Nombre exacto de la tarea a borrar: ")
        if tarea_a_borrar in tareas:
            tareas.remove(tarea_a_borrar)
            
            # ¡GUARDAMOS EL CAMBIO!
            guardar_tareas(tareas)
            print("🗑️ Tarea eliminada permanentemente.")
        else:
            print("⚠️ Esa tarea no existe.")

    elif opcion == "4":
        print("¡Guardando y saliendo... Hasta luego!")
        break

    else:
        print("Opción no válida.")