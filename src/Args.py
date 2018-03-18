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
import getopt
from src.Ventana1 import Ventana1

class Args:
    def __init__(self):
        # Valores por defecto
        self.palabras = 100
        self.archivo = "palabras.txt"
        self.longitud = 5
        self.numerar = False
        self.escribir = True
        self.comprobar = False
        self.interfaz = False

        self.extraer()

    def extraer(self):
        try:
            # [1:] omite el primer elemento
            opciones, argumentos = getopt.getopt(
                sys.argv[1:], "f:p:l:nwhg", ["help"])
            if len(argumentos) > 0:
                self.error("sintaxis", None)
            for opcion, argumento in opciones:
                if opcion == "-f":
                    self.archivo = argumento
                elif opcion == "-p":
                    try:
                        self.palabras = int(argumento)
                    except ValueError:
                        self.error("valor", argumento)
                elif opcion == "-l":
                    try:
                        self.longitud = int(argumento)
                    except ValueError:
                        self.error("valor", argumento)
                elif opcion == "-n":
                    self.numerar = True
                elif opcion == "-w":
                    self.comprobar = True
                elif opcion == "-g":
                    self.interfaz = True
                    v1 = Ventana1(self.palabras, self.longitud, self.comprobar, self.archivo, self.numerar)
                    self.palabras = int(v1.n_palabras.get())
                    self.longitud = int(v1.longitud.get())
                    self.comprobar = bool(v1.wikipedia.get())
                    self.numerar = bool(v1.numerar.get())
                    self.archivo = v1.archivo_salida.get()
                else:
                    self.ayuda()
                    self.escribir = False
        except getopt.GetoptError:
            self.error("sintaxis", None)

    def ayuda(self):
        print("""Bienvenido a GeneradordePalabrasAbsurdoAlaParQueInútil!
Argumentos:
\t-f archivo -> Seleccionar archivo de destino (defecto: palabras.txt)
\t-p N -> Seleccionar número de palabras (defecto: 100)
\t-l N -> Seleccionar longitud de las palabras (defecto: 5)
\t-n -> Numera las palabras
\t-w -> Busca la palabra en Wikipedia
\t-g -> Abrir interfaz gráfica
\t-h --help -> Muestra esta ayuda""")

    def error(self, tipo, arg):
        if tipo == "valor":
            print(arg, "no es un entero")
        else:
            print(sys.argv[0], "[-h] [[-f archivo] [-p Npalabras] [-l longitud] [-w] [-n]] [-g]")
        sys.exit(2)  # Sale con código de error 2