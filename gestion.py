import os
import core
from datetime import datetime
import random

diccCitas = {}
citas = {}

def loadInfoCitas(fileName):
    global diccCitas
    if (core.checkFile('citas.json')):
        diccCitas = core.loadInfo('citas.json')
    else:
        core.crearFile('citas.json', diccCitas)

iniciar = True
def mainMenu():
    os.system('clear') and os.system('cls')
    print('GESTION DE CITAS')
    print('1. Crear cita', '2. Buscar Citas', '3. Modificar cita', '4. Eliminar cita','5.Volver al menu principal', sep = '\n')
    opcion = int(input('Ingrese la opcion que desea realizar: ').strip())

    if (opcion == 1):

        idCita = (str(random.randint(1,10000))).zfill(5)
        nombrePaciente = (input('Ingrese el nombre del paciente: ').strip()).upper()
        fechaCita = input('Ingrese la fecha de la cita programada(dd/mm/aa): ').strip()
        while True:
            try:
                fechaFormat = datetime.strptime(fechaCita, '%d/%m/%Y').date()
                break
            except ValueError:
                print('Formato de fecha no valido')
                os.system('pause') and os.system('sleep 5')
                break
        fechaFinal = fechaFormat.strftime('%d/%m/%Y')

        horaCita = input('Ingrese la hora de la cita programada(hh:mm 24H): ').strip()
        while True:
            try:
                horaFormat = datetime.strptime(horaCita, '%H:%M').time()
                break
            except ValueError:
                print('Formato de hora no valido')
                os.system('pause') and os.system('sleep 5')
                break
        horaFinal = horaFormat.strftime('%H:%M')
        motivoConsulta = (input('Ingrese el motivo de la consulta: ').strip()).upper()

        citas = {
            'idCita': idCita,
            'motivoConsulta': motivoConsulta
        }

        isRepetido = False
        for item in diccCitas:
            checkNombre = diccCitas[item].get('nombrePaciente',-1)
            checkFecha = diccCitas[item].get('fechaCita',-1)
            checkHora = diccCitas[item].get('horaCita',-1)
            if (checkNombre == nombrePaciente) and (checkFecha == fechaFinal) and (checkHora == horaFinal):
                print('Ya existe una cita programada para este paciente en esta hora y fecha')
                isRepetido = True
                os.system('pause') and os.system('sleep 5')
                break
        if not isRepetido:
            citas.update({'nombrePaciente':nombrePaciente})
            citas.update({'fechaCita':fechaFinal})
            citas.update({'horaCita':horaFinal})
            diccCitas.update({f'{idCita}':citas})
        core.crearFile('citas.json',diccCitas)
        os.system('pause') and os.system('sleep 5')

    elif (opcion == 2):

        iniciarBusqueda = True
        while iniciarBusqueda:
            os.system('clear') and os.system('cls')
            print('BUSCAR CITA')
            print('1. Buscar IDCita', '2. Buscar por nombre: ', '3. Buscar por fecha: ', '4. Volver al menu principal: ', sep = '\n')
            opcion = int(input('Ingrese la opcion que desea realizar: ').strip())

            if (opcion == 1):

                #BUSQUEDA POR ID:
                print('LISTADO DE CITAS')
                for item in diccCitas:
                    print(f'ID :{diccCitas[item]["idCita"]}, NOMBRE: {diccCitas[item]["nombrePaciente"]}')
                idBusqueda = input('Ingrese el ID de la cita: ').strip()
                if idBusqueda in diccCitas:
                    os.system('clear') and os.system('cls')
                    print('RESULTADO BUSQUEDA CITA')
                    print(f'ID:{idBusqueda}')
                    print(f'NOMBRE: {diccCitas[idBusqueda]["nombrePaciente"]}')
                    print(f'FECHA: {diccCitas[idBusqueda]["fechaCita"]}')
                    print(f'HORA: {diccCitas[idBusqueda]["horaCita"]}')
                    print(f'MOTIVO: {diccCitas[idBusqueda]["motivoConsulta"]}')
                    os.system('pause') and os.system('sleep 5')
                else:
                    print('ID no se encuentra entre las citas programadas')
                    os.system('pause') and os.system('sleep 10')

            elif (opcion == 2):

                #BUSQUEDA POR NOMBRE
                print('LISTADO DE CITAS')
                for item in diccCitas:
                    print(f'NOMBRE PACIENTE :{diccCitas[item]["nombrePaciente"]}')
                nombreBusqueda = (input('Ingrese el nombre del paciente que desea buscar: ').strip()).upper()
                encontrado = False
                for llave in diccCitas:
                    if nombreBusqueda == diccCitas[llave]['nombrePaciente']:
                        print('------------------------------------------------------')
                        print('RESULTADO BUSQUEDA CITA')
                        print(f'ID:{llave}')
                        print(f'NOMBRE: {diccCitas[llave]["nombrePaciente"]}')
                        print(f'FECHA: {diccCitas[llave]["fechaCita"]}')
                        print(f'HORA: {diccCitas[llave]["horaCita"]}')
                        print(f'MOTIVO: {diccCitas[llave]["motivoConsulta"]}')
                        os.system('pause') and os.system('sleep 5')
                        encontrado = True
                if not encontrado:
                    print('EL PACIENTE BUSCADO NO SE ENCUENTRA EN EL SISTEMA')
                    os.system('pause') and os.system('sleep 10')

            elif (opcion == 3):

                #BUSQUEDA POR FECHA
                print('LISTADO DE CITAS')
                for item in diccCitas:
                    print(f'NOMBRE PACIENTE: {diccCitas[item]["nombrePaciente"]},FECHA: {diccCitas[item]["fechaCita"]}')
                fechaBusqueda = input('Ingrese la fecha de la cita que desea buscar: ').strip()
                encontrado = False
                for llave in diccCitas:
                    if fechaBusqueda == diccCitas[llave]['fechaCita']:
                        print('------------------------------------------------------')
                        print('RESULTADO BUSQUEDA CITA')
                        print(f'ID:{llave}')
                        print(f'NOMBRE: {diccCitas[llave]["nombrePaciente"]}')
                        print(f'FECHA: {diccCitas[llave]["fechaCita"]}')
                        print(f'HORA: {diccCitas[llave]["horaCita"]}')
                        print(f'MOTIVO: {diccCitas[llave]["motivoConsulta"]}')
                        os.system('pause') and os.system('sleep 5')
                        encontrado = True
                if not encontrado:
                    print('LA FECHA DE LA CITA NO SE ENCUENTRA EN EL SISTEMA')
                    os.system('pause') and os.system('sleep 5')
            elif (opcion == 4):
                iniciarBusqueda = False
            else:
                print('Opcion no valida')
                iniciarBusqueda = False 

    elif (opcion == 3):

        #MODIFICAR 
        os.system('clear') and os.system('cls')

        print('LISTADO DE CITAS')
        for item in diccCitas:
            print(f'ID: {diccCitas[item]["idCita"]}, NOMBRE PACIENTE: {diccCitas[item]["nombrePaciente"]}')
        idBusqueda = input('Ingrese el ID de la cita que desea modificar: ').strip()
        fecha = input('Ingrese nueva fecha para la cita(dd/mm/aa): ').strip()
        while True:
            try:
                fechaFormat = datetime.strptime(fecha, '%d/%m/%Y').date()
                break
            except ValueError:
                print('Formato de fecha no valido')
                os.system('pause') and os.system('sleep 5')
                break
        fechaMod = fechaFormat.strftime('%d/%m/%Y')

        hora = input('Ingrese nueva hora para la cita(H:M 24H): ').strip()
        while True:
            try:
                horaFormat = datetime.strptime(hora, '%H:%M').time()
                break
            except ValueError:
                print('Formato de hora no valido')
                os.system('pause') and os.system('sleep 5')
                break
        horaMod = horaFormat.strftime('%H:%M')

        isIdEncontrado = False
        for llave in diccCitas:
            if idBusqueda == diccCitas[llave]['idCita']:
                diccCitas[llave]['nombrePaciente'] = (input('Ingrese nuevo nombre del paciente o enter para omitir: ').strip()).upper() or diccCitas[llave]['nombrePaciente']
                diccCitas[llave]['motivoConsulta'] = (input('Ingrese el nuevo motivo de la consulta del paciente o enter para omitir: ').strip()).upper() or diccCitas[llave]['motivoConsulta']
                diccCitas[llave]['fechaCita'] = fechaMod
                diccCitas[llave]['horaCita'] = horaMod
                isIdEncontrado = True
                os.system('pause') and os.system('sleep 5')
                break
        if not isIdEncontrado:
            print('ID no se encuentra entre las citas programadas')
            os.system('pause') and os.system('sleep 5')

        core.editarInfo('citas.json', diccCitas)
        
    elif (opcion == 4):

        #ELIMINAR CITA MEDICA
        os.system('clear') and os.system('cls')
        print('LISTADO DE CITAS')
        for item in diccCitas:
            print(f'ID: {diccCitas[item]["idCita"]}, NOMBRE PACIENTE: {diccCitas[item]["nombrePaciente"]}, FECHA CITA: {diccCitas[item]["fechaCita"]}')
        idBusqueda = input('Ingrese el ID de la cita que desea eliminar: ').strip()

        isIdEncontrado = False
        for llave in diccCitas:
            if idBusqueda in diccCitas[llave]['idCita']:
                diccCitas.pop(llave)
                core.editarInfo('citas.json', diccCitas)
                print('Cita eliminada')
                isIdEncontrado = True
                os.system('pause') and os.system('sleep 5')

        if not isIdEncontrado:
            print('ID no se encuentra entre las citas programadas')
            os.system('pause') and os.system('sleep 5')

    elif (opcion == 5):
        iniciar = False
        if iniciar:
            mainMenu()
    else:
        print('Opcion no valida')
        mainMenu()