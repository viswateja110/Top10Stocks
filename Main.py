import equitydownloader as ed
import CSVParser


if __name__=='__main__':    
    ed.GetEquityFile(ed.GetFileName()+'.zip')
    CSVParser.ParseCsv(ed.RESOURCES_PATH+ed.GetFileName()+'/'+ed.GetFileName().replace('_','.'))
