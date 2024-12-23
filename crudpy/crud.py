import tkinter as tk

#importar modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from pixecodedb import *

from conexion import *

class formularioclientes:
 global base
 base =None  
   
 global Textboxid
 Textboxid =None
 
 global Textboxnom
 Textboxnom =None
 
 global Textboxape
 Textboxape =None
 
 global combo
 combo =None
 
 global groupBox
 groupBox =None
 
 global tree
 tree =None
 
    
 def formulario():#funcion
   global Textboxid
   global Textboxid
   global Textboxape
   global base
   global combo
   global base
   global groupBox
   global tree

    
    
    
 try:
     base = Tk()
     base.geometry("1200x300")
     base.title("formulario Python Rodrigo")
     
     groupBox = LabelFrame(base,text="Datos del personal",padx=5,pady=5)
     groupBox.grid(row=0,column=0,padx=10,pady=10)
     
     LabelId=Label(groupBox,text="ID",width=13,font=("arial",12)).grid(row=0,column=0)
     Textboxid = Entry(groupBox)
     Textboxid.grid(row=0,column=1)
     
     Labelnombre=Label(groupBox,text="Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
     Textboxnom = Entry(groupBox)
     Textboxnom.grid(row=1,column=1)
     
     Labelapellido=Label(groupBox,text="Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
     Textboxape = Entry(groupBox)
     Textboxape.grid(row=2,column=1)
     
     Labelsexo=Label(groupBox,text="Sexo:",width=13,font=("arial",12)).grid(row=3,column=0)
     seleccionsexo = tk.StringVar()
     combo= ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=seleccionsexo)
     combo.grid(row=3,column=1)
     seleccionsexo.set("Masculino")
     
     Button(groupBox,text="Guardar",width=10).grid(row=4,column=0)
     Button(groupBox,text="Modificar",width=10).grid(row=4,column=1)
     Button(groupBox,text="Eliminar",width=10).grid(row=4,column=2)      
     
     groupBox  = LabelFrame(base,text="Lista del personal",padx=5,pady=5,)
     groupBox.grid(row=0,column=1,padx=5,pady=5)
     #crear un treeview
     
     #configurar las columnas
     
     tree = ttk.Treeview(groupBox,columns=("ID","Nombres","Apellidos","Sexo"),show='headings',height=5,)
     tree.column("# 1",anchor=CENTER)
     tree.heading("# 1",text="ID")
     tree.column("# 2",anchor=CENTER)
     tree.heading("# 2",text="Nombres")
     tree.column("# 3",anchor=CENTER)
     tree.heading("# 3",text="Apellidos")
     tree.column("# 4",anchor=CENTER)
     tree.heading("# 4",text="Sexo")
     
     tree.pack()#funcione correta mente y muestre
     
     
     
     
     base.mainloop()
 except ValueError as error:
            print("error al mostrar la interfaz,error: {}".format(error))
            
 formulario()