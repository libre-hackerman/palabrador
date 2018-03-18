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

from src.Palabra import Palabra
from src.Comprobador import Comprobador
from src.Ventana2 import Ventana2

class Escritor:
    def __init__(self, args):
        if (args.escribir):
            self.generador = Palabra(args.longitud)
            self.lista_palabras = []

            self.flujo_escritura = open(
                args.archivo, mode="w", encoding="utf-8")
            self.escribir(args.palabras, args.numerar)
            self.flujo_escritura.close()
            if args.comprobar and not args.interfaz:
                Comprobador(self.lista_palabras, False)
            elif args.interfaz:
                Ventana2(self.lista_palabras, args.comprobar)

    def escribir(self, n, numerar):
        for i in range(0, n):
            self.lista_palabras.append(self.generador.nueva())

            if numerar:
                self.flujo_escritura.write(str(i+1) + " ")
            self.flujo_escritura.write(self.lista_palabras[i] + "\n")