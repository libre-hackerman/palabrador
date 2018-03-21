import os
from time import time

class LectorLibros:
    def __init__(self):
        # Diccionario de libros {fichero: lista_palabras}
        self.libros = {}

        # Tiempo de carga
        self.tiempo_carga = 0

        # Ruta del directorio de diccionarios
        self.directorio_libros = "libros/"

        self.cargar_libros()

    def cargar_libros(self):
        t1 = time()
        archivos = os.listdir(self.directorio_libros)
        for a in archivos:
            if os.path.isfile(self.directorio_libros + a):
                palabras = self.leer_libro(self.directorio_libros + a)
                self.libros.update({a: palabras})
        self.tiempo_carga = time() - t1

    def leer_libro(self, libro):
        palabras = []
        flujo_lectura = open(libro, mode="r", encoding="UTF-8")
        for linea in flujo_lectura:
            # [: -1] omite el último carácter (\n)
            for palabra in linea.lower()[:-1].split(" "):
                palabras.append(self.de_acentar(palabra))
        flujo_lectura.close()
        return palabras

    def de_acentar(self, original):
        nueva = ""
        for letra in original:
            if letra == "á":
                nueva += "a"
            elif letra == "é":
                nueva += "e"
            elif letra == "í":
                nueva += "i"
            elif letra == "ó":
                nueva += "o"
            elif letra == "ú" or letra == "ü":
                nueva += "u"
            else:
                nueva += letra
        return nueva