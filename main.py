from tkinter import *
import string
import random

root = Tk()
root.config(bg = "Light Gray")
root.resizable(0, 0)
root.title("Generador de Contraseñas")
root.geometry("260x320")

#FRAME PREFERENCIAS
framePreferencias = Frame(root, borderwidth = 10)
framePreferencias.pack(padx = 20, pady = 20)

#Cantidad de caracteres
texto1 = Label(framePreferencias, text = "Nº de caracteres (max. 32):").grid(row = 0, column = 0, padx = 10)

nCaracteres = StringVar()
input1 = Entry(framePreferencias, width = 3, textvariable = nCaracteres).grid(row = 0, column = 1)

#Letras
def habilitarRadiobuttons():
    if radio1["state"] == NORMAL:
        radio1.configure(state = DISABLED)
        radio2.configure(state = DISABLED)
        radio3.configure(state = DISABLED)
    else:
        radio1.configure(state = NORMAL)
        radio2.configure(state = NORMAL)
        radio3.configure(state = NORMAL)

varCheck1 = IntVar()
check1 = Checkbutton(framePreferencias, text = "Incluir letras", variable = varCheck1, command = habilitarRadiobuttons).grid(row = 1, column = 0, sticky = W, columnspan = 2)

varRadioLetras = IntVar()
radio1 = Radiobutton(framePreferencias, text = "Solo mayúsculas", variable = varRadioLetras, value = 1, state = DISABLED)
radio2 = Radiobutton(framePreferencias, text = "Solo minúsculas", variable = varRadioLetras, value = 2, state = DISABLED)
radio3 = Radiobutton(framePreferencias, text = "Usar ambas", variable = varRadioLetras, value = 3, state = DISABLED)
varRadioLetras.set(3)
radio1.grid(row = 2, column = 0, sticky = W, columnspan = 2, padx = 10)
radio2.grid(row = 3, column = 0, sticky = W, columnspan = 2, padx = 10)
radio3.grid(row = 4, column = 0, sticky = W, columnspan = 2, padx = 10)

#Números
varCheck2 = IntVar()
check2 = Checkbutton(framePreferencias, text = "Incluir números", variable = varCheck2).grid(row = 5, column = 0, sticky = W, columnspan = 2)

#Especiales
varCheck3 = IntVar()
check3 = Checkbutton(framePreferencias, text = "Incluir caracteres especiales", variable = varCheck3).grid(row = 6, column = 0, sticky = W, columnspan = 2)

#FRAME OUTPUT
frameOutput = Frame(root)
frameOutput.pack(padx = 20)

#Salida/Display
output = StringVar()
entry1 = Entry(frameOutput, textvariable = output, width = 33)
entry1.grid(row = 0, column = 0, pady = 10, padx = 10)

#La magia
arrLetras = list(string.ascii_lowercase + string.ascii_uppercase)
arrNumeros = list("0123456789")
arrSimbolos = list(" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

def generarContraseña():
    if nCaracteres.get() == "" or int(nCaracteres.get()) < 1 or int(nCaracteres.get()) > 32 or (varCheck1.get() == 0 and varCheck2.get() == 0 and varCheck3.get() == 0):
        output.set("ERROR")
    else:
        arrConsiderados, resultado = [], ""
        if varCheck1.get():
            if varRadioLetras.get() == 1:
                arrConsiderados += arrLetras[26:]
            elif varRadioLetras.get() == 2:
                arrConsiderados += arrLetras[:26]
            else:
                arrConsiderados += arrLetras
        if varCheck2.get():
            arrConsiderados += arrNumeros
        if varCheck3.get():
            arrConsiderados += arrSimbolos
        for i in range(int(nCaracteres.get())):
            resultado += random.choice(arrConsiderados)
        output.set(resultado)

#Boton GENERAR
boton1 = Button(frameOutput, text = "GENERAR", command = generarContraseña)
boton1.grid(row = 1, column = 0, pady = 10, padx = 10)

root.mainloop()