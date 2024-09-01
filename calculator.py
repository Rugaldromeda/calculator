import os

def clear():
    reset = int(input("Deseja fazer outra operação? 1 - SIM, 2 - Não : "))

    if(reset == 1):
        os.system('cls') or None
        init()
    elif(reset == 2):
        os.system('cls') or None
        exit()

def soma(num1,num2):

    somando = num1+num2
    print("{} + {} = {}".format(num1,num2, somando)) 
    clear()

def sub(num1,num2):

    subtraindo = num1-num2
    print("{} + {} = {}".format(num1,num2, subtraindo)) 
    clear()

def multi(num1,num2):

    multiplicando = num1*num2
    print("{} * {} = {}".format(num1,num2, multiplicando)) 
    clear()

def div(num1,num2):

    dividindo = num1/num2
    print("{} / {} = {}".format(num1,num2, dividindo)) 
    clear()

def exp(num1,num2):

    potencia = num1**num2
    print("{} elevado a {} = {}".format(num1,num2, potencia)) 
    clear()

def calc(op):
    num1 = int(input("Qual o primeiro valor?"))
    num2 = int(input("Qual o segundo valor?"))
    op(num1,num2)

def init():
    print("Bem vindo a calculadora python \n 0 : Soma \n"
 " 1 : Subtração \n 2 : Multiplicação \n 3 : Divisão \n 4 : exponenciação")

    operation = int(input("Escolha a operação que deseja realizar:"))

    if(operation == 0):
        print(" Soma escolhida")
        calc(soma)
    elif(operation == 1):
        print(" Subtração escolhida")
        calc(sub)
    elif(operation == 2):
        print(" Multiplicação - Escolhida")
        calc(multi)
    elif(operation == 3):
        print(" Divisão escolhida")
        calc(div)
    elif(operation == 4):
        print(" Exponenciação escolhida")
        calc(exp)

init()



