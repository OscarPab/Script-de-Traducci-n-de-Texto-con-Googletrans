from googletrans import Translator

def traducir_texto(texto, src='auto', dest='es'):
    # Crear una instancia del traductor
    traductor = Translator()
    
    # Traducir el texto
    traduccion = traductor.translate(texto, src=src, dest=dest)
    
    # Devolver el texto traducido
    return traduccion.text

# Solicitar al usuario el texto a traducir
texto_a_traducir = input("Introduce el texto que deseas traducir: ")

# Solicitar al usuario el idioma de destino
idioma_destino = input("Introduce el código del idioma de destino (por ejemplo, 'es' para español): ")

# Traducir el texto
texto_traducido = traducir_texto(texto_a_traducir, dest=idioma_destino)

# Mostrar el texto traducido
print(f"Texto traducido: {texto_traducido}")
