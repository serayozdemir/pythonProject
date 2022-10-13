liste=[]
for i in range(0,5):
    liste.append(eval(input))

def siralama_fonksiyonu(a):
    return a*a-20

liste.sort(key=siralama_fonksiyonu)
print(liste)
