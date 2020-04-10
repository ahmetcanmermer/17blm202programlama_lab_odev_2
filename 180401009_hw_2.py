import csv
import sys
def histogram(liste):
    dict = {}
    for item in liste:
        if(item in dict):
            dict[item] = dict[item]+1
        else:
            dict[item] = 1
    return dict
def ort(liste):
    toplam = 0
    for i in range(0,len(liste)):
        toplam += liste[i]
    return int(toplam/len(liste))
def bubble_sort(liste):
    i = len(liste)
    for i in range(i-1,-1,-1):
        for j in range(0,i):
            if(liste[j]>liste[j+1]):
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
    return liste
with open(sys.argv[1]+"input_hw_2.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    liste = []
    for line in csv_reader:
        liste.append(line)
aylar = []
for ay in range(0,len(liste)):
    aylar.append(str(liste[ay][3][5])+str(liste[ay][3][6]))
histogram1 = histogram(aylar)
deger = []
for key,value in histogram1.items():
    print(f"{key}. ay {value} kişi ayrıldı")
    deger.append(value)
bubble_sort(deger)
ortalama = ortalama(deger)
medyan = deger[len(deger)//2]
print(ortalama)
print(medyan)
with open(sys.argv[2]+"180401009_hw_2_output.txt","w") as txt_file:
    txt_file.write(f"ortalama={ortalama}\nmedyan={medyan}")