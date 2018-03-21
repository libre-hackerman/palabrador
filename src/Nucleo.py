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
from src.Escritor import Escritor

class Nucleo:
    def __init__(self, args):
        if (args.escribir):
            self.generador = Palabra(args.longitud)
            self.lista_palabras = []

            # Generación de palabras pseudo-aleatorias
            for i in range(0, args.palabras):
                self.lista_palabras.append(self.generador.obtener_nueva())

            Escritor.escribir_archivo_todas(args.archivo, self.lista_palabras, args.numerar)

            if (args.wikipedia or args.diccionarios) and not args.interfaz:
                Comprobador(self.lista_palabras, False, args.wikipedia, args.diccionarios)
            elif args.interfaz:
                Ventana2(self.lista_palabras, args.wikipedia)