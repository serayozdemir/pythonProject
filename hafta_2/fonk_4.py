def topla_ne_varsa_git(*a): #ben buraya canımın istediği kadar parametre gönderebilirim demek
    toplam=0
    for deger in a:
        toplam+=deger
    return toplam

print(topla_ne_varsa_git(3,5,9,15,36))