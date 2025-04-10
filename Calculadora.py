import flet 

def main(page: flet.Page):
    page.title = 'Calculadora'
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.height = 500


    todos_valores =""


    resultado_texto = flet.Text(value="0", size=28, color="white", text_align="right" )

    def entrar_valores(e):
        nonlocal todos_valores 
        todos_valores+= str(e.control.text)
        resultado_texto.value = todos_valores
        page.update()

    def limpar_tela(e):
        nonlocal todos_valores 
        todos_valores = ""
        resultado_texto.value = "0"
        page.update()

    def calcular(e):
        nonlocal todos_valores
        try:
            resultado_texto.value = str(eval(todos_valores)) 
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = "Error"
            todos_valores = ""
        page.update()





    display = flet.Container(
        content = resultado_texto,
        bgcolor = "#27474f", 
        padding=10,
        border_radius=10,
        height=70,
        alignment=flet.alignment.center_right


        )
    
    estilo_numeros = {
        "height" :60,
        "bgcolor" : "gray" ,
        "color" : "" ,
        "expand" :1, 
    }

    estilo_operadores = {
        "height" :60,
        "bgcolor" : "Orange" ,
        "color" : "" ,
        "expand" :1, 
    }

    estilo_limpar = {
        "height" :60,
        "bgcolor" : "Green" ,
        "color" : "" ,
        "expand" :1, 
    }

    estilo_igual = {
        "height" :60,
        "bgcolor" : "Green" ,
        "color" : "" ,
        "expand" :1, 
    }

    grelha_de_botoes = [

       [
           ("C" ,estilo_limpar,limpar_tela),
           ("%" ,estilo_operadores,entrar_valores),
           ("/" ,estilo_operadores, entrar_valores),
           ("*" ,estilo_operadores,entrar_valores)
        ], 

        [
           ("7" ,estilo_numeros,entrar_valores),
           ("8" ,estilo_numeros,entrar_valores),
           ("9" ,estilo_numeros,entrar_valores),
           ("-" ,estilo_operadores,entrar_valores)
        ], 

        [
           ("4" ,estilo_numeros,entrar_valores),
           ("5" ,estilo_numeros,entrar_valores),
           ("6" ,estilo_numeros,entrar_valores),
           ("+" ,estilo_operadores,entrar_valores)
        ], 

        [
           ("1" ,estilo_numeros,entrar_valores),
           ("2" ,estilo_numeros,entrar_valores),
           ("3" ,estilo_numeros,entrar_valores),
           ("=" ,estilo_igual,calcular)
        ], 

        [
           ("0" , {**estilo_numeros, "expand" :2},entrar_valores),
           ("." ,estilo_numeros,entrar_valores),
           ("<" ,estilo_operadores, lambda e: None)
        ], 

        
    ]

    botoes = []
    
    for linha in grelha_de_botoes:
        linha_control = []
        for texto, estilo, handler in linha:
            btn = flet.ElevatedButton(
                    text=texto,
                    on_click=handler,
                    **estilo, 
                    style=flet.ButtonStyle(
                        shape=flet.RoundedRectangleBorder(radius=5),
                        padding=0)

                )
            linha_control.append(btn)
        botoes.append(flet.Row(linha_control, spacing=5))   

    

    page.add(
        flet.Column(
            [
               display, 
               flet.Column(botoes, spacing=5)
            ]
            )
    )

flet.app(target=main)

