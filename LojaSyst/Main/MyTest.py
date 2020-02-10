
import re
from datetime import datetime



def convertDateTime( data: str, hora: str):
    datastr = list(re.split("/|:| ", data + " " + hora))
    dataint = []

    for item in datastr:
        dataint.append(int(item))

    datatuple = tuple(dataint)

    return dataint


data = "10/10/2020"
hour = "12:12:12"

datahora = datetime(convertDateTime(data, hour)).strftime("%d/%m/%Y %H:%M:%S")
