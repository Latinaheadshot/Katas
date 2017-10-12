# ASCII a = 97 e = 101 i = 105 o = 111 u = 117
# ASCII A = 65 E = 69 I = 73 O = 79 U = 85
letra = input("Escribe UNA NADA MAS letra")

class Vocal():
    def __init__(self,letra):
        self.letra = letra

    def vocal(self, letra):
        code_ascii = ord(letra)
        if code_ascii == 97 or code_ascii == 101 or code_ascii == 105 or code_ascii == 111 or code_ascii == 117 or \
                        code_ascii == 65 or code_ascii == 69 or code_ascii == 73 or code_ascii == 79 or code_ascii == 85:
            return True
        else:
            return False

prueba = Vocal(letra)
regresa = prueba.vocal(letra)

print (regresa)

