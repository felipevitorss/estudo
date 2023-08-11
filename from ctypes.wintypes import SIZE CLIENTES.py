from ctypes.wintypes import SIZE
from optparse import Values
import PySimpleGUI as sg
import sqlite3 as bbb

#criar a conexão e interage com o banco
conn = bbb.connect("Desktop/FelipeVitor/clientes.db")
c = conn.cursor()

#criar o layout
layout = [
    [sg.Button("Cadastrar")],
    [sg.Button("Fornecedores")],
    [sg.Button("Transportadora")]
]

font_programa = ('Arial',25)

#criar  a janela principal e chamar os componentes desta na janela
#WINDOW  (nome da janela, componentes, tamanho da janela)
window = sg.Window("Sistema de cadastro de clientes",layout,size=(1024,728),font=font_programa,resizable=True)

#Se o programa for executado, abra a janela
while True:
    event, values = window.read()

    #Se a janela for fechada
    if event == sg.WINDOW_CLOSED:

        break

    #CADASTRO DE CLIENTES 
    if event == "Cadastrar":
        
        #criar layout
        clientes_layout = [
            [sg.Text("Nome")],
            [sg.InputText(key="Nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Text("Endereco")],
            [sg.InputText(key="Endereco")],
            [sg.Text("Telefone")],
            [sg.InputText(key="Telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="Cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        clientes_window = sg.Window ("Cadastro de Clientes",clientes_layout,size = (1024,728))

        while True:
            event, values = clientes_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                clientes_window.close()
                break

            #interação com o banco
            c.execute("INSERT INTO clientes (Nome, CPF, Endereco, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)", (values["Nome"], values["CPF"], values["Endereco"], values["Telefone"], values["Cidade"], values["Estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            clientes_window["Nome"].update("")
            clientes_window["CPF"].update("")
            clientes_window["Endereco"].update("")
            clientes_window["Telefone"].update("")
            clientes_window["Cidade"].update("")
            clientes_window["Estado"].update("")
        

            #configurar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")


        #CADASTRO DOS FORNECEDORES 
    elif event == "Fornecedores":
        
         Fornecedores_layout = [
            [sg.Text("ID_Fornecedor")],
            [sg.InputText(key="ID_Fornecedor")],
            [sg.Text("Nome_Fornecedor")],
            [sg.InputText(key="Nome_Fornecedor")],
            [sg.Text("Endereco_Fornecedor")],
            [sg.InputText(key="Endereco_Fornecedor")],
            [sg.Text("Telefone_Fornecedor")],
            [sg.InputText(key="Telefone_Fornecedor")],
            [sg.Text("Cidade_Fornecedor")],
            [sg.InputText(key="Cidade_Fornecedor")],
            [sg.Text("Estado_Fornecedor")],
            [sg.InputText(key="Estado_Fornecedor")],
            [sg.Text("Pais_Fornecedor")],
            [sg.InputText(key="Pais_Fornecedor")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

         Fornecedores_window = sg.Window("Cadastro de Fornecedores",Fornecedores_layout,size = (1024,728))

         while True:
            event, values = Fornecedores_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                Fornecedores_window.close()
                break

            #interação com o banco
            c.execute("INSERT INTO Fornecedores (ID_Fornecedor, Nome_Fornecedor, Endereco_Fornecedor, Telefone_Fornecedor, Cidade_Fornecedor, Estado_Fornecedor, Pais_Fornecedor) VALUES (?, ?, ?, ?, ?, ?, ?)", (values["ID_Fornecedor"], values["Nome_Fornecedor"], values["Endereco_Fornecedor"], values["Telefone_Fornecedor"], values["Cidade_Fornecedor"], values["Estado_Fornecedor"], values["Pais_Fornecedor"]))
            conn.commit()

            #Limpar iputs após o cadastro
            Fornecedores_window["ID_Fornecedor"].update("")
            Fornecedores_window["Nome_Fornecedor"].update("")
            Fornecedores_window["Endereco_Fornecedor"].update("")
            Fornecedores_window["Telefone_Fornecedor"].update("")
            Fornecedores_window["Cidade_Fornecedor"].update("")
            Fornecedores_window["Estado_Fornecedor"].update("")
            Fornecedores_window["Pais_Fornecedor"].update("")

            #configurar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")


        #CADASTRO DAS TRANSPORTADORAS
    elif event == "Transportadora":

         Transportadora_layout = [
            [sg.Text("ID_Transportadora")],
            [sg.InputText(key="ID_Transportadora")],
            [sg.Text("Nome_Transportadora")],
            [sg.InputText(key="Nome_Transportadora")],
            [sg.Text("Telefone_Transportadora")],
            [sg.InputText(key="Telefone_Transportadora")],
            [sg.Text("Telefone")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]


         Transportadora_window = sg.Window ("Cadastro de Transportadoras",Transportadora_layout,size = (1024,728))

         while True:
            event, values = Transportadora_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                Transportadora_window.close()
                break
            
            #interação com o banco
            c.execute("INSERT INTO Transportadora (ID_Transportadora, Nome_Transportadora, Telefone_Transportadora) VALUES (?, ?, ? )", (values["ID_Transportadora"], values["Nome_Transportadora"], values["Telefone_Transportadora"]))
            conn.commit()

            #Limpar iputs após o cadastro
            Transportadora_window["ID_Transportadora"].update("")
            Transportadora_window["Nome_Transportadora"].update("")
            Transportadora_window["Telefone_Transportadora"].update("")
            
            #configurar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")
          
           
conn.close()