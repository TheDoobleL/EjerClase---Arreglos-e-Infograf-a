def crear_matriz(alumnos, materias):
    return [[0 for _ in range(materias)] for _ in range(alumnos)]


def mostrar_tabla(matriz, inicio, fin, materias):
    print("\n--- Tabla de Alumnos {} a {} ---".format(inicio + 1, fin))
  
    print("{:<12}|".format("Alumno"), end="")
    for i in range(materias):
        print("{:<12}|".format(f"Materia {i + 1}"), end="")
    print() 

   
    print("-" * (12 * (materias + 1) + 1))

   
    for i in range(inicio, fin):
        print("{:<12}|".format(f"Alumno {i + 1}"), end="")
        for j in range(materias):
            print("{:<12}|".format(matriz[i][j]), end="")
        print()  


def buscar_alumno(matriz, alumno, materias):
    if alumno < 1 or alumno > len(matriz):
        print("Error: El número de alumno no es válido.")
        return
    print(f"\n--- Información del Alumno {alumno} ---")
    print("Materia 5:", matriz[alumno - 1][4])  


def main():
    print("Bienvenido al sistema de gestión de alumnos y materias.")
    alumnos = int(input("Ingrese la cantidad de alumnos: "))
    materias = 6

    
    matriz = crear_matriz(alumnos, materias)

  
    for i in range(alumnos):
        for j in range(materias):
            matriz[i][j] = (i + j) % 101  

    
    num_tablas = (alumnos // 100) + (1 if alumnos % 100 != 0 else 0)
    print(f"\nSe han creado {num_tablas} tablas de 100 alumnos cada una.")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver una tabla de alumnos")
        print("2. Buscar un alumno en la Materia 5")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
           
            tabla = int(input(f"Ingrese el número de la tabla que desea ver (1-{num_tablas}): "))
            if tabla < 1 or tabla > num_tablas:
                print("Error: Número de tabla no válido.")
                continue
            inicio = (tabla - 1) * 100
            fin = min(inicio + 100, alumnos)
            mostrar_tabla(matriz, inicio, fin, materias)

        elif opcion == "2":
           
            alumno = int(input("Ingrese el número del alumno que desea buscar: "))
            buscar_alumno(matriz, alumno, materias)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if _name_ == "_main_":
    main()