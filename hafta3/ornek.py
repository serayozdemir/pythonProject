'''soru:  kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini de bu toplamdan çıkaran
ve geri gönderen python kodunu yazınız palindrom: sağdan ve soldan aynı gözüken'''
def palindrom(*dram):
    toplam= fark=0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -=sayi
    return toplam - fark

palindrom(10,101,55,40,9009)





