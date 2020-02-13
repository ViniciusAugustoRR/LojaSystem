from datetime import datetime
import time
import mysql.connector
from Models.Cliente import ClienteMD
from Models.Equipamento import EquipamentoMD
from Models.Service import ServiceMD
from Models.Responsavel import ResponsavelMD
from Models.Marca import MarcaMd
from mysql.connector import Error

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

    def ConsultarClientes(self):

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

    def ConsultarCliente(self, Cliente_Id: int):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "select * from cliente where id_cliente = %s;"
            cursor.execute(querry, (Cliente_Id, ) )


            for listaItems in cursor:

                Cliente1 = ClienteMD()

                Cliente1.Id = listaItems[0]
                Cliente1.Nome_c = listaItems[1]
                Cliente1.Email = listaItems[2]
                Cliente1.Telefone = listaItems[3]
                Cliente1.Enderec = listaItems[4]



            return Cliente1

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


######################################################################


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

    def ConsultarEquipamentos(self):

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

    def ConsultarEquipamento(self, Equipamento_Id: int):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "select * from equipamento where id_equipamento = %s;"
            cursor.execute(querry, (Equipamento_Id,))


            for listaItems in cursor:
                Equipamento1 = EquipamentoMD()

                Equipamento1.Id = listaItems[0]
                Equipamento1.Serie_N = listaItems[1]
                Equipamento1.Nome = listaItems[2]
                Equipamento1.Modelo = listaItems[3]
                Equipamento1.Acessorios = listaItems[4]
                Equipamento1.Marca_id = listaItems[5]

            return Equipamento1

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


######################################################################

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

    def ConsultarMarcas(self):

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

    def ConsultarMarca(self, Marca_Id: int):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "select * from marca where id_marca = %s;"
            cursor.execute(querry, (Marca_Id,))

            for listaItems in cursor:
                Marca1 = MarcaMd()

                Marca1.Id = listaItems[0]
                Marca1.Nome_Marca = listaItems[1]

            return Marca1

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

    def DeletarMarca(self, Marca_Id: int):
        try:

            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "DELETE FROM marca Where id_marca = %s "

            cursor.execute(querry, (Marca_Id,))

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()


######################################################################


    def CadastrarTecnico(self, Tecnico: ResponsavelMD):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            args = (Tecnico.Nome, Tecnico.Categoria)
            querry = "INSERT INTO responsavel(nome_respons, categoria_respons) " \
                     " VALUES (%s, %s)"

            cursor.execute(querry, args)

            if cursor.lastrowid:
                print("Responsavel com o id " + str(cursor.lastrowid) + " Responsavel com sucesso !!")
            else:
                print("Responsavel n cadastrado")

            db.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

    def ConsultarTecnicos(self):

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
                Tecnico1.Categoria = listaItems[2]

                Tecnicos.append(Tecnico1)

            return Tecnicos

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

    def ConsultarTecnico(self, Tecnico_Id: int):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "select * from responsavel where id_respons = %s;"
            cursor.execute(querry, (Tecnico_Id,))

            for listaItems in cursor:
                Tecnico1 = EquipamentoMD()

                Tecnico1.Id = listaItems[0]
                Tecnico1.Nome = listaItems[1]
                Tecnico1.Categoria = listaItems[2]

            return Tecnico1

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


######################################################################



    def CadastrarService(self, service: ServiceMD):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()


            args = (service.Data_i, service.Data_f, service.Cliente_Id, service.Responsavel_Id, service.Equipamento_Id)
            querry = "INSERT INTO service(data_i, data_f, fk_cliente_id, fk_responsavel_id, fk_equipamento_id)" \
                     " VALUES (%s, %s, %s, %s, %s);"
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

    def ConsultarServices(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            cursor.execute("select * from service;")
            servicesDB = cursor.fetchall()

            services = []

            for listaItems in servicesDB:

                service1 = ServiceMD(data_i=listaItems[1],
                                     data_f=listaItems[2],
                                     cliente_id=listaItems[3],
                                     responsavel_id=listaItems[4],
                                     equipamento_id=listaItems[5])
                service1.Id = listaItems[0]

                services.append(service1)

            return services

        except Error as error:
            print(error)

        finally:
            cursor.close()
            db.close()

    def ConsultarService(self, Service_Id: int):

        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
            cursor = db.cursor()

            querry = "select * from service where id_service = %s;"
            cursor.execute(querry, (Service_Id,))


            for listaItems in cursor:
                Service1 = ServiceMD()

                Service1.Id = listaItems[0]
                Service1.Data_i = listaItems[1].strftime("%d/%m/%Y %H:%M:%S")
                Service1.Data_f = listaItems[2].strftime("%d/%m/%Y %H:%M:%S")
                Service1.Cliente_Id = listaItems[3]
                Service1.Responsavel_Id = listaItems[4]
                Service1.Equipamento_Id = listaItems[5]

            return Service1

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


######################################################################


'''def TesteData(self, Data: datetime):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
        cursor = db.cursor()

        args = (Data, )
        querry = "INSERT INTO teste(datateste)" \
                 " VALUES (%s)"

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
        db.close()'''
'''
CLIENTE = OK
MARCA = OK
RESPOSNAVEIS = OK
EQUIPAMENTO = OK
SERVICES = OK
ALL OK BOIS, WE DID IT
'''
'''
MeuDb = DBfac()
Clientes = MeuDb.ConsultarClientes()
for Cliente in Clientes:
    print(Cliente.Id)
Cliente = MeuDb.ConsultarCliente(8)
print(Cliente.Nome_c)
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
    print(serv.Equipamento_Id)

MeuDb.CadastrarEquipamento(Equipamento)
ClienteNo = ClienteMD()

ClienteNo.Nome_c = "Mila Muniz Pinto"
ClienteNo.Enderec = "Algum predio em salvador fds"
ClienteNo.Telefone = "719284879231"
ClienteNo.Email = "MIlamunizalgodotipo.com"

print(ClienteNo.__dict__)

MeuDb = DBfac()
service = ServiceMD()

service.Cliente_Id = 9
service.Equipamento_Id = 1
service.Responsavel_Id = 1
service.Data_i = datetime.now()
# RECEBE DATA E HORA ATUAL
service.Data_f = datetime(2020, 5, 14, 13, 20, 5)
# ANO -> MÊS -> DIA   /////   HORA -> MINUTO -> SEGUNDO
# .strftime("%d/%m/%Y %H:%M:%S")


MeuDb.CadastrarService(service)'''
