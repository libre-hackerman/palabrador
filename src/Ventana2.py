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
import tkinter as tk
from PIL import ImageTk
from src.Comprobador import Comprobador

class Ventana2:
    def __init__(self, lista_palabras, comprobar):
        # Atributos recibidos por parámetros
        self.lista_palabras = lista_palabras
        self.comprobar = comprobar

        if self.comprobar:
            self.wiki = None  # Objeto comprobador
            self.cargando()

        # Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Generador de Palabras")

        # Favicon
        python_ico = ImageTk.PhotoImage(file='img/python.gif')
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, python_ico)

        # Cuadro de palabras
        self.frame_cuadro_palabras = tk.Frame(self.ventana)
        self.barra_vertical = tk.Scrollbar(self.frame_cuadro_palabras, orient=tk.VERTICAL, activebackground="cyan")
        self.barra_horizontal = tk.Scrollbar(self.frame_cuadro_palabras, orient=tk.HORIZONTAL, activebackground="cyan")
        self.cuadro_palabras = tk.Listbox(
            self.frame_cuadro_palabras, yscrollcommand=self.barra_vertical.set,
            xscrollcommand=self.barra_horizontal.set, width=10, height=8)
        self.barra_vertical.config(command=self.cuadro_palabras.yview)
        self.barra_horizontal.config(command=self.cuadro_palabras.xview)

        # Estadísticas:
        if self.comprobar:
            self.frame_cuadro_estadisticas = tk.Frame(self.ventana)

            self.etiqueta_total = tk.Label(self.frame_cuadro_estadisticas,
                                           text=("Total palabras: " + str(len(self.lista_palabras))))
            self.etiqueta_encontradas = tk.Label(self.frame_cuadro_estadisticas,
                                                 text=("Encontradas: " + str(len(self.wiki.palabras_encontradas))),
                                                 fg="green")
            self.etiqueta_no_encontradas = tk.Label(self.frame_cuadro_estadisticas,
                                                    text=(" No encontradas: " + str(len(self.wiki.palabras_no_encontradas))),
                                                    fg="red")
            imagen_wikipedia = ImageTk.PhotoImage(file="img/wiki_logo.png")
            self.etiqueta_wikipedia = tk.Label(self.frame_cuadro_estadisticas, image=imagen_wikipedia)

        # Botón
        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.destroy, activebackground="cyan")

        self.insertar_listbox()
        self.posicionador()

    def posicionador(self):
        # Cuadro de palabras
        self.frame_cuadro_palabras.grid(row=1, column=1, padx=5, pady=5)

        self.barra_vertical.pack(side=tk.RIGHT, fill=tk.Y)
        self.cuadro_palabras.pack(side=tk.TOP)
        self.barra_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

        # Estadísticas
        if self.comprobar:
            self.frame_cuadro_estadisticas.grid(row=1, column=2, padx=15, pady=5)
            self.etiqueta_total.grid(row=1, sticky=tk.E)
            self.etiqueta_encontradas.grid(row=2, sticky=tk.E)
            self.etiqueta_no_encontradas.grid(row=3, sticky=tk.E)
            self.etiqueta_wikipedia.grid(row=4, pady=10)

        self.boton_salir.grid(row=2, column=2, sticky=tk.E, padx=4, pady=4)

        self.ventana.protocol("WM_DELETE_WINDOW", sys.exit)
        self.ventana.mainloop()

    def insertar_listbox(self):
        for i in range(0, len(self.lista_palabras)):
            self.cuadro_palabras.insert(i, self.lista_palabras[i])
            # Color del texto
            if self.comprobar:
                if self.lista_palabras[i] in self.wiki.palabras_encontradas:
                    self.cuadro_palabras.itemconfig(i, fg="green")
                else:
                    self.cuadro_palabras.itemconfig(i, fg="red")

    def cargando(self):
        ventana = tk.Tk()
        ventana.title("Cargando")

        reloj = tk.Label(ventana, bitmap="hourglass")
        cargando = tk.Label(ventana, text="Buscando en Wikipedia...")
        reloj.pack(side=tk.LEFT)
        cargando.pack(side=tk.LEFT)

        # Uso update para que no se quede bloqueado en un mainloop
        # Actualizo varias veces porque parece que una sola vez
        # no siempre es suficiente para cargarlo completamente
        # Ya sé que es una chapuza. But works on my machine (usually)
        # TODO hacer una solución decente
        for i in range(0, 20):
            ventana.update()
        self.wiki = Comprobador(self.lista_palabras, True)
        ventana.destroy()