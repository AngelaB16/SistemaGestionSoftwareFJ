import tkinter as tk
from tkinter import ttk, messagebox

from modelos.reserva import Reserva


class VistaReservas:

    def __init__(self, frame, sistema):

        self.frame = frame
        self.sistema = sistema

    
        # Titulo
    

        titulo = tk.Label(
            frame,
            text="GESTIÓN DE RESERVAS",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

    
        # Formulario
    

        formulario = tk.LabelFrame(
            frame,
            text="Datos de la Reserva",
            padx=15,
            pady=15
        )

        formulario.pack(fill="x", padx=20)

        # Codigo

        tk.Label(
            formulario,
            text="Código"
        ).grid(row=0, column=0, sticky="w")

        self.codigo = tk.Entry(
            formulario,
            width=30
        )

        self.codigo.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )

        # Cliente

        tk.Label(
            formulario,
            text="Cliente"
        ).grid(row=1, column=0, sticky="w")

        self.combo_cliente = ttk.Combobox(
            formulario,
            width=28,
            state="readonly"
        )

        self.combo_cliente.grid(
            row=1,
            column=1,
            padx=10,
            pady=5
        )

        # Servicio

        tk.Label(
            formulario,
            text="Servicio"
        ).grid(row=2, column=0, sticky="w")

        self.combo_servicio = ttk.Combobox(
            formulario,
            width=28,
            state="readonly"
        )

        self.combo_servicio.grid(
            row=2,
            column=1,
            padx=10,
            pady=5
        )

        # Duración

        tk.Label(
            formulario,
            text="Duración"
        ).grid(row=3, column=0, sticky="w")

        self.duracion = tk.Entry(
            formulario,
            width=30
        )

        self.duracion.grid(
            row=3,
            column=1,
            padx=10,
            pady=5
        )

        # Botones

        botones = tk.Frame(frame)

        botones.pack(pady=10)

        tk.Button(
            botones,
            text="Registrar",
            width=15,
            command=self.registrar_reserva
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botones,
            text="Confirmar",
            width=15,
            command=self.confirmar_reserva
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botones,
            text="Cancelar",
            width=15,
            command=self.cancelar_reserva
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botones,
            text="Eliminar",
            width=15,
            command=self.eliminar_reserva
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            botones,
            text="Limpiar",
            width=15,
            command=self.limpiar
        ).grid(row=0, column=4, padx=5)

    
        # Tabla
    

        columnas = (
            "codigo",
            "cliente",
            "servicio",
            "duracion",
            "estado",
            "total"
        )

        self.tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("cliente", text="Cliente")
        self.tabla.heading("servicio", text="Servicio")
        self.tabla.heading("duracion", text="Duración")
        self.tabla.heading("estado", text="Estado")
        self.tabla.heading("total", text="Costo Total")

        self.tabla.column("codigo", width=80, anchor="center")
        self.tabla.column("cliente", width=180)
        self.tabla.column("servicio", width=180)
        self.tabla.column("duracion", width=80, anchor="center")
        self.tabla.column("estado", width=100, anchor="center")
        self.tabla.column("total", width=120, anchor="e")

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_reserva
        )

        self.frame.bind("<Visibility>", self.actualizar_datos)

    def actualizar_datos(self, event=None):

        self.cargar_clientes()
        self.cargar_servicios()

    # Cargar clientes

    def cargar_clientes(self):

        clientes = self.sistema.obtener_clientes()

        self.combo_cliente["values"] = [
            f"{c.codigo} - {c.nombre}"
            for c in self.sistema.obtener_clientes()
        ]

    # Cargar servicios

    def cargar_servicios(self):

        servicios = self.sistema.obtener_servicios()

        self.combo_servicio["values"] = [
            f"{s.codigo} - {s.nombre}"
            for s in self.sistema.obtener_servicios()
        ]


    # Registrar reserva



    def registrar_reserva(self):

        self.cargar_clientes()
        self.cargar_servicios()

        try:

            codigo = self.codigo.get()
            nombre_cliente = self.combo_cliente.get()
            nombre_servicio = self.combo_servicio.get()
            duracion = int(self.duracion.get())

            cliente = None
            codigo_cliente = self.combo_cliente.get().split(" - ")[0]
            codigo_servicio = self.combo_servicio.get().split(" - ")[0].strip()

            for c in self.sistema.obtener_clientes():

                if str(c.codigo).strip() == codigo_cliente:
                    cliente = c
                    break

            servicio = None

            for s in self.sistema.obtener_servicios():

                if str(s.codigo).strip() == codigo_servicio:
                    servicio = s
                    break

            if cliente is None:

                raise Exception(
                    "Debe seleccionar un cliente."
                )

            if servicio is None:

                raise Exception(
                    "Debe seleccionar un servicio."
                )

            reserva = Reserva(
                codigo,
                cliente,
                servicio,
                duracion
            )

            self.sistema.agregar_reserva(
                reserva
            )

            self.tabla.insert(
                "",
                "end",
                values=(
                    reserva.codigo,
                    cliente.nombre,
                    servicio.nombre,
                    reserva.duracion,
                    reserva.estado,
                    reserva.costo_total()
                )
            )

            messagebox.showinfo(
                "Éxito",
                "Reserva registrada correctamente."
            )

            self.limpiar()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # Seleccionar reserva

    def seleccionar_reserva(self, event):

        seleccion = self.tabla.focus()

        if not seleccion:
            return

        datos = self.tabla.item(
            seleccion
        )["values"]

        self.limpiar()

        self.codigo.insert(
            0,
            datos[0]
        )

        self.combo_cliente.set(
            datos[1]
        )

        self.combo_servicio.set(
            datos[2]
        )

        self.duracion.insert(
            0,
            datos[3]
        )

    # Confirmar

    def confirmar_reserva(self):

        seleccion = self.tabla.focus()

        if not seleccion:

            messagebox.showwarning(
                "Advertencia",
                "Seleccione una reserva."
            )

            return

        codigo = str(
            self.tabla.item(seleccion)["values"][0]
        )

        self.sistema.confirmar_reserva(codigo)

        datos = list(
            self.tabla.item(seleccion)["values"]
        )

        datos[4] = "Confirmada"

        self.tabla.item(
            seleccion,
            values=datos
        )

        messagebox.showinfo(
            "Éxito",
            "Reserva confirmada."
        )

    # Cancelar

    def cancelar_reserva(self):

        seleccion = self.tabla.focus()

        if not seleccion:

            messagebox.showwarning(
                "Advertencia",
                "Seleccione una reserva."
            )

            return

        codigo = str(
            self.tabla.item(seleccion)["values"][0]
        )

        self.sistema.cancelar_reserva(codigo)

        datos = list(
            self.tabla.item(seleccion)["values"]
        )

        datos[4] = "Cancelada"

        self.tabla.item(
            seleccion,
            values=datos
        )

        messagebox.showinfo(
            "Éxito",
            "Reserva cancelada."
        )

    # Eliminar

    def eliminar_reserva(self):

        seleccion = self.tabla.focus()

        if not seleccion:

            messagebox.showwarning(
                "Advertencia",
                "Seleccione una reserva."
            )

            return

        codigo = str(
            self.tabla.item(seleccion)["values"][0]
        )

        self.sistema.eliminar_reserva(codigo)

        self.tabla.delete(
            seleccion
        )

        messagebox.showinfo(
            "Éxito",
            "Reserva eliminada correctamente."
        )

    # Limpiar

    def limpiar(self):

        self.codigo.delete(
            0,
            tk.END
        )

        self.duracion.delete(
            0,
            tk.END
        )

        self.combo_cliente.set("")

        self.combo_servicio.set("")