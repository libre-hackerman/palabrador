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

from random import randint


class Palabra:
    def __init__(self, l):
        # ‱ de aparición (1/10000)
        self.vocales_10000 = {"a": 2780,
                              "e": 3035,
                              "i": 1387,
                              "o": 1926,
                              "u": 872}
        self.consonantes_10000 = {"b": 258,
                                  "c": 850,
                                  "d": 1064,
                                  "f": 125,
                                  "g": 183,
                                  "h": 127,
                                  "j": 80,
                                  "k": 4,
                                  "l": 902,
                                  "m": 572,
                                  "n": 1218,
                                  "p": 456,
                                  "q": 160,
                                  "r": 1248,
                                  "s": 1449,
                                  "t": 841,
                                  "v": 163,
                                  "w": 2,
                                  "x": 40,
                                  "y": 163,
                                  "z": 94}
        self.longitud = l
        self.palabra = ""

        # Piscinas (sacos, tómbolas, bolsas... ya me entiendes)
        self.vocales_pool = []
        self.consonantes_pool = []
        self.llenar_pool()

    def llenar_pool(self):
        # Llenado de vocales
        for vocal, probabilidad in self.vocales_10000.items():
            for i in range(0, probabilidad):
                self.vocales_pool.append(vocal)
        # Llenado de consonantes
        for consonante, probabilidad in self.consonantes_10000.items():
            for i in range(0, probabilidad):
                self.consonantes_pool.append(consonante)

    def generar(self):
        self.palabra = ""
        for i in range(0, self.longitud):
            if i % 2 == 0:
                factor_probabilidad = randint(0, 100)
                # Probabilidad aumentada al final de la palabra de "n" y "s"
                if factor_probabilidad < 50 or i < self.longitud-1:
                    self.palabra += self.consonantes_pool[randint(
                        0, len(self.consonantes_pool)-1)]
                elif factor_probabilidad < 75:
                    self.palabra += "n"
                else:
                    self.palabra += "s"
            else:
                self.palabra += self.vocales_pool[randint(
                    0, len(self.vocales_pool)-1)]

    def nueva(self):
        self.generar()
        return self.palabra
