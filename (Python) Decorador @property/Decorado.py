class Temperatura:
    def __init__(self,temp):
        self.temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,temp):
        print("Definindo temperatura...")
        self._temp = (temp * 1.8) + 32


temp_c = float(input("Informe a temperatura: "))

pessoa = Temperatura(temp_c)

print("Valor em fahrenheit e {}".format(pessoa.temp))
