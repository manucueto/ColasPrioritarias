import flet as ft
import simpy
import time

class Cliente:
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre

def main(page: ft.Page):
    # Inicializamos la simulación
    env = simpy.Environment()


    # Creamos un diccionario para mapear las opciones del menú desplegable a valores enteros
    tipo_cliente_map = {
        "Cliente Tipo 0 (baja prioridad)": 0,
        "Cliente Tipo 1 (mediana prioridad)": 1,
        "Cliente Tipo 2 (alta prioridad)": 2,
    }

    # Creamos una lista para almacenar los clientes
    cola_clientes = []

    def agregar_cliente(e):
        # Obtenemos la opción seleccionada del menú desplegable
        opcion_seleccionada = color_dropdown.value

        # Obtenemos el tipo de cliente según el mapeo
        tipo_cliente = tipo_cliente_map.get(opcion_seleccionada, 0)

        # Creamos un nuevo cliente con un nombre único
        nuevo_cliente = Cliente(tipo_cliente, f"C{len(cola_clientes) + 1}")

        # Agregamos el cliente a la cola
        cola_clientes.append(nuevo_cliente)

        # Actualizamos la lista de clientes
        actualizar_lista_clientes()
        page.update()

    def actualizar_lista_clientes():
        # Generamos una cadena con la lista de clientes en orden inverso
        lista_clientes_str = " -- ".join(f"{cliente.nombre} (Tipo {cliente.tipo})" for cliente in reversed(cola_clientes))
        lista_clientes_text.value = lista_clientes_str

    def limpiar(e):
        # Limpiamos la lista de clientes
        cola_clientes.clear()
        # Actualizamos la lista de clientes
        actualizar_lista_clientes()
        page.update()

    def simular_cola(e):
          # Tomamos el primer cliente de la lista
        # Evaluamos la lista de clientes y atendemos a los clientes según su prioridad
        for i in range(len(cola_clientes)-1, -1, -1):
            cliente_actual = cola_clientes[i]
            if (cliente_actual.tipo == 2):
                # Atendemos al cliente de tipo 2
                time.sleep(3)
                output_text.value = f"Cliente {cliente_actual.nombre} fue atendido."
                cola_clientes.remove(cliente_actual)
                actualizar_lista_clientes()
                page.update()
        for i in range(len(cola_clientes)-1, -1, -1):
            cliente_actual = cola_clientes[i]
            if (cliente_actual.tipo == 1):
                # Atendemos al cliente de tipo 1
                time.sleep(3)
                output_text.value = f"Cliente {cliente_actual.nombre} fue atendido."
                cola_clientes.remove(cliente_actual)
                actualizar_lista_clientes()
                page.update()
        for i in range(len(cola_clientes)-1, -1, -1):
            cliente_actual = cola_clientes[i]
            if (cliente_actual.tipo == 0):
                # Atendemos al cliente de tipo 0
                time.sleep(3)
                output_text.value = f"Cliente {cliente_actual.nombre} fue atendido."
                cola_clientes.remove(cliente_actual)

                actualizar_lista_clientes()
                page.update()

        # Mostramos mensaje de finalización
        time.sleep(3)
        actualizar_lista_clientes()
        limpiar()
        output_text.value = "Simulación de la cola terminada."
        time.sleep(3)
        page.update()
        output_text.value = ""
        page.update()

    output_text = ft.Text()
    lista_clientes_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Agregar Cliente", on_click=agregar_cliente)
    simulate_btn = ft.ElevatedButton(text="Simular Cola", on_click=simular_cola)
    limpiar_btn = ft.ElevatedButton(text="Limpiar", on_click=limpiar)
    color_dropdown = ft.Dropdown(
        width=1240,
        options=[
            ft.dropdown.Option("Cliente Tipo 0 (baja prioridad)"),
            ft.dropdown.Option("Cliente Tipo 1 (mediana prioridad)"),
            ft.dropdown.Option("Cliente Tipo 2 (alta prioridad)"),
        ],
    )

    # Crear una fila con los botones
    button_row = ft.Row([submit_btn, simulate_btn], alignment=ft.MainAxisAlignment.CENTER)
    button_clean = ft.Row([limpiar_btn], alignment=ft.MainAxisAlignment.CENTER)
    page.add(color_dropdown, button_row, lista_clientes_text, output_text, button_clean)

ft.app(target=main)
