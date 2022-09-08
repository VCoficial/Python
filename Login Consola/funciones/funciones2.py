def validarListaCaracteres(texto,validar):
 bien=True

 for i in texto:
    
    if i in validar:
        bien=False

    return bien