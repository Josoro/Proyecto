
from Calculadora import *

class Controlador():
    def __init__(self, listaNumeros):
        self.listaNumeros = listaNumeros

    def operacionesModelo(self, numero, operacion, calculadora):
        if operacion == "suma":
            calculadora.sumar(numero)
        elif operacion == "resta":
            calculadora.restar(numero)
        elif operacion == "multiplicacion":
            calculadora.multiplicar(numero)
        else:
            calculadora.dividir(numero)

    def operaciones(self, operacion, tipo):
        contador = 0
        calculadora = Calculadora()
        base = 0
        while contador < len(self.listaNumeros):
            if tipo == "decimal":
                self.operacionesModelo(int(self.listaNumeros[contador]), operacion, calculadora)
            elif tipo == "binario":
                numero = calculadora.decimal(self.listaNumeros[contador],2)
                self.operacionesModelo(numero, operacion, calculadora)
                base = 2
            elif tipo == "octal":
                numero = calculadora.decimal(self.listaNumeros[contador], 8)
                self.operacionesModelo(numero, operacion, calculadora)
                base = 8
            else:
                numero = calculadora.decimal(self.listaNumeros[contador], 16)
                self.operacionesModelo(numero, operacion, calculadora)
                base = 16
            contador += 1
        if tipo != "decimal":
            calculadora.binarioOctalHexadecimal(calculadora.obtenerResultado(), base)
        return calculadora.obtenerResultado()

    def convertirEnDecimal(self, tipo):
        if tipo == "binario":
            calculadora = Calculadora()
            return calculadora.decimal(self.listaNumeros[0], 2)
        elif tipo == "octal":
            calculadora = Calculadora()
            return calculadora.decimal(self.listaNumeros[0], 8)
        elif tipo == "decimal":
            return self.listaNumeros[0]
        else:
            calculadora = Calculadora()
            return calculadora.decimal(self.listaNumeros[0], 16)

    def procesoConversiones(self, tipo, base):
        numero = self.convertirEnDecimal(tipo)
        calculadora = Calculadora()
        calculadora.binarioOctalHexadecimal(int(numero), base)
        return calculadora.obtenerResultado()

    def conversiones(self, tipo, base, radioDecimal):
        print("en conversiones")
        if base == 10 and radioDecimal == False:
            return self.convertirEnDecimal(tipo)
        else:
            return self.procesoConversiones(tipo, base)