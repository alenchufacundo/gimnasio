import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.font import BOLD
import utilities.functions as utl
#al usar as, lo trata al archivo como un objeto donde se pueden acceder a las funciones de ella como metodos.

class MasterPanel:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Panel Administrador")
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (w,h))
        self.window.config(bg="#fcfcfc")
        self.window.resizable(width=0, height=0)

        #frame Izquierda
        self.frameLeft = tk.Frame(self.window, bd=0, width=500, relief=tk.SOLID, padx=10, pady=10, bg="#fcfcfc")
        self.frameLeft.pack(side="left", expand=tk.NO,fill=tk.BOTH)

        self.labelTitle = tk.Label(self.frameLeft, text="Panel de Administracion", font=('Times', 30), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.labelTitle.pack(fill=tk.X, padx=10, pady=100)
        
        self.loadInfoButton = tk.Button(self.frameLeft, text="Cargar alumnos", font=("Times", 15), bg='#3a7ff6', bd=0, fg="#fff")
        self.loadInfoButton.pack(fill=tk.X, padx=10, pady=20)

        self.showInfo = tk.Button(self.frameLeft, text="Mostrar estadisticas", font=("Times", 15), bg='#3a7ff6', bd=0, fg="#fff")
        self.showInfo.pack(fill=tk.X, padx=10, pady=40)


        #frame Derecha
        self.frameRight = tk.Frame(self.window, bd=0, width=500, relief=tk.SOLID, padx=10, pady=10, bg="#F3FAC4")
        self.frameRight.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #Entry barra de busqueda
        self.entrySearch = ttk.Entry(self.frameRight, font=('Times', 14), width=40)
        self.entrySearch.place(x=10,y=10)  

        self.btnSearch = tk.Button(self.frameRight, text="Buscar", font=("Times", 12), bg='#3a7ff6', bd=0, fg="#fff")
        self.btnSearch.pack(fill=tk.NONE, padx=10, pady=10)

        #lista de columnas
        self.labelNum = tk.Label(self.frameRight, text="Numero", font=("Times", 13), bg='#3a7ff6', bd=0, fg="#fff")
        self.labelNum.place(x=0,y=100)

        self.labelNom_Apel = tk.Label(self.frameRight, text="Nombre y Apellido", font=("Times", 13), bg='#3a7ff6', bd=0, fg="#fff")
        self.labelNom_Apel.place(x=70,y=100)
        
        self.labelSexo = tk.Label(self.frameRight, text="Sexo", font=("Times", 13), bg='#3a7ff6', bd=0, fg="#fff")
        self.labelSexo.place(x=230,y=100)

        self.labelUltPago = tk.Label(self.frameRight, text="Ultimo pago", font=("Times", 13), bg='#3a7ff6', bd=0, fg="#fff")
        self.labelUltPago.place(x=300,y=100)

        self.labelEdicion = tk.Label(self.frameRight, text="Edicion", font=("Times", 13), bg='#3a7ff6', bd=0, fg="#fff")
        self.labelEdicion.place(x=400, y=100)

















        #logo
        self.logo = utl.readImage("./images/mancuerna20.png", (400,400))
        
        self.frameLogo = tk.Frame(self.frameLeft, bd=0, width=300,relief=tk.SOLID, padx=10, pady=10, bg="#fcfcfc")
        self.frameLogo.pack(side="left", expand=tk.YES, fill=tk.BOTH) 

        #se ubique del lado izq, que no expanda y haga un fill(se llene para ambos lados, X e Y)
        self.labelFrame = tk.Label(self.frameLogo, image=self.logo, bg="#fcfcfc")
        self.labelFrame.place(x=0, y=0, relwidth=1, relheight=1)

        self.window.mainloop()

