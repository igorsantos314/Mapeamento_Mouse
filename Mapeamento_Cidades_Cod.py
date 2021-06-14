from tkinter import *

class mapeamento:

    def __init__(self) -> None:
        
        dict_cidades = {}
        
        window = Tk()
        window.geometry('200x100')
        
        lblCod = Label(text='Código da Cidade:')
        lblCod.pack()

        etCod_Cidade = Entry()
        etCod_Cidade.pack()

        lblNome_Cidade = Label(text='Nome da Cidade')
        lblNome_Cidade.pack()

        etCidade = Entry()
        etCidade.pack()

        def add():
            city = f"{etCod_Cidade.get()}:'{etCidade.get().title()}',\n"

            arquivo = open('dict_mapeamento.txt', 'a')
            arquivo.write(city)
            arquivo.close()

            print(city)

            #limpar
            etCod_Cidade.delete(0, END)
            etCidade.delete(0, END)

        btAdicionar = Button(text='Add', command=add)
        btAdicionar.pack()

        window.mainloop()

mapeamento()