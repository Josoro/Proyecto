#importar tkinter para hacer interfaz grafica en python
import tkinter as tk
#importar controlador
from Controlador import *

class Ventana():
    def __init__(self):
        #inicializacion de la ventana
        self.root = tk.Tk()

        #inicializacion de entradas
        self.entradaNumero = tk.Entry(self.root)
        self.entradaResultado = tk.Entry(self.root)

        #inicializacion de radiobuttons a nivel datos
        self.radio = tk.IntVar()
        self.radio.set(0)
        self.tipos = [("Decimal"),("Binario"),("Octal"),("Hexadecimal")]

        #cantidad numeros en operacion
        self.totalNumeros = []

        #tipo de operacion a realizar
        self.operacion = ""

        #error de entrada para numero
        self.error = False

    #accion para cambiar bases
    def cambioBase(self, decimal, base):
        conversion = ""
        while decimal // base != 0:
            print(str(decimal % base))
            if base == 16:
                if decimal % base == 10:
                    conversion = "a" + conversion
                elif decimal % base == 11:
                    conversion = "b" + conversion
                elif decimal % base == 12:
                    conversion = "c" + conversion
                elif decimal % base == 13:
                    conversion = "d" + conversion
                elif decimal % base == 14:
                    conversion = "e" + conversion
                elif decimal % base == 15:
                    conversion = "f" + conversion
            else:
                conversion = str(decimal % base) + conversion
            decimal = decimal // base
        return str(decimal) + conversion

    #obtener el tipo de numero que se va a ingresar
    def obtenerTipoSeleccionado(self):
        print(self.radio.get())
        if self.radio.get() == 0:
            return "decimal"
        elif self.radio.get() == 1:
            return "binario"
        elif self.radio.get() == 2:
            return "octal"
        else:
            return "hexadecimal"

    def verificarDecimal(self):
        try:
            int(self.entradaNumero.get())
            return True
        except:
            return False

    def verificarBinario(self):
        listaCaracteres = ["2","3","4","5","6","7","8","9"]
        contador = 0
        while contador < len(listaCaracteres):
            if self.entradaNumero.get().find(listaCaracteres[contador]) != -1:
                return False
            contador += 1
        return True

    def verificarOctal(self):
        listaCaracteres = ["8","9"]
        contador = 0
        while contador < len(listaCaracteres):
            if self.entradaNumero.get().find(listaCaracteres[contador]) != -1:
                return False
            contador += 1
        return True

    def verificarHexadecimal(self):
        listaCaracteres = ["g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",":",",",";","-","_","{","}","[","]","+","*","|","°","!","#","$","%","&","/","(",")","?","¡","¿","<",">"]
        contador = 0
        while contador < len(listaCaracteres):
            if self.entradaNumero.get().find(listaCaracteres[contador]) != -1:
                return False
            contador += 1
        return True

    def validacionesParaImprimir(self, operacion, cantidadPermitida):
        if operacion:
            if len(self.totalNumeros) < cantidadPermitida:
                self.totalNumeros.append(self.entradaNumero.get())
                self.error = False
            else:
                self.resultado("¡Maximo alcanzado!", False)
        else:
            self.resultado("¡Caracter inválido!", False)
            self.error = True

    def iniciarValidacionesGenerales(self, tipo, cantidadPermitida):
        if self.operacion != tipo and self.operacion != "":
            self.resultado("¡Operacion incorrecta!",False)
            return
        self.operacion = tipo
        self.resultado("",False)
        if self.obtenerTipoSeleccionado() == "decimal":
            self.validacionesParaImprimir(self.verificarDecimal(), cantidadPermitida)
        elif self.obtenerTipoSeleccionado() == "binario":
            self.validacionesParaImprimir(self.verificarBinario(), cantidadPermitida)
        elif self.obtenerTipoSeleccionado() == "octal":
            self.validacionesParaImprimir(self.verificarOctal(), cantidadPermitida)
        else:
            self.validacionesParaImprimir(self.verificarHexadecimal(), cantidadPermitida)

    #accion boton suma
    def suma(self):
        print("Suma")
        self.iniciarValidacionesGenerales("suma", 5)

    #accion boton resta
    def resta(self):
        print("Resta")
        self.iniciarValidacionesGenerales("resta", 2)

    #accion boton multiplicacion
    def multiplicacion(self):
        print("Multiplicacion")
        self.iniciarValidacionesGenerales("multiplicacion", 2)

    #accion boton division
    def division(self):
        print("Division")
        self.iniciarValidacionesGenerales("division", 2)

    def procesamientoConversiones(self, tipo, base, radioDecimal):
        if self.obtenerTipoSeleccionado() == tipo:
            self.iniciarValidacionesGenerales(tipo, 1)
            if self.error == False:
                self.resultado(self.entradaNumero.get(), False)
                self.limpiarMemoria()
        else:
            self.iniciarValidacionesGenerales(tipo, 1)
            if self.error == False:
                controlador = Controlador(self.totalNumeros)
                resultado = controlador.conversiones(self.obtenerTipoSeleccionado(), base, radioDecimal)
                self.resultado(resultado, False)
                self.limpiarMemoria()

    #accion boton decimal
    def decimal(self):
        print("Decimal")
        self.procesamientoConversiones("decimal", 10, False)

    #accion boton binario
    def binario(self):
        print("Binario")
        self.procesamientoConversiones("binario", 2, True)

    #accion boton octal
    def octal(self):
        print("Octal")
        self.procesamientoConversiones("octal", 8, False)

    #accion boton hexadecimal
    def hexadecimal(self):
        print("Hexadecimal")
        self.procesamientoConversiones("hexadecimal", 16, False)

    # accion boton igual (resultado)
    def final(self):
        self.resultado("",True)

    def limpiarMemoria(self):
        self.totalNumeros = []
        self.operacion = ""

    #accion para ir imprimiendo en seccion resultado
    def resultado(self,resultado, final):
        print("Resultado---")
        print(resultado)
        self.entradaResultado.delete('0', 'end')
        if final:
            "aqui voy al controlador"
            controlador = Controlador(self.totalNumeros)
            resultado = controlador.operaciones(self.operacion, self.obtenerTipoSeleccionado())
            self.limpiarMemoria()
        self.entradaResultado.insert(0, resultado)

    #seccion de radiobuttons en la ventana
    def seccionBotonesRadio(self):
        tk.Label(self.root, text="""Escoja el tipo:""").pack()
        for val, language in enumerate(self.tipos):
            tk.Radiobutton(self.root, text=language, padx = 20, variable=self.radio, value=val).pack(anchor=tk.W)

    #seccion de ingreso de numeros en la ventana
    def seccionIngresoNumero(self):
        tk.Label(self.root, text="Ingrese número:").pack()
        self.entradaNumero.pack()

    #seccion de botones para operaciones matematicas en la ventana
    def seccionBotones(self):
        tk.Button(self.root, text='+', command=self.suma).pack()
        tk.Button(self.root, text='-', command=self.resta).pack()
        tk.Button(self.root, text='*', command=self.multiplicacion).pack()
        tk.Button(self.root, text='/', command=self.division).pack()
        tk.Button(self.root, text='Decimal', command=self.decimal).pack()
        tk.Button(self.root, text='Binario', command=self.binario).pack()
        tk.Button(self.root, text='Octal', command=self.octal).pack()
        tk.Button(self.root, text='Hexadecimal', command=self.hexadecimal).pack()
        tk.Button(self.root, text='=', command=self.final).pack()

    #seccion para mostrar el resultado de la operacion final
    def seccionResultado(self):
        tk.Label(self.root, text="Resultado final:").pack()
        self.entradaResultado.pack()

    #inicio del programa
    def iniciarPrograma(self):
        self.seccionBotonesRadio()
        self.seccionIngresoNumero()
        self.seccionBotones()
        self.seccionResultado()
        self.root.mainloop()

iniciar = Ventana()
iniciar.iniciarPrograma()