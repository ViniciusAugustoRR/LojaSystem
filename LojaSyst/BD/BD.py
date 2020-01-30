import mysql.connector
from Models.Cliente import ClienteMD
from Models.Equipamento import EquipamentoMD
from Models.Service import ServiceMD
from Models.Responsavel import ResponsavelMD
from Models.Marca import MarcaMd
from mysql.connector import Error
from datetime import datetime
import copy

class DBfac:

    def CadastrarCliente(self, Cliente: ClienteMD):

        '''PASSO A PASSO,
        ABRIR CONEXÃO COM O BANCO
        CRIAR CURSOR
        FAZER UMA TUPLA COM OS ITENS QUE SERÃO INSERIDOS
        FAZER A QUERRY QUE SERA EXECUTADA
        EXECUTAR O COMANDO DA QUERRY COM OS DADOS QUE SERÃO INSERIDOS
        CONFIRMAR SE A OPERAÇÃO DEU CERTO OU ERRADO
        FECHAR A CONEXÃO E O CURSOR'''

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            args = (Cliente.Nome_c, Cliente.Email, Cliente.Telefone, Cliente.Enderec)
            querry = "INSERT INTO cliente(nome_cliente, email, telefone, endereco) " \
                     " VALUES (%s, %s, %s, %s)"

            cursor.execute(querry, args)

            if cursor.lastrowid:
                print("Cliente com o id " + str(cursor.lastrowid) + "Cadastrado com sucesso !!")
            else:
                print("Cliente n cadastrado")

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def PuxarClientes(self):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()


            cursor.execute("select * from cliente;")
            ClientesCur = cursor.fetchall()

            Clientes = []

            for listaItems in ClientesCur:

                Cliente1 = ClienteMD()

                Cliente1.Id = listaItems[0]
                Cliente1.Nome_c = listaItems[1]
                Cliente1.Email = listaItems[2]
                Cliente1.Telefone = listaItems[3]
                Cliente1.Enderec = listaItems[4]

                Clientes.append(Cliente1)

            return Clientes



        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def DeleteCliente(self, Cliente_Id: int):

        try:

            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "DELETE FROM cliente Where id_cliente = %s "

            cursor.execute(querry, (Cliente_Id,))

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

##########################################

    def CadastrarEquipamento(self, Equipamento : EquipamentoMD):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            args = (Equipamento.Serie_N, Equipamento.Nome, Equipamento.Modelo, Equipamento.Acessorios, Equipamento.Marca_id)
            querry = "INSERT INTO equipamento(serie_num, nome_equipamento, modelo, acessorios, fk_marca_id) " \
                     " VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(querry, args)

            if cursor.lastrowid:
                print("Equipamento com o id " + str(cursor.lastrowid) + "Cadastrado com sucesso !!")
            else:
                print("Equipamento n cadastrado")

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def PuxarEquipamentos(self):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            cursor.execute("select * from equipamento;")
            EquipamentosDb = cursor.fetchall()

            Equipamentos = []

            for listaItems in EquipamentosDb:

                Equipamento1 = EquipamentoMD()

                Equipamento1.Id = listaItems[0]
                Equipamento1.Serie_N = listaItems[1]
                Equipamento1.Nome = listaItems[2]
                Equipamento1.Modelo = listaItems[3]
                Equipamento1.Acessorios = listaItems[4]
                Equipamento1.Marca_id = listaItems[5]

                Equipamentos.append(Equipamento1)

            return Equipamentos



        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def DeletarEquipamento(self, Equip_Id: int):
        try:

            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "DELETE FROM equipamento Where id_equipamento = %s "

            cursor.execute(querry, (Equip_Id,))

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

