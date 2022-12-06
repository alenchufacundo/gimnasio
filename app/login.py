import tkinter as tk
import pymysql
from tkinter import messagebox, ttk
from tkinter.font import BOLD
import utilities.functions as utl
from app.mainPanel import MasterPanel
from db.db_connection import Database

class Application:
    
    #function para verificar si el usuario se encuntra en la bbdd
    def verificationLogin(self):

        #conexion a base de datos
        # db = Database ()

        username = self.user.get()
        pw = self.password.get()
        if username == "root" and pw == "1234":
            self.window.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña o el usuario son incorrectas o no se encuetran registrados")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Aesthethic')
        self.window.geometry('800x500')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(width=0, height=0)
        utl.centerWindow(self.window, 800, 500)


        logo = utl.readImage("./images/mancuerna20.png", (200,200))

        #añade un frame a la ventana principal, los frame son como div/contenedores.

        #PANEL DEL LADO IZQUIERDA (LOGO)
        frameLogo = tk.Frame(self.window, bd=0, width=300,relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frameLogo.pack(side="left", expand=tk.NO, fill=tk.BOTH) 
        #se ubique del lado izq, que no expanda y haga un fill(se llene para ambos lados, X e Y)
        labelFrame = tk.Label(frameLogo, image=logo, bg='#3a7ff6')
        labelFrame.place(x=0, y=0, relwidth=1, relheight=1)

        #PANEL DEL LADO DERECHO(TITULO, USER & PW)

        #creacion del frame ppal
        frameInfo = tk.Frame(self.window, bd=0,
                        relief=tk.SOLID, bg='#fcfcfc')
        frameInfo.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #PANEL LADO DERECHO PARTE TITULO

        #creacion del frame primario
        frame_info_top = tk.Frame(frameInfo, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_info_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_info_top, text="Bievenid@s a AESTHETIC", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #PANEL DEL USUARIO Y PW
        
        #creacion del frame secundario
        frame_info_fill = tk.Frame(frameInfo, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_info_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #creacion de etiquetas
        #usuario
        userLabel = tk.Label(frame_info_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        userLabel.pack(fill=tk.X, padx=20, pady=5)

        self.user = ttk.Entry(frame_info_fill, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)

        #password
        passwordLabel = tk.Label(frame_info_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        passwordLabel.pack(fill=tk.X, padx=20, pady=5)

        self.password = ttk.Entry(frame_info_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        #boton de login
        loginButton = tk.Button(frame_info_fill, text="Iniciar sesion", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificationLogin)
        loginButton.pack(fill=tk.X, padx=20, pady=20)
        #evento bind, para que aprete enter y funcione el verificationLogin()
        loginButton.bind("<Button-2>", lambda event:self.verificationLogin())
        
        self.window.mainloop()