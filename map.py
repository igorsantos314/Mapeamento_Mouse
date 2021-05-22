from ctypes import windll, Structure, c_long, byref
from time import sleep
from tkinter import *
from tkinter import Frame

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

class mapa(Frame):

    def __init__(self):
        
        self.difX = 0
        self.difY = 0

        self.window = Tk()
        self.window.title('MAPEAMENTO')

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

        #CALIBRAGEM DE POSICIONAMENTO DA IMAGEM
        lblCalibragem = Label(text='Calibragem:')
        lblCalibragem.pack(pady=15)

        lblCalibragemX = Label(text="Digite o X:")
        lblCalibragemX.pack()

        self.etCalibX = Entry()
        self.etCalibX.pack()

        lblCalibragemY = Label(text="Digite o Y:")
        lblCalibragemY.pack()

        self.etCalibY = Entry()
        self.etCalibY.pack()

        btCod = Button(text='CALIBRAR', command=lambda: calib())
        btCod.pack()

        def calib():

            x = self.etCalibX.get().split()
            y = self.etCalibY.get().split()

            print(x)
            print(y)

            self.difX = int(x[0]) - int(x[1])
            self.difY = int(y[0]) - int(y[1])

            print(self.difX)
            print(self.difY)

            print('CALIBRADO COM SUCESSO !')

            self.etCalibX.delete(0, END)
            self.etCalibY.delete(0, END)

        #AO PRESSIONAR P DISPARAR O EVENTO
        self.window.bind("<F1>", self.keyPressed)
        self.window.bind("<KeyPress-c>", self.keyPressed)

        self.window.mainloop()

    def queryMousePosition(self, reset):

        if reset:
            #RESETAR CALIBRAGEM
            self.difX = 0
            self.difY = 0

        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": pt.x - self.difX, "y": pt.y - self.difY }

    def keyPressed(self, event):
        l = event.keysym

        if l == 'F1':
            #ATIVAR EVENTO
            pos = self.queryMousePosition(False)

            #EXIBIR POSIÇÃO SELECIONADA
            self.lblPosAtual['text'] = "X=" + str(pos["x"]) + " Y:" + str(pos["y"])

            #GUARDAR POSIÇÃO
            self.etPos.insert(END, str(pos["x"]) + "," + str(pos["y"]) + ",")

        elif l == 'c':
            #ATIVAR EVENTO
            pos = self.queryMousePosition(True)

            #INSERIR POSIÇÕES
            self.etCalibX.insert(0, str(pos["x"]))
            self.etCalibY.insert(0, str(pos["y"]))

mapa()