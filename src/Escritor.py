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


class Escritor:
    @staticmethod
    def escribir_archivo_todas(archivo, lista_palabras, numerar):
        flujo_escritura = open(archivo, mode="w", encoding="utf-8")
        for i in range(0, len(lista_palabras)):
            if numerar:
                flujo_escritura.write(str(i + 1) + " ")
            flujo_escritura.write(lista_palabras[i] + "\n")
        flujo_escritura.close()

    @staticmethod
    def escribir_archivo_encontradas(archivo, lista_palabras, numerar):
        # Descartar repetidos
        lista_final = []
        for x in lista_palabras:
            if x not in lista_final:
                lista_final.append(x)

        flujo_escritura = open(archivo, mode="w", encoding="utf-8")
        for i in range(0, len(lista_final)):
            if numerar:
                flujo_escritura.write(str(i + 1) + " ")
            flujo_escritura.write(lista_final[i] + "\n")
