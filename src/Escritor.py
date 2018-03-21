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

from sys import stderr


class Escritor:
    archivo = ""
    numerar = ""
    @staticmethod
    def escribir_archivo_todas(lista_palabras):
        if Escritor.archivo != "" and Escritor.numerar != "":
            flujo_escritura = open(Escritor.archivo, mode="w", encoding="utf-8")
            for i in range(0, len(lista_palabras)):
                if Escritor.numerar:
                    flujo_escritura.write(str(i + 1) + " ")
                flujo_escritura.write(lista_palabras[i] + "\n")
            flujo_escritura.close()
        else:
            print("Decirle al genio que programó esto que mire la clase Escritor", file=stderr)

    @staticmethod
    def escribir_archivo_encontradas(lista_palabras):
        if Escritor.archivo != "" and Escritor.numerar != "":
            # Descartar repetidos
            lista_final = []
            for x in lista_palabras:
                if x not in lista_final:
                    lista_final.append(x)

            # Eliminar extensión .txt
            if Escritor.archivo.endswith(".txt"):
                archivo = Escritor.archivo[:-4]
            else:
                archivo = Escritor.archivo

            flujo_escritura = open(archivo+"_encontradas.txt", mode="w", encoding="utf-8")
            for i in range(0, len(lista_final)):
                if Escritor.numerar:
                    flujo_escritura.write(str(i + 1) + " ")
                flujo_escritura.write(lista_final[i] + "\n")
        else:
            print("Decirle al genio que programó esto que mire la clase Escritor", file=stderr)
