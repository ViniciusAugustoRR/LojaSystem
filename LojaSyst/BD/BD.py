import mysql.connector
from Models.Cliente import ClienteMD
from mysql.connector import Error


class DBfac:

    def CadastrarCliente(self, Clientex: ClienteMD):

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

            args = (Clientex.Nome_c, Clientex.Email, Clientex.Telefone, Clientex.Enderec)
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


            Cliente1 = ClienteMD()
            Clientes = []
            listaItems = []


            for Cliente in cursor:
                for item in Cliente:
                    listaItems.append(item)

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

    def DeleteCliente(self, Cliente_Id):

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



''' 
MeuDb = DBfac()
Clientes = MeuDb.PuxarClientes()

for Cliente in Clientes:
    print(Cliente.Id)

ClienteNo = ClienteMD()

ClienteNo.Nome_c = "Mila Muniz Pinto"
ClienteNo.Enderec = "Algum predio em salvador fds"
ClienteNo.Telefone = "719284879231"
ClienteNo.Email = "MIlamunizalgodotipo.com"
 '''



