import random
import string
#Bienvenida locknova
print("Bienvenido a Locknova generador de constraseña seguro y personalizado")
#contraseña personalizada
Mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZK"
Minusculas="abcdefghijklmnopqrstuvwxyz"
Numeros="0123456789"
Simbolos="!@#$%^&*()_-+=<>?/"
Longitud_corta=("6 caracteres")
Longitud_larga=("16 caracteres")
#Opciones para incluir en la contraseña
print("¿Qué deseas incluir en tu contraseña?")
incluir_mayusculas = input("¿Incluir mayúsculas? si/no: ").lower()
incluir_minusculas = input("¿Incluir minúsculas? si/no: ").lower()
incluir_numeros = input("¿Incluir números? si/no: ").lower()
incluir_simbolos = input("¿Incluir símbolos? si/no: ").lower()
#Longitud de contraseña
Longitud=int(input(f"Deseas que tu contraseña sea de {Longitud_corta} o {Longitud_larga}:"))
#Que eligio el usuario con if y else
Opciones_incluidas_en_la_contraseña = ""

if incluir_mayusculas == "si":
    Opciones_incluidas_en_la_contraseña += string.ascii_uppercase
if incluir_minusculas == "si":
    Opciones_incluidas_en_la_contraseña += string.ascii_lowercase
if incluir_numeros == "si":
    Opciones_incluidas_en_la_contraseña += string.digits
if incluir_simbolos == "si":
    Opciones_incluidas_en_la_contraseña += string.punctuation
#Validar que este seleccionado por lo menos una de las enterires opciones
if Opciones_incluidas_en_la_contraseña == "":
    print("Debes escoger por lo menos una opción para poder avanzar.")
else:
    contraseña = ""
    for i in range(Longitud):
        contraseña += random.choice(Opciones_incluidas_en_la_contraseña)
    # Mostrar contraseña
    print("Tu contraseña ha sido generada con éxito:")
    print(contraseña)