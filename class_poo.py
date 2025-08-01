
class Numero:
    def __init__(self, numero):
        self.numero = numero
        
    def evaluarNumero(self):
        if self.numero & 1:
            print("impar")
            if self.numero == 7:
                print("\n El número ingresado es un comodin")
        else:
            print("par")
            if self.numero == 10:
                print("\n El número ingresado es 10")
                
    def sumar(self,numeroasumar):
        return self.numero + numeroasumar
    
    
if __name__ == "__main__":
    
    numeroaevaluar = Numero(int(input("Ingrese un número: \n")))
    numeroaevaluar.evaluarNumero()
    sumarealizada = numeroaevaluar.sumar(2)
    print("\n La suma realizada es: ",sumarealizada)

                 
                    