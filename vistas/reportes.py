import tkinter as tk


class VistaReportes:

    def __init__(self, frame, sistema):

        self.sistema = sistema
        self.frame = frame

        titulo = tk.Label(
            frame,
            text="REPORTES DEL SISTEMA",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        self.texto = tk.Text(
            frame,
            width=100,
            height=25,
            font=("Consolas", 10)
        )

        self.texto.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        btn = tk.Button(
            frame,
            text="Generar Reporte",
            width=20,
            command=self.generar_reporte
        )

        btn.pack(pady=10)

    def generar_reporte(self):

        self.texto.delete("1.0", tk.END)

        clientes = self.sistema.obtener_clientes()
        servicios = self.sistema.obtener_servicios()
        reservas = self.sistema.obtener_reservas()

        confirmadas = 0
        canceladas = 0
        pendientes = 0
        ingresos = 0

        for reserva in reservas:

            if reserva.estado == "Confirmada":
                confirmadas += 1

            elif reserva.estado == "Cancelada":
                canceladas += 1

            else:
                pendientes += 1

            ingresos += reserva.costo_total()

        reporte = ""

        reporte += "=====================================\n"
        reporte += "   SOFTWARE FJ - REPORTE GENERAL\n"
        reporte += "=====================================\n\n"

        reporte += f"Clientes registrados : {len(clientes)}\n"
        reporte += f"Servicios registrados: {len(servicios)}\n"
        reporte += f"Reservas registradas : {len(reservas)}\n\n"

        reporte += "Estado de Reservas\n"
        reporte += "------------------------------\n"
        reporte += f"Confirmadas : {confirmadas}\n"
        reporte += f"Pendientes  : {pendientes}\n"
        reporte += f"Canceladas  : {canceladas}\n\n"

        reporte += f"Ingresos estimados : ${ingresos:,.2f}\n\n"

        reporte += "=========== CLIENTES ===========\n"

        for cliente in clientes:

            reporte += (
                f"{cliente.codigo} - "
                f"{cliente.nombre} - "
                f"{cliente.documento}\n"
            )

        reporte += "\n=========== SERVICIOS ===========\n"

        for servicio in servicios:

            reporte += (
                f"{servicio.codigo} - "
                f"{servicio.nombre} - "
                f"${servicio.calcular_costo():,.2f}\n"
            )

        reporte += "\n=========== RESERVAS ===========\n"

        for reserva in reservas:

            reporte += (
                f"{reserva.codigo} | "
                f"{reserva.cliente.nombre} | "
                f"{reserva.servicio.nombre} | "
                f"{reserva.estado} | "
                f"${reserva.costo_total():,.2f}\n"
            )

        self.texto.insert(
            tk.END,
            reporte
        )