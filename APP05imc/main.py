import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu imc es de: {imc:.2f}"
        page.update()
        
    #funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()

    #validacion del IMC
        if imc<18.5:
        
            dialog=ft.AlertDialog(
            title="bajo de peso",
            content="Tu IMC indica que tienes bajo peso",
            actions=[
                ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
            ]
        )
        elif imc>=18.5 and imc<24.9:
            dialog=ft.AlertDialog(
        
        title="peso normal",
        content="Tu IMC indica que tienes un peso normal",
        actions=[
            ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
        ]
    )
        elif imc>=25 and imc<30:
            dialog=ft.AlertDialog(
                title="sobrepeso",
                content="Tu IMC indica que tienes un peso normal",
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
        elif imc>=25 and imc<30:
            dialog=ft.AlertDialog(
        title="sobrepeso",
        content="Tu IMC indica que tienes un peso normal",
        actions=[
            ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
        ]
    )

        page.dialog=dialog
        page.dialog.open=True
        page.update()
        
    except ValueError:
        page.dialog.open = False
        page.update()

def main(page: ft.Page):
    page.title = "calculadora de IMC"
    page.bgcolor = "#03e4f4"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("tu IMC es de: ")
    
    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def on_calcular(e):
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
        
    def Limpiar (e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value="Tu IMC es de: "
        page.update()
        
    
    btncalcular=ft.ElevatedButton(text="Calcular",on_click="on_calcular")
    btnlimpiar=ft.ElevatedButton(text="Calcular",on_click="limpiar")
    
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
                btncalcular,btnlimpiar
            ],alignment="CENTER")
    )
    
    
    
    
    
ft.app(main,view=ft.AppView.WEB_BROWSER)