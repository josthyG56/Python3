# pip install colorama
"""
 la biblioteca colorama en Python.
 Colorama te permite cambiar los colores y
 estilos de texto en la consola. 
"""
from colorama import init, Fore, Style

# Inicializar colorama
"el siguiente texto impreso será en el color y estilo predeterminados de la consola"
init(autoreset=True)

# Solicitar al usuario que ingrese los datos
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electrónico: ")

# Imprimir con diferentes 
' Python 3.6 en adelate se usan las f-strings o literals strings'
print(f"{Style.BRIGHT}{Fore.RED}Nombre: {nombre}")
print(f"{Style.BRIGHT}{Fore.GREEN}Edad: {edad}")
print(f"{Fore.BLUE}Correo electrónico: {correo}")

# Fausto Joshua Ramirez Meza  372