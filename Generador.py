from tkinter import *



ventana=Tk()
ventana.title("Datos personales")
ventana.resizable(0,0)
frame=Frame(ventana)
frame.grid(row=0, column=0)
lblTitulo=LabelFrame(frame, text="Ingrese sus datos básicos")
lblTitulo.grid(row=0, column=0)
lblNombre=Label(frame, text="Nombre*:")
lblNombre.grid(row=1, column=0)
txtNombre=Entry(frame, width= 25)
txtNombre.grid(row=1, column=1, padx= 10, pady=10)
lblApellido=Label(frame, text="Apellido*:")
lblApellido.grid(row=2, column=0)
txtApellido=Entry(frame, width= 25)
txtApellido.grid(row=2, column=1, padx= 10, pady=10)
lblCedula=Label(frame, text="Cédula*:")
lblCedula.grid(row=3, column=0)
txtCedula=Entry(frame, width= 25)
txtCedula.grid(row=3, column=1, padx= 10, pady=10)
lblEmail=Label(frame, text="E-mail*:")
lblEmail.grid(row=4,column=0)
txtEmail=Entry(frame, width=25)
txtEmail.grid(row=4,column=1, padx= 10, pady=10)


ventana.mainloop()