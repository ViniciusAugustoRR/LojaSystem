
import re
from datetime import datetime
from BD.BD import DBfac


def convertDateTime(data: str, hora: str):
    datastr = list(re.split("/|:| ", data + " " + hora))
    dataint = []

    for item in datastr:
        dataint.append(int(item))

    datatimetype = datetime(dataint[2], dataint[1], dataint[0], dataint[3], dataint[4], dataint[5])

    return datatimetype


data = "12/12/2012"
hour = "13:11:14"

print(type(data))

datahora = convertDateTime(data, hour)

print(datahora)
print(type(datahora))

db = DBfac()

