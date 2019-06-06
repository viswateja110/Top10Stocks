import csv
import json
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
def ParseCsv(fileName):
    data={}
    with open(fileName,'r') as csvObj:
        csvReader=csv.DictReader(csvObj)
        filterRow={}
        for row in csvReader:
            code=row['SC_CODE']
            filterRow={'SC_NAME':row['SC_NAME'].strip(),'OPEN':row['OPEN'],'HIGH':row['HIGH'],'LOW':row['LOW'],'CLOSE':row['CLOSE']}            
            data[code]=filterRow
            r.set(code,str(data[code]))
        
    with open("equityData.json","w") as jsonFile:
        jsonFile.write(json.dumps(data,indent=4))
                
