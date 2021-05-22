from ctypes import windll, Structure, c_long, byref
from time import sleep
from tkinter import *
from tkinter import Frame

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

class mapa(Frame):

    def __init__(self):
        
        self.window = Tk()
        self.window.title('MAPEAMENTO')
        self.window.geometry('250x250')

        lbl = Label(text="MAPEAMENTO DA CIDADE:")
        lbl.pack()

        #POSIÇÃO
        self.etPos = Entry(font='Courier 12')
        self.etPos.pack()

        self.lblPosAtual = Label(font='Courier 12', fg='red')
        self.lblPosAtual.pack()

        #BOTAO PARA GERAR CÓDIGO
        btCod = Button(text='GERAR CÓDIGO HTML', command=lambda: setCod())
        btCod.pack()

        #INFOS
        lblTitulo = Label(text='Titulo:')
        lblTitulo.pack()

        etTitulo = Entry()
        etTitulo.pack()

        lblLink = Label(text='Link:')
        lblLink.pack()

        etLink = Entry()
        etLink.pack()

        lblCod = Label(text="CÓDIGO HTML:")
        lblCod.pack()

        self.etCodigo = Entry(font='Courier 12')
        self.etCodigo.pack()

        def setCod():

            codigo = '<area title="{}" shape="poly" alt="Part" coords="{}" href="{}"/>'.format(etTitulo.get(), self.etPos.get(), etLink.get(), )
            self.etCodigo.insert(0, codigo)

            etLink.delete(0, END)
            etTitulo.delete(0, END)

        #AO PRESSIONAR P DISPARAR O EVENTO
        self.window.bind("<KeyPress-p>", self.keyPressed)

        self.window.mainloop()

    def queryMousePosition(self):
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": pt.x-5, "y": pt.y+510 }

    def keyPressed(self, event):
        l = event.keysym

        if l == 'p':
            #ATIVAR EVENTO
            pos = self.queryMousePosition()

            #EXIBIR POSIÇÃO SELECIONADA
            self.lblPosAtual['text'] = "X=" + str(pos["x"]) + " Y:" + str(pos["y"])

            #GUARDAR POSIÇÃO
            self.etPos.insert(0, str(pos["x"]) + "," + str(pos["y"]) + ",")

mapa()