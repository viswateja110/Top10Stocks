import requests
import zipfile
import os
import shutil
from datetime import date
import redis
RESOURCES_PATH="./resources/"
def GetFileName():
    currDate=date.today().strftime('%d%m%y')
    return 'EQ{}_CSV'.format(currDate)

def GetEquityFile(fileToDownload):
    URL="https://www.bseindia.com/download/BhavCopy/Equity/"+fileToDownload
    r= requests.get(URL,allow_redirects=True)
    
    if(not os.path.exists(RESOURCES_PATH)):
        os.mkdir('resources')

    if 'x-zip-compressed' in r.headers.get('content-type'):
        open(fileToDownload,'wb').write(r.content)
        shutil.move(fileToDownload,RESOURCES_PATH)
        if UnzipFile(fileToDownload):
            os.remove(RESOURCES_PATH+fileToDownload)

def UnzipFile(fileName):
    try:
        pathToZipFile=RESOURCES_PATH+fileName
        zipObj=zipfile.ZipFile(pathToZipFile,'r')
        zipObj.extractall(pathToZipFile.rsplit('.',1)[0])
        zipObj.close()
        return True
    except Exception as e:
        print e.message      
        return False



