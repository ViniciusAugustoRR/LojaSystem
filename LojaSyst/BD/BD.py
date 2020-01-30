import mysql.connector
from Models.Cliente import ClienteMD
from Models.Equipamento import EquipamentoMD
from Models.Service import ServiceMD
from Models.Responsavel import ResponsavelMD
from mysql.connector import Error
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
            listaItems = []

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

            Equipamento1 = EquipamentoMD()
            Equipamentos = []
            listaItems = []

            for Equipamento in cursor:
                for item in Equipamento:
                    listaItems.append(item)

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

            args = (Service.Data, Service.Data_o, Service.Hora, Service.Hora_o, Service.Cliente_Id, Service.Equipamento_Id, Service.Responsavel_Id)
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

            Service1 = ServiceMD()
            Services = []
            listaItems = []

            for Service in cursor:
                for item in Service:
                    listaItems.append(item)

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

            args = (Tecnico.Nome)
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

            cursor.execute("select * from tecnico;")

            Tecnico1 = ResponsavelMD()
            Tecnicos = []
            listaItems = []

            for Service in cursor:
                for item in Service:
                    listaItems.append(item)

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




MeuDb = DBfac()
Clientes = MeuDb.PuxarClientes()

for Cliente in Clientes:
    print(Cliente.Nome_c)

'''ClienteNo = ClienteMD()

ClienteNo.Nome_c = "Mila Muniz Pinto"
ClienteNo.Enderec = "Algum predio em salvador fds"
ClienteNo.Telefone = "719284879231"
ClienteNo.Email = "MIlamunizalgodotipo.com"

print(ClienteNo.__dict__)'''



