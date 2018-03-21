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

import sys
import os

class LectorConfig:
    def __init__(self, diccionarios, probabilidades):
        # Índices de probabilidad
        self.prob_vocales = {}
        self.prob_consonantes = {}

        # Diccionarios
        self.libros = {}

        # Rutas de probabilidades
        self.fichero_prob_vocales = "reglas/prob_vocales.rl"
        self.fichero_prob_consonantes = "reglas/prob_consonantes.rl"

        # Ruta del directorio de diccionarios
        self.directorio_libros = "libros/"

        # Carga de probabilidades
        if probabilidades:
            self.cargar_prob_vocales()
            self.cargar_prob_consonantes()

        # Carga de la lista de diccionarios
        if diccionarios:
            self.cargar_libros()

    def cargar_prob_vocales(self):
        separador = ":"

        try:
            flujo_lectura = open(self.fichero_prob_vocales, mode="r", encoding="utf-8")
            lineas = flujo_lectura.readlines()

            for l in lineas:
                vocal = l.split(separador)[0]
                probabilidad = int(l.split(separador)[1])
                self.prob_vocales.update({vocal: probabilidad})

        except FileNotFoundError:
            # Escribe en stderr
            print("No existe el archivo", self.fichero_prob_vocales, file=sys.stderr)
            sys.exit(2)

    def cargar_prob_consonantes(self):
        separador = ":"

        try:
            flujo_lectura = open(self.fichero_prob_consonantes, mode="r", encoding="utf-8")
            lineas = flujo_lectura.readlines()

            for l in lineas:
                consonante = l.split(separador)[0]
                probabilidad = int(l.split(separador)[1])
                self.prob_consonantes.update({consonante: probabilidad})

        except FileNotFoundError:
            # Escribe en stderr
            print("No existe el archivo", self.fichero_prob_consonantes, file=sys.stderr)
            sys.exit(2)

    def cargar_libros(self):
        archivos = os.listdir(self.directorio_libros)
        for a in archivos:
            if os.path.isfile(self.directorio_libros + a):
                palabras = self.leer_libro(self.directorio_libros + a)
                self.libros.update({a: palabras})

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
