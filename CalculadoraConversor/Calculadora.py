
class Calculadora():
    def __init__(self):
        self.resultado = 0

    def obtenerResultado(self):
        return self.resultado

    def sumar(self, numero):
        if self.resultado == 0:
            self.resultado = numero
        else:
            self.resultado += numero

    def restar(self, numero):
        if self.resultado == 0:
            self.resultado = numero
        else:
            self.resultado -= numero

    def multiplicar(self, numero):
        if self.resultado == 0:
            self.resultado = numero
        else:
            self.resultado *= numero

    def dividir(self, numero):
        if self.resultado == 0:
            self.resultado = numero
        else:
            self.resultado /= numero

    def decimal(self, numero, base):
        return int(numero, base)

    def binarioOctalHexadecimal(self, decimal, base):
        conversion = ""
        while decimal / base != 0:
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
            else:
                conversion = str(decimal % base) + conversion
            decimal = decimal // base
        self.resultado = str(decimal) + conversion


