def birim_islem(**birim):
    print("birimin tipi:" , type(birim))
    print("birim adı:" , birim["ad"])
    print("birim tipi:" , birim["tip"])
    print("birim yılı:" , birim["yil"])

birim_islem(ad="balikesir", tip="üniversite", yil=1992)
