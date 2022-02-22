def verificar_acao(arg):
    if arg == []:
        print('Ação inexistente.')
        return quit()
    else:
        return True

def get_value(arg, chave):
    valores = arg[0][chave]
    return valores
    