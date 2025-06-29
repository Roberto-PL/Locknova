import random
import string
# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n🔐 Bienvenido a LockNova - Generador de Contraseñas")
        print("\n¿Que metodo deseas usar? ")
        print("1. Generar contraseña personalizada")
        print("2. Generar contraseña con palabra base")
        print("3. Salir")

        opcion = input("Elige una opción (1/2/3): ").strip()
        if opcion == "1":
            generar_contraseña_personalizada()
        elif opcion == "2":
            generar_contraseña_con_palabra_base()
        elif opcion == "3":
            print(" Gracias por usar LockNova.")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")

# Método 1: Contraseña personalizada
def generar_contraseña_personalizada():
    print("\n Generador de Contraseña Personalizada")
    Mayusculas = string.ascii_uppercase
    Minusculas = string.ascii_lowercase
    Numeros = string.digits
    Simbolos = string.punctuation

    print("¿Qué deseas incluir en tu contraseña?")
    incluir_mayusculas = input("¿Incluir mayúsculas? si/no: ").strip().lower()
    incluir_minusculas = input("¿Incluir minúsculas? si/no: ").strip().lower()
    incluir_numeros = input("¿Incluir números? si/no: ").strip().lower()
    incluir_simbolos = input("¿Incluir símbolos? si/no: ").strip().lower()

    # Validación de longitud
    while True:
        try:
            longitud = int(input("¿6 o 16 caracteres?: "))
            if longitud in (6, 16):
                break
            else:
                print(" Solo puedes ingresar 6 o 16. Intenta nuevamente.")
        except ValueError:
            print(" Ingresa un número válido.")

    opciones = ""
    if incluir_mayusculas == "si":
        opciones += Mayusculas
    if incluir_minusculas == "si":
        opciones += Minusculas
    if incluir_numeros == "si":
        opciones += Numeros
    if incluir_simbolos == "si":
        opciones += Simbolos

    if opciones == "":
        print("Debes seleccionar al menos una opción con “Sí”.")
        return

    contraseña = "".join(random.choice(opciones) for _ in range(longitud))

    print("\n Tu contraseña ha sido generada con éxito:")
    print(contraseña)

    guardar = input("¿Guardar en archivo .txt? si/no: ").strip().lower()
    if guardar == "si":
        with open("contraseña_generada.txt", "w") as archivo:
            archivo.write("Contraseña personalizada: " + contraseña)
        print("📁 Guardada en 'contraseña_generada.txt'.")

# Método 2: Contraseña con palabra base
def generar_contraseña_con_palabra_base():
    print("\n Generador con Palabra Base")
    palabra_base = input("Ingresa una palabra base: ").strip()
    if palabra_base == "":
        print(" No ingresaste nada.")
        return
    if not any(c.isalpha() for c in palabra_base):
        print(" La palabra base debe contener al menos una letra.")
        return

    sustituciones = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 'l': '|'}
    caracteres = list(palabra_base)

    for i in range(len(caracteres)):
        letra = caracteres[i].lower()
        if letra in sustituciones:
            caracteres[i] = sustituciones[letra]

    simbolos_extra = ('!', '#', '%', '&')
    caracteres.append(random.choice(simbolos_extra))
    random.shuffle(caracteres)
    contraseña = ''.join(caracteres)

    if not any(c.isalpha() for c in contraseña):
        print(" No quedan letras en la contraseña. Usa otra palabra base.")
        return

    print("\n Tu contraseña ha sido generada con éxito:")
    print(contraseña)

    guardar = input("¿Guardar en archivo .txt? si/no: ").strip().lower()
    if guardar == "si":
        with open("contraseña_generada.txt", "w") as archivo:
            archivo.write("Contraseña con palabra base: " + contraseña)
        print("📁 Guardada en 'contraseña_generada.txt'.")







