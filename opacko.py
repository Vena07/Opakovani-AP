nejmensi1 = []
nejvetsi1 = []
ranodmcisla = []
import random
import time
def Nserazeni(cislo):
    global nejmensi1,i
    for i in range(len(cisla)):
        cisla2 =cisla
        nejmensi1.append(min(cisla2))
        cisla2.remove(min(cisla2))
    for i in range(len(cisla)):
        cisla2 = cisla
        nejvetsi1.append(max(cisla2))
        cisla2.remove(max(cisla2))

def generovani_senzami():
    global ranodmcisla
    ranodmcisla = []
    for i in range(10):
        number = random.randint(0,10)
        ranodmcisla.append(number)


cisla = [3,5,8,1,2,4,6,7]
nejmensi = sorted(cisla)
nejvetsi = sorted(cisla,reverse=True)
prumer = sum(cisla)/len(cisla)

print("díky funkce")
print(nejmensi)
print(nejvetsi)
print(prumer)


print("Pdoel cyklu podminek atd.")
Nserazeni(cisla)
print(nejmensi1)
print(nejvetsi1)

while True:
    generovani_senzami()
    prumer = sorted(ranodmcisla)
    print("Pro kolegu noska")
    print(ranodmcisla)
    print(max(ranodmcisla))
    print(min(ranodmcisla))
    print(prumer[4])
    time.sleep(5)