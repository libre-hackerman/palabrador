# Copyright (C) 2017 Esteban López | gnu_stallman (at) protonmail (dot) ch
#
# This file is part of Palabrador
#
# Palabrador is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#
# Palabrador is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

import urllib.request
from time import sleep
from src.LectorConfig import LectorConfig

class Comprobador:
    def __init__(self, lista_palabras, silencioso, wikipedia, diccionarios):
        self.pausa = 2
        self.palabras = lista_palabras
        self.silencioso = silencioso
        # Palabras de Wikipedia
        self.w_palabras_encontradas = []
        self.w_palabras_no_encontradas = []
        # Palabras de diccionarios
        self.d_palabras_encontradas = []
        self.d_palabras_no_encontradas = []

        if wikipedia:
            self.comprobar_wikipedia()

        if diccionarios:
            self.diccionarios = LectorConfig(True, False)  # Carga diccionarios, no probabilidades
            self.comprobar_diccionarios()

        if not self.silencioso:
            self.mostrar_marcador(wikipedia, diccionarios)

    def comprobar_wikipedia(self):
        for palabra in self.palabras:
            sleep(self.pausa)

            try:
                urllib.request.urlopen("http://es.wikipedia.org/wiki/" + palabra)
                if not self.silencioso:
                    print("La palabra", palabra, "existe en Wikipedia")
                self.w_palabras_encontradas.append(palabra)
            except urllib.error.URLError:
                self.w_palabras_no_encontradas.append(palabra)

    def comprobar_diccionarios(self):
        # Recorre la lista de palabras generadas
        for palabra in self.palabras:
            encontrada = False
            # Recorre la lista de libros
            for libro in self.diccionarios.libros.keys():
                # Recorre las palabras de cada libro
                for referencia in self.diccionarios.libros[libro]:
                    if palabra == referencia:
                        self.d_palabras_encontradas.append(palabra)
                        if not self.silencioso:
                            print("La palabra", palabra, "se ha encontrado en", libro)
                        encontrada = True
                        break  # Deja de buscar en el libro
                if encontrada:
                    break  # Evita que compruebe el siguiente libro
            if not encontrada:
                self.d_palabras_no_encontradas.append(palabra)

    def mostrar_marcador(self, wikipedia, diccionarios):
        if wikipedia:
            print("\nEstadísticas de Wikipedia:")
            print("Palabras encontradas:", len(self.w_palabras_encontradas))
            print("Palabras no encontradas:", len(self.w_palabras_no_encontradas))
        if diccionarios:
            print("\nEstadísticas de diccionarios:")
            print("Diccionarios usados:")
            for dic in self.diccionarios.libros.keys():
                print("-", dic)
            print("Palabras encontradas:", len(self.d_palabras_encontradas))
            print("Palabras no encontradas:", len(self.d_palabras_no_encontradas))
        print("Total de palabras:", len(self.palabras))
