def segmentador_correo(correo):
    nombre_usuario, dominio = correo.split('@')[0], correo.split('@')[1]
    return nombre_usuario, dominio

def verificar_dominio_personalizado(dominio):
    dominios_populares = ["gmail.com", "yahoo.com", "hotmail.com"]
    if dominio.lower() in dominios_populares:
        return False
    else:
        return True

def mensaje_final(nombre_usuario, dominio):
    if verificar_dominio_personalizado(dominio):
        return f"Hey {nombre_usuario.capitalize()}, parece que tienes tu propia configuración personalizada en {dominio.capitalize()}. ¡Impresionante!"
    else:
        return f"Hey {nombre_usuario.capitalize()}, veo que tu correo está registrado con {dominio.capitalize()}. ¡Eso es genial!"

def main():
    correo = input("Ingrese su dirección de correo electrónico: ")
    nombre_usuario, dominio = segmentador_correo(correo)
    mensaje = mensaje_final(nombre_usuario, dominio)
    print(mensaje)

if __name__ == "__main__":
    main()
