# Interfaz principal del Sistema Software FJ

import tkinter as tk
from tkinter import ttk
from sistema import Sistema
from vistas.clientes import VistaClientes
from vistas.servicios import VistaServicios
#from vistas.reservas import VistaReservas
#from vistas.reportes import VistaReportes

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
        
        self.sistema = Sistema()

        # Cargar la vista
        self.vista_clientes = VistaClientes(self.tab_clientes, self.sistema)
        self.vista_clientes = VistaServicios(self.tab_servicios, self.sistema)
        #self.vista_clientes = VistaReservas(self.tab_reservas, self.sistema)
        #self.vista_clientes = VistaReportes(self.tab_reportes, self.sistema)


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