meme_dict = {
    "F": "Respeito",
    "FF": "Desistir",
    "GG": "Good Game/Bom jogo",
    "RUSHAR": "Ir pra cima",
    "Broken": "Algo que está desbalanceado"
}

neynoprime = input("Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas): ")

if neynoprime in meme_dict.keys():
    print(meme_dict[neynoprime])
else:
    print('Está palavra não está neste dicionário')
