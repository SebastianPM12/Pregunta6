import sys
from turtle import st #Este import sys es un modulo
import ModuloTransporte as mt
"""
Se importa la primera la clase Qmain window, es para el manejo de la ventana o el formulario en si
Se importa otra segunda clase es el QApplication es para el manejo de las aplicaciones, para que funcione
todo el entorno grafico del vs code 
"""
from PyQt6.QtWidgets import QMainWindow, QApplication #Importamos dos clases qtwidgets es para el formulario y el QmAINwINDOS PARA LA APLICACION 
from PyQt6 import uic #Imporamos el modulo uic para llamar al formulario
import Modulo01 as operation01 #alias para el modulo 01 para poder utilizar todas sus funciones
class transporte(QMainWindow):   #ejemplo 01 es la clase     #cADA CLASE como en java tiene un constructor
    def __init__(self):  #init es el consturctor de la clase Ejemplo01, el self hace referencia a la clase y como se llama la calse Ejemplo01
        QMainWindow.__init__(self)
        uic.loadUi("TransporteOrigen.ui",self) #aca significa 
        #Inicializar los objetos que hemos hecho en el qt designer
        self.initUI()

    def initUI(self):
        self.bListo.clicked.connect(self.calcular)
        self.bSalir.clicked.connect(self.salir)
        self.bNuevo.clicked.connect(self.nuevo)
    
    def nuevo(self):
        self.pagoKid.setText("")#limpias el tMonto
        self.pagoAdulto.setText("")#Limpast el lblDescuento
        self.pagoUni.setText("")
        self.montoCombustible.setText("")
        self.totalCobrado.setText("")
        self.ganancia.setText("")

    def salir(self):
        self.close()
   
    def calcular(self):
        kid=int(self.pagoKid.text())
        adulto=int(self.pagoAdulto.text())
        uni=int(self.pagoUni.text())
        mcb=float(self.montoCombustible.text())
        totalCobrado=mt.totalCobrado(kid,adulto,uni)
        self.totalCobrado.setText(str(totalCobrado))
        self.ganancia.setText(str(mt.ganancia(mcb,totalCobrado)))





if __name__=='__main__':
    #Se crea una instancia para iniciar la aplicacion
    app=QApplication(sys.argv)
    #Vamos a crear un objeto del tipo ejemplo 01  
    vetana01=transporte()
    #Mostrar la ventana o el objeto o el formulario 
    vetana01.show()
    #Cerar la aplicacion
    sys.exit(app.exec())
