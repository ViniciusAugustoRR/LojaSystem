from datetime import datetime

'''
 data_o:datetime.date,
 data: datetime.date,

 cliente: ClienteMD,
 responsavel: ResponsavelMD,
 equipamento: EquipamentoMD
 '''

from datetime import datetime
from Models.Cliente import ClienteMD
from Models.Responsavel import ResponsavelMD
from Models.Equipamento import EquipamentoMD

class ServiceMD:
    def __init__(self, data_i: datetime, data_f: datetime, cliente_id: int, responsavel_id: int, equipamento_id: int):

        self.Id = int

        self.Data_i = data_i
        self.Data_f = data_f

        self.Cliente_Id = cliente_id
        self.Responsavel_Id = responsavel_id
        self.Equipamento_Id = equipamento_id

