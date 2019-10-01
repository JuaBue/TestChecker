# coding: utf-8
from Tkinter import *
import tkMessageBox
from Parser import *
from Tkconstants import *
import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import os.path
from tkFileDialog import *


class Menu(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.folder_path = "C:\Users\juan.bueno\Desktop\INGENICO"
        parent.geometry("524x200")
        parent.resizable(width=False, height=False)
        parent.iconbitmap('logos\crocodile.ico')
        self.parent.title("TestChecker")
        Menu.configura(self, parent)

    def configura(self, parent):
        self.Labelframe1 = LabelFrame(parent)
        self.Labelframe1.place(x=9, y=10.5, relheight=0.31, relwidth=0.96)
        self.Labelframe1.configure(text="Ubicación Fichero Trazas", borderwidth="2", relief=GROOVE, width=435)

        self.Label1 = Label(parent)
        self.Label1.place(x=9, y=118.5, height=19, width=201)
        self.Label1.configure(text="¿Quieres Procesar este fichero de trazas?", width=201)

        self.Button1 = Button(parent)
        self.Button1.place(x=9, y=145.25, height=41, width=101)
        self.Button1.configure(pady="0", text="Procesar...", font='Helvetica 9 bold', command=lambda: self.checkparse())

        self.Button2 = Button(parent)
        self.Button2.place(x=141.5, y=145.25, height=41, width=101)
        self.Button2.configure(pady="0", text="Salir", command=lambda: self.cerrarapp())

        image = PhotoImage(file="logos\\folder.gif")
        self.Button3 = Button(self.Labelframe1)
        self.Button3.place(x=462.25, rely=0.2, height=20, width=20)
        self.Button3.configure(image=image, width="20", height="20", relief=GROOVE, bd=0, command=lambda: self.selectpath())

        self.Entry4 = Entry(self.Labelframe1)
        self.Entry4.place(relx=0.03, rely=0.20, height=19, width=420)
        self.Entry4.insert(INSERT, self.folder_path)

        self.Label2 = Label(parent)
        self.Label2.place(x=9, y=85, height=25, width=70)
        self.Label2.configure(text="Fichero CSS:", width=201)

        SelectCSS = StringVar()
        SelectCSS.set("TestReport.css")
        self.OptionMenu1 = OptionMenu(parent, SelectCSS, "TestReport.css", "...")
        self.OptionMenu1.place(x=90, y=85, height=25, width=155)

        self.Frame2 = LabelFrame(parent)
        self.Frame2.place(relx=0.57, rely=0.46, relheight=0.49, relwidth=0.41)
        self.Frame2.configure(text="Generación Reportes", relief=GROOVE, borderwidth="2",width=185)

        CheckVar1 = IntVar()
        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.Checkbutton1.place(x=4, y=5, relheight=0.26, relwidth=0.31)
        self.Checkbutton1.configure(highlightcolor="black", justify=LEFT, text=".pdf ", variable=CheckVar1)

        CheckVar2 = IntVar()
        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.Checkbutton2.place(x=4, y=25, relheight=0.26, relwidth=0.31)
        self.Checkbutton2.configure(highlightcolor="black", justify=LEFT, text=".html", variable=CheckVar2)

        CheckVar3 = IntVar()
        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.Checkbutton3.place(x=1, y=45, relheight=0.26, relwidth=0.31)
        self.Checkbutton3.configure(highlightcolor="black", justify=LEFT, text=".txt", variable=CheckVar3)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.49, rely=0.22, height=41, width=81)
        self.Button4.configure(highlightcolor="black", text="Report", pady="0", width=81, command=lambda: self.genereport(CheckVar1.get(), CheckVar2.get(), CheckVar3.get()))
        self.Button4.configure(state=DISABLED)

        parent.mainloop()

    def selectpath(self):
        filename = askopenfilename()
        if os.path.isfile(filename):
            self.folder_path = filename
            self.Entry4.delete(0, "end")
            self.Entry4.insert(END, self.folder_path)
        else:
            result = tkMessageBox.showerror("TestChecker", "El fichero seleccionado no es valido", icon='error')
            if result == 'yes':
                tk.destroy()
            else:
                pass

    def cerrarapp(self):
        result = tkMessageBox.askquestion("TestChecker", "¿Desea salir de la aplicación?", icon='warning')
        if result == 'yes':
            tk.destroy()
        else:
            pass

    def genereport(self, CheckVar1, CheckVar2, CheckVar3):
        if not (CheckVar1 or CheckVar2 or CheckVar3):
            result = tkMessageBox.showerror("TestChecker", "No ha seleccionado el tipo de reporte", icon='error')
            if result == 'yes':
                tk.destroy()
            else:
                pass
        else:
            objetoparser = ParserTest()
            objetoparser.openreport()

    def noselectapp(self):
        result = tkMessageBox.showerror("TestChecker", "No ha seleccionado el tipo de reporte", icon='error')
        if result == 'yes':
            tk.destroy()
        else:
            pass

    def checkparse(self):
        if os.path.isfile(self.folder_path):
            objetoparser = ParserTest()
            objetoparser.parsetrace(self.folder_path)
            self.Button4.configure(state=ACTIVE)
        else:
            result = tkMessageBox.showerror("TestChecker", "No ha seleccionado un tipo de fichero valido", icon='error')
            if result == 'yes':
                tk.destroy()
            else:
                pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        tk = Tk()
        Menu(parent=tk)
    else:
        filepath = sys.argv[1]
        objetoparser = ParserTest()
        objetoparser.parsetrace(filepath)
        objetoparser.openreport()



