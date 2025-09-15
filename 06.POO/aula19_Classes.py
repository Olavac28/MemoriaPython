class Veiculo:
    def __init__(self, fabricante, modelo): #construtor
        self.__fabricante = fabricante #usar self__nome para deixar atributo privado
        self.__modelo = modelo
        self.__cor = None

    def movimentar(self): #self é quase obrigatório para funções dee objetos
        print(f"veiculo {self.__fabricante} {self.__modelo} se movimentando")

    def setColor(self, cor):
        self.__cor = cor
    def getColor(self):
        return self.__cor

meuVeiculo = Veiculo("fiat", "uno")
meuVeiculo.movimentar()

meuVeiculo.setColor("preto")
print(f"Cor do meu veiculo = {meuVeiculo.getColor()}")