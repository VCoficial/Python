from controller.get import mirarapi,miraruno
from controller.post import actualizarUsuario
from libs.consumir import crearUsuarios, eliminar


menu_options = {
    1: 'Mostrar 1',
    2: 'Insertar 2',
    3: 'Editar 3',
    4: 'Eliminar',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     return  mirarapi()

def option2():
     return crearUsuarios()

def option3():
     return actualizarUsuario()

def option4():
     return eliminar()

if __name__=='__main__':
    while(True):
        print_menu()
        option = " "
        try:
            option = int(input('ELIGE TU OPCION : '))
        except:
            print('MAL. POR FAVOR INGRESA UN NUMERO ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()    
        elif option == 5:
            print('GRACIAS POR ESTAR CON NOSTROS ')
            exit()
        else:
            print('IDIOTA NO SABE LEER SOLO NUMEROS ENTRE 1 Y 5.')