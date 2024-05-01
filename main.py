import flet as ft
import simpy

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

    def simular_cola(e):
        # Ejecutamos la simulación de la cola aquí
        # (debes implementar la lógica de la simulación)

        # Actualizamos el texto de salida
        output_text.value = "Simulación de la cola ejecutada."
        page.update()

    output_text = ft.Text()
    lista_clientes_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Agregar Cliente", on_click=agregar_cliente)
    simulate_btn = ft.ElevatedButton(text="Simular Cola", on_click=simular_cola)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Cliente Tipo 0 (baja prioridad)"),
            ft.dropdown.Option("Cliente Tipo 1 (mediana prioridad)"),
            ft.dropdown.Option("Cliente Tipo 2 (alta prioridad)"),
        ],
    )
    page.add(color_dropdown, submit_btn, simulate_btn, lista_clientes_text, output_text)

ft.app(target=main)