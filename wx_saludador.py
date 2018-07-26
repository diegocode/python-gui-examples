#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

app = wx.App() ##
frame = wx.Frame(None, title='Saludador')

def btnSaludarCallBack(e):
    s = "Hola " + txtNombre.GetValue()
    if chkSonrisa.GetValue() == 1:
        s = s + " :) "
        
    s = s + "!!!"
    wx.MessageBox(s, 'Saludo', wx.OK | wx.ICON_INFORMATION)

btnSaludar = wx.Button(frame, label='&Saludar')
btnSaludar.Bind(wx.EVT_BUTTON, btnSaludarCallBack)

lblAQuien = wx.StaticText(frame, label="¿A quién saludamos?")
txtNombre = wx.TextCtrl(frame)
chkSonrisa = wx.CheckBox(frame, label='Agregar :)')

gs = wx.GridBagSizer(5, 5)
gs.Add(lblAQuien, pos=(0, 0), flag= wx.EXPAND | wx.ALL, border=5)
gs.Add(txtNombre, pos=(1, 0), flag= wx.EXPAND | wx.ALL, border=5)
gs.Add(btnSaludar, pos=(1, 1), flag= wx.EXPAND | wx.ALL, border=5)
gs.Add(chkSonrisa, pos=(2, 0), flag= wx.EXPAND | wx.ALL, border=5)

frame.SetSizer(gs)

frame.Show()
frame.Centre()
app.MainLoop()
