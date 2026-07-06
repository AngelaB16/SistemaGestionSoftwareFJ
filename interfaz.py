# Interfaz principal del Sistema Software FJ

import tkinter as tk
from tkinter import ttk

from vistas.clientes import VistaClientes

class InterfazPrincipal:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Sistema Integral de Gestión - Software FJ")
        self.ventana.geometry("1100x700")
        self.ventana.resizable(False, False)

        # Notebook (Pestañas)
        self.notebook = ttk.Notebook(self.ventana)

        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)
        self.tab_reservas = ttk.Frame(self.notebook)
        self.tab_reportes = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_servicios, text="Servicios")
        self.notebook.add(self.tab_reservas, text="Reservas")
        self.notebook.add(self.tab_reportes, text="Reportes")

        self.notebook.pack(expand=True, fill="both")
        
        # Cargar la vista
        self.vista_clientes = VistaClientes(self.tab_clientes)

        # Barra de estado
        estado = tk.Label(
            self.ventana,
            text="Sistema listo",
            anchor="w",
            relief="sunken"
        )

        estado.pack(fill="x", side="bottom")

    def ejecutar(self):
        self.ventana.mainloop()