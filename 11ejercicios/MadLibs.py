while True:
    
    sustantivo = input("Elige un sustantivo: ")
    sustantivo_plural = input("Elige un sustantivo en plural: ")
    sustantivo2 = input("Elige otro sustantivo: ")
    lugar = input("Dime un lugar: ")
    adjetivo = input("Elige un adjetivo (palabra que describe): ")
    sustantivo3 = input("Elige otro sustantivo: ")

    print("------------------------------------------")
    print("Sé amable con tu", sustantivo, "- de", sustantivo_plural)
    print("Porque un pato podría ser el", sustantivo2, "de alguien,")
    print("Sé amable con tus", sustantivo_plural, "en", lugar)
    print("Donde el clima siempre es", adjetivo, ".")
    print()
    print("Puedes pensar que esto es el", sustantivo3, ",")
    print("Bueno, lo es.")
    print("------------------------------------------")

    respuesta = input("¿Deseas jugar de nuevo? (Sí/No): ")
    if respuesta.lower() != 'si':
        break
