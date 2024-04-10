# Solicitar al usuario que ingrese los datos
# Datos capturados por el usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electrónico: ")

# Definicion de colores ANSI
"""
Los códigos de escape ANSI son secuencias especiales de caracteres 
que se utilizan para controlar aspectos específicos de la salida de
 texto en terminales y consolas que admiten el estándar ANSI 
 (American National Standards Institute). 
"""
# Definir códigos de escape ANSI
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
RESET_COLOR = "\033[0m"
NEGRITA = "\033[1m"

# Imprimir con diferentes 
' Python 3.6 en adelate se usan las f-strings o literals strings'
# Crear las cadenas formateadas con diferentes colores y negrita
nombre_formateado = f"{COLOR_ROJO}{NEGRITA}Nombre: {nombre}{RESET_COLOR}"
edad_formateada = f"{COLOR_VERDE}{NEGRITA}Edad: {edad}{RESET_COLOR}"
correo_formateado = f"{COLOR_AZUL}{NEGRITA}Correo electrónico: {correo}{RESET_COLOR}"

# Imprimir los datos capturados con diferentes colores
print(nombre_formateado)
print(edad_formateada)
print(correo_formateado)

"""
los códigos de escape ANSI permiten enviar instrucciones específicas 
 a la consola para controlar varios aspectos de la salida de texto, como
 el color, el estilo y la posición del cursor. Esto se logra enviando 
 secuencias especiales de caracteres que la consola puede interpretar y
 aplicar según sea necesario.
"""
# Fausto Joshua Ramirez Meza   372