def benim_fonk(n): #sınav sorusu potansiyeli
    return lambda a:a*n

katini_al=benim_fonk(2)
print(katini_al(5))

katini_al=benim_fonk(5)
print(katini_al(5))