import matplotlib
import numpy as np
import random as random
import matplotlib.pyplot as plt


inputN = list(map(float, input("Podaj wejścia(dowolne liczby oddzielona spacją): ").split()))
inputN = np.array(inputN)
def Count(inputN):
    counter = 0
    for num in inputN:
        if isinstance(num, tuple):
            break
        counter = counter + 1
    return counter
N = Count(inputN)
z = sum(inputN) / 100
z = np.array(z)
K = int(input("Podaj liczbę epok: "))
ten = float(input("Podaj skok treningowy: "))
print("Liczba i rodzaj wejść: ", inputN)
print ("Ustawiona liczba epok: ", K)
interval1 = float(input("Podaj pierwszą liczbę dla zakresu początkowego dla wag: "))
interval2 = float(input("Podaj drugą liczbę dla zakresu początkowego dla wag: "))
neuralW = np.random.uniform(low=interval1, high=interval2, size=N)
neuralW = np.array(np.double(neuralW))
print ("Początkowe wagi: ")
print (neuralW)
k = 0
learn_list = []
for iteration in range(K):
    if k < K:
        y = sum(inputN * neuralW)
        delta = (z - y)
        neuralW = neuralW + ten * delta * inputN
        k += 1
        learn_list.append(delta)
    else:
        StopIteration()
print ("Końcowe wagi: ")
print (neuralW)
result = inputN * neuralW
print("Wynik otrzymany: ")
z1 = sum(result)
print(z1)
print("Wynik rzeczywisty: ")
print(z)
print("Różnica: ")
diff = z - z1
print(diff)
print("Różnica w %: ")
diff1 = (z - z1)/z * 100
print(diff1)

x = []
for i in range(K):
    x.append(i)
y = np.array(learn_list)
plt.plot(x, y)
plt.xlabel('Epoki')
plt.ylabel('Błąd')
plt.title('Relacja nauczania (zmniejszanie błędu) do czasu (epoki)')
plt.grid(True)
plt.savefig('zad1.png')
plt.show()
