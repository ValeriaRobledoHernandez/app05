import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value = f"Tu IMC es de: {imc:.2f}"
        page.update()
        
        
        page.dialog.open=True
        page.update()
        
    except ValueError:
        page.dialog.open=False
        page.update()

    def cerrar_dialogo(e):
    
        page.dialog.open=False
        page.update()    

        if imc<18.5:
            ft.AlertDialog(
                title=ft.Text("Bajo de peso"),
                content=ft.Text("Tu IMC indica que tienes bajo peso"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        elif imc>=18.5 and imc<24.9:
            ft.AlertDialog(
                title=ft.Text("Peso normal"),
                content=ft.Text("Tu IMC indica que tienes peso normal"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        elif imc>=25 and imc<30:
            ft.AlertDialog(
                title=ft.Text("Sobrepeso"),
                content=ft.Text("Tu IMC indica que tienes sobrepeso "),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        else:
            ft.AlertDialog(
                title=ft.Text("Obesidad"),
                content=ft.Text("Tu IMC indica que tienes Obesidad, acude a tu médico"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        
        
            
        
        
def main(page: ft.Page):
    page.title="Calculadora de IMC"
    page.bgcolor="purple"
    txtPeso=ft.TextField(label="Ingresa tu peso: ")
    txtAltura=ft.TextField(label="Ingresa tu altura: ")
    lblIMC=ft.Text("Tu IMC es de: ")
    img=ft.Image(
        src="Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    def btnCalcular(event):
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
        
        
        page.dialog.open=True
        
        
    def Limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value="Tu IMC es de: "
        page.update()
    
    
    btnCalcular=ft.ElevatedButton(text="Calcular")
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
