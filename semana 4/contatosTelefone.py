contatos = {
    "Alex": {
        "nome": "Alex",
        "telefone": 4472892260,
    },
    "Paulo": {
        "nome": "Paulo",
        "telefone": 5367470712,
    },
    "Sara": {
        "nome": "Sara",
        "telefone": 2683735356,
    },
    "Mateus": {
        "nome": "Juca",
        "telefone": 7156627616,
    },
}

comando = "continue"

while comando != "sair":
    comando = input(
        "Digite o comando desejado -> cadastrar, listar, remover ou sair: ")

    if comando == "cadastrar":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        contatos[nome] = {
            "nome": nome,
            "telefone": telefone,
        }

    if comando == "listar":
        print(contatos)

    if comando == "remover":
        nome = input("Nome: ")
        if nome in contatos:
            contato = contatos[nome]
            print(f'O contato de {nome} foi removido.')
            del contatos[nome]
        else:
            print("Contato não encontrado")

    print()
