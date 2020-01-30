'''
                 data_o:datetime.date, hora_o: datetime.time,
                 data: datetime.date, hora: datetime.time,

                 cliente: ClienteMD,
                 responsavel: ResponsavelMD,
                 equipamento: EquipamentoMD'''

import datetime
from Models.Cliente import ClienteMD
from Models.Responsavel import ResponsavelMD
from Models.Equipamento import EquipamentoMD

class ServiceMD:
    def __init__(self):

        self.Id = int

        self.Data_o = datetime.date
        self.Hora_o = datetime.time

        self.Data = datetime.date
        self.Hora = datetime.time

        self.Cliente_Id = int
        self.Responsavel_Id = int
        self.Equipamento_Id = int

