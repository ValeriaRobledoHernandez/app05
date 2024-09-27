import flet as ft
from flet_core.types import WEB_BROWSER


def main(page: ft.Page):
    page.title="Calculadora de IMC"
    page.bgcolor="purple"
    txtPeso=ft.TextField(label="Ingresa tu peso: ")
    txtAltura=ft.TextField(label="Ingresa tu altura: ")
    lblIMC=ft.Text("Tu IMC es de: ")
    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    btnCalcular=ft.ElevatedButton(text="Calcular")#,on_click=calcular)
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    page.add(
        ft.Column(
            controls=[
                txtPeso,txtAltura,lblIMC
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,btnLimpiar
            ],alignment="CENTER")
        )
        
        
ft.app(target=main,view=ft.WEB_BROWSER)
