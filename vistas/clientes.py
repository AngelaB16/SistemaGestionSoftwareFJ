# Vista de Clientes

import tkinter as tk
from tkinter import ttk


class VistaClientes:

    def __init__(self, frame):

        self.frame = frame

        # Titulo 

        titulo = tk.Label(
            frame,
            text="GESTIÓN DE CLIENTES",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        # Formulario 

        formulario = tk.LabelFrame(
            frame,
            text="Datos del Cliente",
            padx=15,
            pady=15
        )

        formulario.pack(fill="x", padx=20)

        # Codigo

        tk.Label(formulario, text="Código").grid(row=0, column=0, sticky="w")

        self.codigo = tk.Entry(formulario, width=30)

        self.codigo.grid(row=0, column=1, padx=10, pady=5)

        # Nombre

        tk.Label(formulario, text="Nombre").grid(row=1, column=0, sticky="w")

        self.nombre = tk.Entry(formulario, width=30)

        self.nombre.grid(row=1, column=1, padx=10, pady=5)

        # Documento

        tk.Label(formulario, text="Documento").grid(row=2, column=0, sticky="w")

        self.documento = tk.Entry(formulario, width=30)

        self.documento.grid(row=2, column=1, padx=10, pady=5)

        # Telefono

        tk.Label(formulario, text="Teléfono").grid(row=3, column=0, sticky="w")

        self.telefono = tk.Entry(formulario, width=30)

        self.telefono.grid(row=3, column=1, padx=10, pady=5)

        # Correo

        tk.Label(formulario, text="Correo")

        tk.Label(formulario, text="Correo").grid(row=4, column=0, sticky="w")

        self.correo = tk.Entry(formulario, width=30)

        self.correo.grid(row=4, column=1, padx=10, pady=5)

        # Botones

        botones = tk.Frame(frame)

        botones.pack(pady=10)

        tk.Button(botones, text="Registrar", width=15).pack(side="left", padx=5)

        tk.Button(botones, text="Limpiar", width=15).pack(side="left", padx=5)

        # Tabla 

        columnas = (
            "codigo",
            "nombre",
            "documento",
            "telefono",
            "correo"
        )

        self.tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("documento", text="Documento")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("correo", text="Correo")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=15)