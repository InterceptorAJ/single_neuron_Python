import numpy as np
import random as random

inputN = list(map(int, input("Podaj wejścia(dowolne liczby oddzielona spacją: ").split()))
inputN = np.array(inputN)
def Count(inputN):
    counter = 0
    for num in inputN:
        if isinstance(num, tuple):
            break
        counter = counter + 1
    return counter
N = Count(inputN)
z = sum(inputN)
z = np.array(z)
K = int(input("Podaj liczbę epok: "))
ten = float(input("Podaj skok treningowy: "))
print("Liczba i rodzaj wejść: ", inputN)
print ("Ustawiona liczba epok: ", K)
interval1 = float(input("Podaj pierwszą początkową liczbę dla wagi od 0 do 1 - liczba dziesiętna z kropką: "))
interval2 = float(input("Podaj ostatnią początkową liczbę dla wagi od 0 do 1 - liczba dziesiętna z kropką" ))
neuralW = np.random.uniform(low=interval1, high=interval2, size=N)
neuralW = np.array(neuralW)
print ("Początkowe wagi: ")
print (neuralW)
k = 0
for iteration in range(K):
    if k < K:
        y = sum(inputN * neuralW)
        neuralW = neuralW + ten * (z-y) * inputN
        k += 1
    else:
        StopIteration()
print ("Końcowe wagi: ")
print (neuralW)
result = inputN * neuralW
print("Wynik otrzymany: ")
print(sum(result))
print("Wynik rzeczywisty: ")
print(z)
