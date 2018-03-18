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
from tkinter import messagebox

class Ventana1:
    def __init__(self, palabras, longitud, comprobar, archivo, numerar):
        # Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Generador de Palabras")

        # Favicon
        python_ico = ImageTk.PhotoImage(file='img/python.gif')
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, python_ico)

        # Elecciones
        self.archivo_salida = tk.StringVar()
        self.n_palabras = tk.StringVar()
        self.longitud = tk.StringVar()
        self.wikipedia = tk.IntVar()
        self.numerar = tk.IntVar()

        # Valores por defecto
        self.archivo_salida.set(archivo)
        self.n_palabras.set(str(palabras))
        self.longitud.set(str(longitud))
        self.wikipedia.set(int(comprobar))
        self.numerar.set(int(numerar))

        # Etiquetas
        self.etiqueta_archivo = tk.Label(self.ventana, text="Archivo de salida")
        self.etiqueta_n_palabras = tk.Label(self.ventana, text="Nº de palabras")
        self.etiqueta_longitud = tk.Label(self.ventana, text="Longitud")
        self.etiqueta_wikipedia = tk.Label(self.ventana, text="Buscar en Wikipedia")
        self.etiqueta_numerar = tk.Label(self.ventana, text="Numerar archivo")

        # Cuadros de texto
        self.entrada_archivo = tk.Entry(self.ventana, textvariable=self.archivo_salida, width=25)
        self.entrada_n_palabras = tk.Entry(self.ventana, textvariable=self.n_palabras, width=3)
        self.entrada_longitud = tk.Entry(self.ventana, textvariable=self.longitud, width=3)

        # Checkbuttons
        self.checkbutton_wikipedia = tk.Checkbutton(self.ventana, variable=self.wikipedia, onvalue=1, offvalue=0)
        self.checkbutton_numerar = tk.Checkbutton(self.ventana, variable=self.numerar, onvalue=1, offvalue=0)

        # Botón
        self.boton_generar = tk.Button(self.ventana, text="Generar", command=self.comprobar_datos, activebackground="cyan")

        # Posicionador
        self.posicionador()

    def posicionador(self):
        # Etiquetas
        self.etiqueta_archivo.grid(row=1, column=1, sticky=tk.E, padx=4, pady=3)
        self.etiqueta_n_palabras.grid(row=2, column=1, sticky=tk.E, padx=4, pady=3)
        self.etiqueta_longitud.grid(row=3, column=1, sticky=tk.E, padx=4, pady=3)
        self.etiqueta_wikipedia.grid(row=4, column=1, sticky=tk.E, padx=4, pady=3)
        self.etiqueta_numerar.grid(row=5, column=1, sticky=tk.E, padx=4, pady=3)

        # Cuadros de texto
        self.entrada_archivo.grid(row=1, column=2, sticky=tk.W)
        self.entrada_n_palabras.grid(row=2, column=2, sticky=tk.W)
        self.entrada_longitud.grid(row=3, column=2, sticky=tk.W)

        # Checkbutton
        self.checkbutton_wikipedia.grid(row=4, column=2, sticky=tk.W)
        self.checkbutton_numerar.grid(row=5, column=2, sticky=tk.W)

        # Botón
        self.boton_generar.grid(row=6, column=2, sticky=tk.E, padx=4, pady=4)

        self.ventana.protocol("WM_DELETE_WINDOW", sys.exit)
        self.ventana.mainloop()

    def comprobar_datos(self):
        try:
            if int(self.longitud.get()) > 0 and int(self.n_palabras.get()) > 0:
                self.ventana.destroy()
            else:
                self.datos_incorrectos()
        except ValueError:
            self.datos_incorrectos()

    def datos_incorrectos(self):
        messagebox.showerror("Error", "Datos incorrectos")