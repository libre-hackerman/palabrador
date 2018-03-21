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
from src.LectorConfig import LectorConfig


class Palabra:
    def __init__(self, l):
        # Cargador de reglas de generación
        self.reglas = LectorConfig(False, True)  # Carga probabilidades, no diccionarios

        # ‱ de aparición
        self.vocales_10000 = self.reglas.prob_vocales
        self.consonantes_10000 = self.reglas.prob_consonantes
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
