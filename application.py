"""This program is made to calculate the factorial of a number"""
import os
import sys

print "Welcome to factorial"

def factorial(numero, nombre):
    """Factorial function"""
    if nombre > 0 and nombre <= 995:
        numero = factorial(numero, nombre-1)
        numero = numero*nombre
    else:
        numero = 1
    if nombre > 995:
        print "It is a very high number for factor attempts with a smaller number"
    return numero

def resultado():
    """Her number is entered to calculate the result of the factorial"""
    try:
        numero = int(raw_input("Enter a number from 1 to 995:\n"))
        calculo = factorial(1, numero)
        print "The factorial of %s is %s" % (numero, calculo)
        raw_input("Press enter")
        question()
        

    except ValueError:
        print "\nIt must be a numeric value try again:"
        resultado()


def question():
    """Make the question to see if he wants to re-enter data"""
    limpiar()
    val3 = raw_input("You want to calculate the factorial of a number: y/n\n")
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
