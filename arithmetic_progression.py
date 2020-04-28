#-*- coding:utf-8 -*-

#Calculadora de progresiones aritmeticas

def with_difference(primer, segundo, d):
    result = 0

    result = float((primer + segundo) / d)

    return result


def run():
    primer = int(raw_input('Ingrese el primer término: '))
    segundo = int(raw_input('Ingrese el segundo término: '))
    
    while True:
        dife = str(raw_input('''
            Se le dío el valor de la diferencia?
            [s]i
            [n]o
            '''))
        if dife =='s':
            d = int(raw_input('Ingrese la diferencia: '))
            cal_with_diference = with_difference(primer, segundo, d)
            print('El resultado es: {}'.format(cal_with_diference))

        if dife == 'n':
            no_difference(a1, a2)

        else:
            print('Ingrese la letra entre los corchetes')





if __name__ == '__main__':
    print('INGRESE LOS DATOS DE LA PROGRESIÓN ARITMÉTICA')
    run()
