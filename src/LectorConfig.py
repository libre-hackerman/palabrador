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


class LectorConfig:
    def __init__(self):
        # Diccionarios de probabilidad
        self.prob_vocales = {}
        self.prob_consonantes = {}

        # Rutas de archivos
        self.fichero_prob_vocales = "reglas/prob_vocales.rl"
        self.fichero_prob_consonantes = "reglas/prob_consonantes.rl"

        # Carga de probabilidades
        self.cargar_prob_vocales()
        self.cargar_prob_consonantes()

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
