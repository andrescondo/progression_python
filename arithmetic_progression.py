#-*- coding:utf-8 -*-

#Calculadora de progresiones aritmeticas
def formula_foreground():
    first = 0
    end = float(raw_input('Ingrese el último término: '))
    c = float(raw_input('Ingrese la cantidad de elementos dados: '))
    d = float(raw_input('Ingrese la razón/diferencia: '))

    first = float(end - (c - 1)* d)
    return first


def foreground():
    while True:
        dife = str(raw_input('''
            ¿Te dieron las razon/diferencia para el ejercicio?: 
            [y]es
            [n]o
            [v]olver

            '''))
        if dife == 'y':
            first_term = formula_foreground()
            print('El primer elemento de la progresion es: {}'.format(first_term))
        elif dife == 'n':
            print('En proceso')

        elif dife == 'v':
            run()



def last_term():
    pass

def reason():
    pass

def sum():
    pass


def run():
    while True:
        excercise = str(raw_input('''
            ¿Qué se les pidio encontrar?

            [p]rimer término
            [u]ltimo término
            [r]azón / diferencia
            [s]uma de valores
            [c]errar
            '''))

        if excercise == 'p':
            foreground()
        elif excercise == 'u':
            last_term()
        elif excercise == 'r':
            reason()
        elif excercise == 's':
            sum()
        elif excercise == 'c':
            break
        else:
           error


if __name__ == '__main__':
    print('=== CALCULADORA DE PROGRESIÓN ARITMÉTICA ===')
    error = str('Ingrese la letra entre los corchetes')
    run()
