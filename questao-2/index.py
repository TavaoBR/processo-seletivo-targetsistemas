def verificar_letra_a(texto):
    texto = texto.lower()
    quantidade_a = texto.count('a')
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vez(es) no texto.")
    else:
        print(f"A letra 'a' não foi encontrada no texto")
        
texto_usuario = input("Digite um texto: ")

verificar_letra_a(texto_usuario)            