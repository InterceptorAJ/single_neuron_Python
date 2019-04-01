import numpy as np
import random as random

inputN = []
in1 = int(input('Podaj ilość wejść linii: '))
for i in range(in1):
    inputN.append(float(input("Podaj wejście: ")))
print(np.floor(inputN))
question = input('Czy chcesz dodać kolejny zestaw liczb? T/N ')
in2 = 1
while question.upper() == 'T':
    for i in range(in1):
        inputN.append(float(input("Podaj wejście: ")))
    question = input('Czy chcesz dodać kolejny zestaw liczb? T/N ')
    in2 += 1
else:
    pass

print('Wejścia: ')
inputN = np.array(inputN)
inputN = np.split(inputN, in2)
print(inputN)

z = []
for i in range(in2):
    z.append(float(input("Podaj wyjście: ")))
z = np.array(z)
print('Wyjścia: ')
print(z)

K = int(input("Podaj liczbę epok: "))
ten = float(input("Podaj skok treningowy: "))
print("Liczba i rodzaj wejść: ", inputN)
print ("Ustawiona liczba epok: ", K)
interval1 = float(input("Podaj pierwszą początkową liczbę dla wagi od 0 do 1 (liczba dziesiętna z kropką): "))
interval2 = float(input("Podaj ostatnią początkową liczbę dla wagi od 0 do 1 (liczba dziesiętna z kropką): "))
neuralW = np.random.uniform(low=interval1, high=interval2, size=in1)
neuralW = np.array(neuralW)
print ("Początkowe wagi: ")
print (neuralW)
arr_cnt = 0
k = 0
M = in2
for iteration in range(K):
    if k < K:
        for array in inputN:
            for i in z:
                if arr_cnt < M:
                    y = sum(array * neuralW)
                    neuralW = neuralW + ten * (i - y) * array
                    arr_cnt += 1
                else:
                    k += 1
                    arr_cnt = 0
    else:
        StopIteration()
print("Końcowe wagi: ")
print(neuralW)
print("Wyniki otrzymane: ")
for array in inputN:
    result = sum(array * neuralW)
    result = np.array(result)
    print(result)
print("Wyniki rzeczywiste: ")
print(z)
