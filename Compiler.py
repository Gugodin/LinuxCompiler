from queue import Empty
import string



tokens= [
        ['crear','mkdir'],
        ['mover','cd'],
        ['mostrar','ls'],
        ['editar','mv'],
        ['remover','rm'],
        ['crearA','touch'],
        ['diagonal','/'],
        ['guion','-'],
        ['guionB','_'],
        ['numero',list(string.digits)],
        ['letra',list(string.ascii_letters)]
        ]





if __name__ == '__main__':
    command = input('Escribe tu comando de Linux ').split(' ')

    for i in range(len(command)):
        band = False
        palabra = command[i]
        # print(palabra)

        for e in range(len(tokens)):
            # print(tokens[e][1])
            if palabra == tokens[e][1]:
                print(f'Token: {tokens[e][0]}')
                band = True
                break
        if band == False:       
            for z in range(len(palabra)):

                char = palabra[z]

                for e in range(len(tokens)):

                    if tokens[e][0] == 'numero' or tokens[e][0] == 'letra':

                        if tokens[e][1].count(char) > 0:
                            print(f'Token: {tokens[e][0]}')
                            break
                    
                    elif char == tokens[e][1]:
                        print(f'Token: {tokens[e][0]}')
                        break



    # print(command)