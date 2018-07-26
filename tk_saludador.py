#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter import messagebox

top = tkinter.Tk()      # ventana principal
top.title("Saludador")  # título de ventana principal
top.geometry("%dx%d%+d%+d" % (300, 150, 100, 200))

def btnSaludarCallBack():
    s = "Hola " + txtNombre.get()
    if flgSonrisa.get() == 1:
        s = s + " :) "
        
    s = s + "!!!"
    messagebox.showinfo("Saludo", s)
    
btnSaludar = tkinter.Button(top, text="Saludar", underline=0, command=btnSaludarCallBack)
top.bind('<Alt_L><s>', lambda e:btnSaludarCallBack())

lblAQuien = tkinter.Label(top, text = "¿A quién saludamos?")
txtNombre = tkinter.Entry(top)

flgSonrisa = tkinter.IntVar()

chkSonrisa = tkinter.Checkbutton(top, text = "Agregar :)", variable = flgSonrisa, \
#                 onvalue = 1, offvalue = 0, 
        height = 3)

lblAQuien.grid(row=0, column=0, sticky=tkinter.W, columnspan=2, padx=5, pady=20)
txtNombre.grid(row=1, column=0, sticky=tkinter.W, padx=5)
btnSaludar.grid(row=1, column=1)
chkSonrisa.grid(row=2, column=0, sticky=tkinter.W, columnspan=2)

top.mainloop()