##############################################

    def CadastrarService(self, Service: ServiceMD):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            args = (Service.Data_i, Service.Data_f, Service.Hora_i, Service.Hora_f, Service.Cliente_Id, Service.Equipamento_Id, Service.Responsavel_Id)
            querry = "INSERT INTO service(data_i, data_f, hora_i, hora_f, fk_cliente_id, fk_responsavel_id, fk_equipamento_id)" \
                     " VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(querry, args)

            if cursor.lastrowid:
                print("Service com o id " + str(cursor.lastrowid) + "Cadastrado com sucesso !!")
            else:
                print("Service n cadastrado")

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def PuxarServices(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            cursor.execute("select * from service;")
            ServicesDB = cursor.fetchall()

            Services = []

            for listaItems in ServicesDB:
                Service1 = ServiceMD()

                Service1.Id = listaItems[0]
                Service1.Data = listaItems[1]
                Service1.Data_o = listaItems[2]
                Service1.Hora = listaItems[3]
                Service1.Hora_o = listaItems[4]
                Service1.Cliente_Id = listaItems[5]
                Service1.Responsavel_Id = listaItems[6]
                Service1.Equipamento_Id = listaItems[7]

                Services.append(Service1)

            return Services

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def DeletarService(self, Service_Id: int):
        try:

            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "DELETE FROM service Where id_service = %s "

            cursor.execute(querry, (Service_Id,))

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

################################################

    def CadastrarTecnico(self, Tecnico: ResponsavelMD):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            args = (Tecnico.Nome, )
            querry = "INSERT INTO responsavel(nome_respons) " \
                     " VALUES (%s)"

            cursor.execute(querry, args)

            if cursor.lastrowid:
                print("Responsavel com o id " + str(cursor.lastrowid) + "Responsavel com sucesso !!")
            else:
                print("Responsavel n cadastrado")

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def PuxarTecnicos(self):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            cursor.execute("select * from responsavel;")
            TecnicosMd = cursor.fetchall()

            Tecnicos = []

            for listaItems in TecnicosMd:
                Tecnico1 = ResponsavelMD()

                Tecnico1.Id = listaItems[0]
                Tecnico1.Nome = listaItems[1]

                Tecnicos.append(Tecnico1)

            return Tecnicos

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def DeletarTecnicos(self, Tecnico_Id: int):
        try:

            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "DELETE FROM responsavel Where id_respons = %s "

            cursor.execute(querry, (Tecnico_Id,))

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()


###############################################

    def CadastrarMarca(self, Marca: MarcaMd):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            args = (Marca.Nome_Marca, )
            querry = "INSERT INTO marca(nome_marca) " \
                     " VALUES (%s)"

            cursor.execute(querry, args)

            if cursor.lastrowid:
                print("Marca com o id " + str(cursor.lastrowid) + "Cadastrada com sucesso !!")
            else:
                print("Marca n cadastrado")

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()
    def PuxarMarcas(self):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            cursor.execute("select * from marca;")
            MarcasDb = cursor.fetchall()

            Marcas = []

            for listaItems in MarcasDb:
                Marca1 = MarcaMd()

                Marca1.Id = listaItems[0]
                Marca1.Nome_Marca = listaItems[1]


                Marcas.append(Marca1)

            return Marcas

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()






'''
CLIENTE = OK
MARCA = OK

'''
'''MeuDb = DBfac()

Clientes = MeuDb.PuxarClientes()
for Cliente in Clientes:
    print(Cliente.Id)
marcas = MeuDb.PuxarMarcas()
for marc in marcas:
    print(marc.Nome_Marca)
Equipamentos = MeuDb.PuxarEquipamentos()
for Equip in Equipamentos:
    print(Equip.Nome)
    print(Equip.Marca_id)
Responsaveis = MeuDb.PuxarTecnicos()
for resp in Responsaveis:
    print(resp.Nome)

Services = MeuDb.PuxarServices()
for serv in Services:
    print(serv.Cliente_Id)
    print(serv.Data_i)
    print(serv.Hora_i)
    print(serv.Equipamento_Id)'''
'''service = ServiceMD()

service.Cliente_Id = 9
service.Equipamento_Id = 1
service.Responsavel_Id = 1

service.Data_i = datetime.date(2020, 1, 2)
service.Hora_i = datetime.time(14, 34, 13)

service.Data_f = datetime.date(2020, 2, 1)
service.Hora_f = datetime.time(15, 23, 3)

MeuDb.CadastrarService(service)'''
'''Equipamento.Nome = "Radio"
Equipamento.Acessorios = "Carregador"
Equipamento.Modelo = "987sa98fankf"
Equipamento.Serie_N = "7sfsfsZ2"
Equipamento.Marca_id = 3

MeuDb.CadastrarEquipamento(Equipamento)'''
'''ClienteNo = ClienteMD()

ClienteNo.Nome_c = "Mila Muniz Pinto"
ClienteNo.Enderec = "Algum predio em salvador fds"
ClienteNo.Telefone = "719284879231"
ClienteNo.Email = "MIlamunizalgodotipo.com"

print(ClienteNo.__dict__)'''



