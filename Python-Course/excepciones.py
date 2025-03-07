def sumar_dos():
    while True:
        a = input('numero: ')
        b = input('numero 2: ')
        try:
            # si sabemos que te va a lanzar una excepcion intentar
            resultado = int(a) + int(b)
            # si el resultado funciono paramos el bucle
        except Exception as e:
            print('pon un numero')
            print(f'Error: {e}')
        else:
            # cuando ya sabemos que no nos va a dar una excepcion
            break
        # finally se ejecuta aun cuando hay excepcion
        finally:
            print('Manejo de excepciones')
    return resultado

print(sumar_dos())


# excepcion ZeroDivisionError
