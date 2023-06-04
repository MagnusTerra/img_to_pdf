import os
import img2pdf

def convertir_imagenes_a_pdf(carpeta):
    imagenes = []
    
    # Obtener todas las imágenes de la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".webp"):
            imagenes.append(os.path.join(carpeta, archivo))
        elif archivo.endswith(".jpg"):
            imagenes.append(os.path.join(carpeta, archivo))
        elif archivo.endswith(".png"):
            imagenes.append(os.path.join(carpeta, archivo))

    # Crear el archivo PDF
    with open("imagenes.pdf", "wb") as pdf:
        pdf.write(img2pdf.convert(imagenes))
    
    print("Archivo PDF creado con éxito.")

# Ejemplo de uso
convertir_imagenes_a_pdf("Carpeta")
