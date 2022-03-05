class Temperatura:
    def __init__(self,celsius):
        self.set_temp(celsius)

    def get_temp(self):               #metodo GETTER
        return self._temp

    def set_temp(self,valor):         #metodo SETTER
        self._temp = (valor * 1.8) + 32

temp_c = float(input('Informe a temperatura: '))

pessoa = Temperatura(temp_c)

print(pessoa.get_temp())
