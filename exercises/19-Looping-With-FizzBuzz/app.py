def fizz_buzz():
    # your code here
    resultado = ""
    for x in range(1, 101):
        if calcularSiMultiplo(x, 3) == True:
            resultado = "Fizz"
        if calcularSiMultiplo(x, 5) == True:
            resultado = resultado + "Buzz"
        if(resultado == ""):
            resultado = x
        print(resultado)
        resultado = ""

def calcularSiMultiplo(numero, multiploDe):
    resto = numero % multiploDe
    if resto == 0 :
        return True
    else: 
        return False
    
fizz_buzz()