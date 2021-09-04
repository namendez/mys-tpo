import argparse
from math import * #importo funciones (sqrt, sin, cos, etc)
import matplotlib.pyplot as plt


def euler(eq, t0, tf, x0, h):
    # en t0, la curva a aproximar vale x0
    
    # inicialmente t_tmp = t0. en cada iteración le voy sumando h hasta llegar a tf.
    # en el array x_euler guardo tuplas con (t_tmp, x(t_tmp))
    x_euler = [(t0, x0)]
    t = t0 # t arranca en t0
    i = 0

    # calculo todos los x0 entre t0 y tf, con incrementos h. los guardo como tuplas (t, x0) en el array x_euler
    while True:
        x0_tmp = x_euler[i][1] # obtengo el x0 para calcular x1 como x1 = x0 + h * (f(t, x))
        t += h
        i += 1

        # si t += h > t salgo del loop (termine de aproximar)
        if (t > tf):
            break

        x1 = x0_tmp + h * eval(eq) # evaluo la funcion en t, ej: t = 2, f(t) = t**2 = 4
        x_euler.append((t, x1))

    return x_euler

def main():
    parser = argparse.ArgumentParser(description="Calcula la aproximación de Euler dado una ED de primer orden.")
    parser.add_argument("-N", help="valor de N = cantidad de particiones", type=int)
    parser.add_argument("-H", help="valor de h = tamaño de la particion", type=float)
    parser.add_argument("-e", "--equation", help="ecuacion diferencial a aproximar")
    parser.add_argument("-x0", help="condicion inicial de la ED para t0", type=float)
    parser.add_argument("-t0", help="instante inicial de la ED para el intervalo a aproximar", type=float)
    parser.add_argument("-tf", help="instante final de la ED para el intervarlo a aproximar", type=float)
    args = parser.parse_args()
    N_value = args.N
    h_value = args.H
    x0 = args.x0
    t0 = args.t0
    tf = args.tf
    eq = args.equation

    if not N_value and not h_value:
        print('Debe ingresar -H o -N')
        return

    if N_value and h_value:
        print('Solo debe ingresar -H o -N, no ambos a la vez')
        return

    if x0 is None or t0 is None or tf is None:
        print('Los valores de x0, t0 y tf son obligatorios.')
        return

    #si se ingresó el valor de N, lo convierto al valor de h
    if not h_value:
        h_value = (tf-t0) / N_value

    try:
        # Aproximo por el metodo de Euler
        x_euler = euler(eq, t0, tf, x0, h_value)

        # Paso el array de tuplas (x, y) a arrays [x], [y] para graficarlo
        x_val = [x[0] for x in x_euler]
        y_val = [x[1] for x in x_euler]

        plt.title('Aproximacion por metodo de Euler a la ED f(x,t) = {0}'.format(eq))
        plt.xlabel('t')
        plt.ylabel('x')
        plt.plot(x_val, y_val)
        plt.plot(x_val, y_val,'or')
        plt.show()

    except (SyntaxError, NameError):
        print('Ecuación inválida, por favor verifique.')



main()