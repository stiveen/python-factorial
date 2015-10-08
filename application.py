"""This program is made to calculate the factorial of a number"""
import os
import sys

print "Bienvenido a factorial"

def factorial(numero, nombre):
    """Factorial function"""
    if nombre > 0 and nombre <= 995:
        numero = factorial(numero, nombre-1)
        numero = numero*nombre
    else:
        numero = 1
    if nombre > 995:
        print "Es un numero muy alto para el factorial intenta con otro numero menor"
    return numero

def resultado():
    """Her number is entered to calculate the result of the factorial"""
    try:
        numero = int(raw_input("inserta un numero del 1 al 995:\n"))
        calculo = factorial(1, numero)
        print "El factorial de %s es %s" % (numero, calculo)
        question()
    except ValueError:
        print "\nTiene que ser un valor numerico vuelve a intentarlo:"
        resultado()


def question():
    """Make the question to see if he wants to re-enter data"""
    val3 = raw_input("desea calcular el factorial de un numero: y/n\n")
    val3 = val3.lower()
    if val3 == "y":
        resultado()
    elif val3 == "n":
        salir()
    else:
        print "Your character is not valid try again"
        limpiar()
        question()


def limpiar():
    "This function serves to clean in windows and ubuntu"
    os.system("cls")
    os.system("clear")

def salir():
    """It is a function to exit the program"""
    print "good bye"
    sys.exit()

resultado()
