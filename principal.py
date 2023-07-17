import os
import core
import gestion


if __name__ == '__main__':
    inicar = True
    while inicar:
        os.system('clear') and os.system('cls')
        print('MENU PRINCIPAL:')
        print('1.Gestion citas', '2. Salir del programa', sep = '\n')
        opcion = int(input('Ingrese una opcion del menu: '))
        try:
            if opcion == 1:
                gestion.loadInfoCitas('citas.json')
                gestion.mainMenu()
            elif opcion == 2:
                print('--------------------------------------------------------------------')
                print('GRACIAS POR USAR NUESTRO SOFTWARE. ESPERE PRONTO LA VERSION 1.2')
                print('--------------------------------------------------------------------')
                inicar = False
            else:
                print('Opcion no valida, ingrese una opcion del menu')
        except ValueError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error: {e}')                    
