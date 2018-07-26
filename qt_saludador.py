
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.setGeometry(100,100,200,100)

def btnSaludarCallBack():
    s = "Hola " + txtNombre.text()
    if chkSonrisa.isChecked():
        s = s + " :) "
    
    s = s + "!!!"
    
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText(s)
    msg.setWindowTitle("Saludo")
    msg.setStandardButtons(QtGui.QMessageBox.Ok)
    msg.exec_()

btnSaludar = QtGui.QPushButton(w)
btnSaludar.setText("&Saludar")
btnSaludar.clicked.connect(btnSaludarCallBack)

lblAQuien = QtGui.QLabel(w)
lblAQuien.setText(u"¿A quién saludamos?")

txtNombre = QtGui.QLineEdit(w)
chkSonrisa = QtGui.QCheckBox(w)
chkSonrisa.setText("Agregar :)")
grid = QtGui.QGridLayout()
grid.addWidget(lblAQuien, 0, 0)
grid.addWidget(txtNombre, 1, 0)
grid.addWidget(chkSonrisa, 2, 0)
grid.addWidget(btnSaludar, 1, 1)

w.setWindowTitle("Saludador")
w.setLayout(grid)
w.show()
sys.exit(app.exec_())
	
