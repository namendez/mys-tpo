# TPO Modelado y Simulación 
## Alumnos:
- Méndez Nicolás 
- Suarez Leandro

Aproximación a una ecuación diferencial de primer orden mediante la implementación del algoritmo de Euler.

# Dependencias
Previo a su ejecución se debe instalar matplotlib:

`pip3 install --user matplotlib==3.4.3`
# Uso
El programa recibe los parámetros por línea de comando, graficando el resultado de la aproximación. 

## Parámetros
`-N <float>: cantidad de intervalos entre t0 y tf. Excluyente con -H`

`-H <float>: tamaño del incremento para las aproximaciones, tal que t1 = t0 + H. Excluyente con -N`

`--equation "<equation>": ecuacion diferencial a aproximar. Debe ser tener una sintaxis válida de Python3`

`-t0 <float>: instante inicial`

`-tf <float>: instante final`

`-x0 <float>: condicion inicial`

## Ejemplos
`python3 euler.py -H 0.5 --equation "2*t" -t0 0 -tf 10 -x0 0`

`python3 euler.py -N 20 --equation "cos(t)" -t0 0 -tf 6 -x0 0`
