import mysql.connector
from Models.Cliente import ClienteMD



class DBfac:

    def CadastrarCliente(self, Clientex: ClienteMD):

        db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
        cursor = db.cursor()

        cursor.execute("""INSERT INTO cliente VALUES ('%str')""")

        db.commit()
        cursor.close()


    def PuxarClientes(self):

        db = mysql.connector.connect(host="localhost", user="root", password="", database="lojasyst")
        cursor = db.cursor()
        cursor.execute("select * from cliente;")


        ClienteB = ClienteMD()
        listaItems = []


        for Cliente in cursor:
            for item in Cliente:
                listaItems.append(item)

            ClienteB.Id = listaItems[0]
            ClienteB.Nome_c = listaItems[1]
            ClienteB.Email = listaItems[2]
            ClienteB.Telefone = listaItems[3]
            ClienteB.Enderec = listaItems[4]

            print(ClienteB.Nome_c)

        cursor.close()




MeuDb = DBfac()


MeuDb.PuxarClientes()

ClienteNo = ClienteMD()

ClienteNo.Nome_c = "Mila Muniz Pinto"
ClienteNo.Enderec = "Algum predio em salvador fds"
ClienteNo.Telefone = "719284879231"
ClienteNo.Email = "MIlamunizalgodotipo.com"

MeuDb.CadastrarCliente(ClienteNo)

MeuDb.PuxarClientes()



