import matplotlib
import numpy as np
import random as random
import matplotlib.pyplot as plt

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
learn_list = []
for iteration in range(K):
        for array in inputN:
            for a in array:
                for i in z:
                    if arr_cnt < M and k < K:
                        y = sum(a * neuralW)
                        delta = i - y
                        neuralW = neuralW + ten * delta * a
                        arr_cnt += 1
                    elif arr_cnt == M:
                        arr_cnt = 0
                        k += 1
                        learn_list.append(delta)
                    elif k == K:
                        StopIteration()

print("Końcowe wagi: ")
print(neuralW)
print("Wyniki otrzymane: ")
z1 = []
result = []
for array in inputN:
    result = sum(array * neuralW)
    z1.append(result)
print(z1)
print("Wyniki rzeczywiste: ")
print(z)
# print("Różnica: ")
# delta = z - z1
# print('deltuk', delta)
# for i in delta:
#     if i < 0:
#         i = i * (-1)
#     elif i > 0:
#         pass
#     elif i == 0:
#         i = 0
# print(delta)
# print("Różnica w %: ")
# diff1 = delta * 100
# print(diff1)

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
