#-*- coding:utf-8 -*-

#Calculadora de progresiones aritmeticas

def reason():
    d = 0
    end = float(raw_input('Ingrese el último término: '))
    first = float(raw_input('Ingrese el primer término: '))
    c = float(raw_input('Ingrese la cantidad de elementos dados: '))

    d = (end - first) / (c - 1)

    return d


def formula_foreground(d):
    first = 0
    reason_ = d
    end = float(raw_input('Ingrese el último término: '))
    c = float(raw_input('Ingrese la cantidad de elementos dados: '))

    first = float(end - (c - 1)* reason_)
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
            r = float(raw_input('Ingrese la razon/diferencia: '))
            first_term = formula_foreground(r)
            print('El primer elemento de la progresion es: {}'.format(first_term))

        elif dife == 'n':
            reason_first = reason()
            print('La razon es: {}'.format(reason_first))
            print('')
            first_term = formula_foreground(reason_first)
            print('El primer elemento de la progresion es: {}'.format(first_term))



        elif dife == 'v':
            print('En proceso')
           



def last_term():
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
           print(error)


if __name__ == '__main__':
    print('    === CALCULADORA DE PROGRESIÓN ARITMÉTICA ===')
    error = 'Ingrese una de las letras entre los corchetes'
    run()
