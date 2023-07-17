import json
import os 

def checkFile(fileName):
    try:
        with open('data/'+fileName, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
    
def crearFile(*args):
    if(checkFile(args[0])==False):
        with open('data/'+args[0],'w') as write_file:
            json.dump(args[1], write_file, indent = 4)
            write_file.close()
    else:
        with open('data/'+args[0],'r+') as file:
            file_data = json.load(file)
            file_data.update(args[1])
            file.seek(0)
            json.dump(file_data,file, indent = 4)
            file.close()

def loadInfo(fileName):
    if(checkFile(fileName)==True):
        with open('data/'+fileName,'r') as read_file:
            dicc = json.load(read_file)
        return dicc
    
def editarInfo(*args):
    with open('data/'+args[0],'w') as write_file:
        json.dump(args[1],write_file,indent = 4)
        write_file.close()