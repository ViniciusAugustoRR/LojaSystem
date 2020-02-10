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
    def __init__(self):

        self.Id = int

        self.Data_i = datetime
        self.Data_f = datetime

        self.Cliente_Id = int
        self.Responsavel_Id = int
        self.Equipamento_Id = int

