class sinif:
    metin= ""
    def __init__(self, a):
        self.metin= a
    def __del__(self):
        print("beni siliyorrr :(")

nesne= sinif("metin")
#print(nesne.metin)
del nesne