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

class Comprobador:
    def __init__(self, lista_palabras, silencioso):
        self.pausa = 2
        self.palabras = lista_palabras
        self.palabras_encontradas = []
        self.palabras_no_encontradas = []
        self.silencioso = silencioso

        self.comprobar()
        if not self.silencioso:
            self.marcador()

    def comprobar(self):
        for palabra in self.palabras:
            sleep(self.pausa)

            try:
                urllib.request.urlopen("http://es.wikipedia.org/wiki/" + palabra)
                if not self.silencioso:
                    print("La palabra", palabra, "existe en Wikipedia")
                self.palabras_encontradas.append(palabra)
            except urllib.error.URLError:
                if not self.silencioso:
                    print("La palabra", palabra, "no existe en Wikipedia")
                self.palabras_no_encontradas.append(palabra)

    def marcador(self):
        print("\nEstadísticas:")
        print("Palabras encontradas:", len(self.palabras_encontradas))
        print("Palabras no encontradas:", len(self.palabras_no_encontradas))
        print("Total:", len(self.palabras))