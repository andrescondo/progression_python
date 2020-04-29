#-*- coding:utf-8 -*-

# Muchas palabras no llevan tilde por que se esta desarrolando en windows en consola
# Y para usuarios que la ejecuten en consola puedan ver las palabras bien

def reason():
    print('-- C A L C U L A R - L A - D I F E R E N C I A --')
    d = 0
    end = float(raw_input('Ingrese el ultimo termino: '))
    first = float(raw_input('Ingrese el primer termino: '))
    c = float(raw_input('Ingrese la cantidad de elementos dados: '))

    d = (end - first) / (c - 1)
    reason_d = d

    print('La razon/diferencia es : {}'.format(reason_d))
    print('''

        ''')
    return d
    


def formula_foreground(d):
    first = 0
    reason_f = d
    end = float(raw_input('Ingrese el último término: '))
    c = float(raw_input('Ingrese la cantidad de elementos dados: '))
    first = float(end - (c - 1)* reason_f)
    return first


def foreground():
    print('-- C A L C U L A R - E L - P R I M E R - T E R M I N O --')

    while True:
        dife = str(raw_input('''
            ¿Te dieron las razon/diferencia para el ejercicio?: 
            [y]es
            [n]o
            [v]olver

            '''))

        if dife == 'y':
            d = float(raw_input('Ingrese la razon/diferencia: '))
            first_term = formula_foreground(d)
            print('')
            print('El primer elemento de la progresion es: {}'.format(first_term))

        elif dife == 'n':
            print('')
            print(no_difference)
        elif dife == 'v':
            run()
        else:
            print(error)

    return result

def formula_last_term(d):
    end = 0
    reason_e = d
    first = float(raw_input('Ingrese el primer termino: '))
    c = float(raw_input('Ingrese la cantidad de elementos: '))
    end = first + (c - 1) * reason_e

    return end


def last_term():
    print('-- C A L C U L A R - E L - U L T I M O - T E R M I N O --')
    while True:
        dife = str(raw_input('''
            ¿Te dieron las razon/diferencia para el ejercicio?: 
            [y]es
            [n]o
            [v]olver
            '''))

        if dife == 'y':
            d = float(raw_input('Ingrese la razon/diferencia: '))
            term_last =  formula_last_term(d)
            print('El ultimo termino es: {}'.format(term_last))

        elif dife == 'n':
            print('')
            print(no_difference)

        elif dife == 'v':
            run()
        else:
            print(error)


def sum_term():  
    su = 0
    first = float(raw_input('Ingrese el primer termino: '))
    end = float(raw_input('Ingrese el ultimo termino: '))
    c = float(raw_input('Ingrese la cantidad de elementos: '))

    su = ((end + first) * c ) / 2
    return su


def sum():
    print('-- C A L C U L A R - L A - S U M A - D E - T O D O S - L O S - T E R M I N O S --')
    
    while True:
        suma = str(raw_input('''
            Hacer las operacion:
            [s]i
            [v]olver
            '''))
        if suma == 's':
            sum_s =  sum_term()
            print('La suma de los terminos es: {}'.format(sum_s))

        elif suma == 'v':
            run()
        else:
            print(error)



def run():
    print('    === CALCULADORA DE PROGRESION ARITMETICA ===')
    while True:
        excercise = str(raw_input('''
            ¿Que se les pidio encontrar?

            [p]rimer termino
            [u]ltimo termino
            [r]azon / diferencia
            [s]uma de valores
            '''))

        if excercise == 'p':
            foreground()
            
        elif excercise == 'u':
            last_term()

        elif excercise == 'r':
            reason()

        elif excercise == 's':
            sum()

        else:
           print(error)


if __name__ == '__main__':
    no_difference = 'Para sacar la razon/diferencia se debe restar dos terminos, si estos son seguidos\nUn termino menos el anterior (a2 - a1 = d) y vuelve a intentar la formula' 
    error = 'Ingrese una de las letras entre los corchetes'
    run()
