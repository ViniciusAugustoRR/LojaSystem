from Models.Service import ServiceMD, ClienteMD, ResponsavelMD, EquipamentoMD
from KViews.Tela01 import Cad
from kivy.app import App


def main():
    Cad().run()


if __name__ == '__main__':
    main()

























'''Resp1 = ResponsavelMD()

listaR = []

Resp1.Id = 1
Resp1.nome = "Marcia"
listaR.append(Resp1)
Resp1.Id = 2
Resp1.nome = "Bedsom"
listaR.append(Resp1)
Resp1.Id = 3
Resp1.nome = "bebado"
listaR.append(Resp1)


cliente1 = ClienteMD()

cliente1.Id = 123#int(input("Cliente id: "))
cliente1.Nome_c = "vINICUS"#str(input("Cliente nome: "))
cliente1.Email = "Emaiosafa .com "#str(input("Cliente Email: "))


serv = ServiceMD()

serv.Id = int(input("ID SERVIÇO : "))

data = []
for c in range(0, 3):
    data.append(int(input(".")))

serv.Data = (data[0], data[1], data[2])
serv.Data_o = (data[0], data[1], data[2])

serv.Hora = (11, 22, 40)
serv.Hora_o = (13, 12, 20)

ep = EquipamentoMD()

ep.Serie_N = "234w"
ep.Equipamento_Nome = "Televisão"
ep.Acessorios = "Pernas e Antena"
ep.Modelo = "UXNVI923NFOA"
ep.MarcaId = "SAMSUMG"


serv.Equipamento = ep
serv.ClienteS = cliente1

print(serv.Id)
print(serv.Data)
print(serv.Data_o)
print(serv.Hora_o)
print(serv.Hora)
print("=========================================================================")

print(serv.Equipamento.Serie_N)
print(serv.Equipamento.Equipamento_Nome)
print(serv.Equipamento.Acessorios)
print(serv.Equipamento.Modelo)
print(serv.Equipamento.MarcaId)
print("=========================================================================")

print(serv.ClienteS.Id)
print(serv.ClienteS.Nome_c)
print(serv.ClienteS.Enderec)
print(serv.ClienteS.Telefone)
print(serv.ClienteS.Email)
print("=========================================================================")'''



