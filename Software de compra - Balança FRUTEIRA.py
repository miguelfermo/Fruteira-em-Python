def calcular_valor_fruta(frutas, codigo, peso_gramas):

    fruta = frutas.get(codigo)

    if fruta is None:

        print("Código de fruta inválido.")

        return None

    nome_fruta = fruta["nome"]

    preco_por_kg = fruta["preco"]

    peso_kg = peso_gramas / 1000.0

    valor_total = peso_kg * preco_por_kg

    return nome_fruta, valor_total

frutas = {

    "01": {"nome": "Abacate", "preco": 4.09},

    "02": {"nome": "Abacaxi", "preco": 9.90},

    "03": {"nome": "Açaí", "preco": 46.2},

    "04": {"nome": "Acerola", "preco": 29.90},

    "05": {"nome": "Ameixa", "preco": 22.49},

    "06": {"nome": "Amêndoa", "preco": 49.90},

    "07": {"nome": "Amora", "preco": 83.1},

    "08": {"nome": "Araçá", "preco": 39.0},

    "09": {"nome": "Avelã", "preco": 115.49},

    "10": {"nome": "Banana", "preco": 8.2},

    "11": {"nome": "Bergamota", "preco": 6.0},

    "12": {"nome": "Butiá", "preco": 4.0},

    "13": {"nome": "Cacau", "preco": 7.50},

    "14": {"nome": "Caju", "preco": 42.0},

    "15": {"nome": "Cambucá", "preco": 24.0},

    "16": {"nome": "Caqui", "preco": 7.39},

    "17": {"nome": "Carambola", "preco": 16.0},

    "18": {"nome": "Castanha", "preco": 24.0},

    "19": {"nome": "Castanha-do-pará", "preco": 30.0},

    "20": {"nome": "Cereja", "preco": 75.0},

    "21": {"nome": "Coco", "preco": 4.0},

    "22": {"nome": "Damasco", "preco": 79.0},

    "23": {"nome": "Figo", "preco": 33.30},

    "24": {"nome": "Framboesa", "preco": 99.80},

    "25": {"nome": "Gabiroba", "preco": 3.0},

    "26": {"nome": "Goiaba", "preco": 9.0},

    "27": {"nome": "Gravatá", "preco": 9.90},

    "28": {"nome": "Graviola", "preco": 24.0},

    "29": {"nome": "Groselha", "preco": 16.0},

    "30": {"nome": "Guaraná", "preco": 15.8},

    "31": {"nome": "Jabuticaba", "preco": 25.2},

    "32": {"nome": "Jaca", "preco": 5.4},

    "33": {"nome": "Jamelão", "preco": 41.0},

    "34": {"nome": "Jujuba", "preco": 12.3},

    "35": {"nome": "Kiwi", "preco": 22.9},

    "36": {"nome": "Kumquat", "preco": 150.0},

    "37": {"nome": "Laranja", "preco": 5.5},

    "38": {"nome": "Limão", "preco": 3.0},

    "39": {"nome": "Lima", "preco": 14.0},

    "40": {"nome": "Maçã", "preco": 14.7},

    "41": {"nome": "Mamão", "preco": 14.8},

    "42": {"nome": "Mamey", "preco": 25.0},

    "43": {"nome": "Manga", "preco": 3.0},

    "44": {"nome": "Mangaba", "preco": 37.2},

    "45": {"nome": "Maracujá", "preco": 9.80},

    "46": {"nome": "Marmelo", "preco": 8.5},

    "47": {"nome": "Melancia", "preco": 4.0},

    "48": {"nome": "Melão", "preco": 13.0},

    "49": {"nome": "Meloa", "preco": 12.2},

    "50": {"nome": "Mexerica", "preco": 16.0},

    "51": {"nome": "Mirtilo", "preco": 183.0},

    "52": {"nome": "Morango", "preco": 11.0},

    "53": {"nome": "Noz", "preco": 89.0},

    "54": {"nome": "Orangelo", "preco": 8.0},

    "55": {"nome": "Pera", "preco": 10.0},

    "56": {"nome": "Pêssego", "preco": 8.0},

    "57": {"nome": "Pitanga", "preco": 37.0},

    "58": {"nome": "Pinha", "preco": 20.0},

    "59": {"nome": "Pitaia", "preco": 26.0},

    "60": {"nome": "Pitomba", "preco": 60.0},

    "61": {"nome": "Pitangatuba", "preco": 38.0},

    "62": {"nome": "Pindaíba", "preco": 30.0},

    "63": {"nome": "Pequi", "preco": 12.0},

    "64": {"nome": "Pixirica", "preco": 28.9},

    "65": {"nome": "Pistache", "preco": 99.80},

    "66": {"nome": "Romã", "preco": 30.0},

    "67": {"nome": "Rambutão", "preco": 8.0},

    "68": {"nome": "Sapucaia", "preco": 80.0},

    "69": {"nome": "Tangerina", "preco": 26.0},

    "70": {"nome": "Tamarindo", "preco": 40.0},

    "71": {"nome": "Tâmara", "preco": 51.0},

    "72": {"nome": "Uva", "preco": 11.00},

    "73": {"nome": "Vergamota", "preco": 6.0},
}

def exibir_menu():

    print("===== MENU =====")

    print("1. Realizar compra ")

    print("2. Listar itens cadastrados")

    print("3. Menu de alteração")

    print("0. Sair")

def adicionar_produto():

    codigo = input("Digite o código do produto: ")

    if codigo in frutas:

        print("===================================================================")

        print("Código de produto já existente. Não é possível adicionar o produto.")

        print("===================================================================")

        return

    nome = input("Digite o nome do produto: ")

    preco = float(input("Digite o preço por kg do produto: "))

    frutas[codigo] = {"nome": nome, "preco": preco}

    print("Produto adicionado com sucesso.")

def alterar_preco():

    codigo = input("Digite o código do produto para alterar o preço: ")

    novo_preco = float(input("Digite o novo preço por kg do produto: "))

    fruta = frutas.get(codigo)

    if fruta is None:

        print("Código de fruta inválido.")

    else:

        fruta["preco"] = novo_preco

        print("Preço alterado com sucesso.")

def realizar_compra():

    total_compra = 0.0

    continuar_compra = True

    while continuar_compra:

        codigo_fruta = input("Digite o código da fruta (ou '0' para encerrar a compra): ")

        if codigo_fruta == "0":

            continuar_compra = False

        elif codigo_fruta not in frutas:

            print("Código de fruta inválido.")

        else:

            peso = float(input(f"Digite quantas gramas de {frutas[codigo_fruta]['nome']}: "))

            nome_fruta, valor_total = calcular_valor_fruta(frutas, codigo_fruta, peso)

            if valor_total is not None:

                print(f"O valor total para {nome_fruta} é de R$ {valor_total:.2f}")

                total_compra += valor_total

    print("||======================================||")

    print("||======================================||")

    print("||======================================||")

    print(f"||======Total da compra: R$ {total_compra:.2f}")

    print("||======================================||")

    print("||======================================||")

    print("||======================================||")

def listar_itens():

    print("===== ITENS CADASTRADOS =====")

    for codigo, fruta in frutas.items():

        print(f"Código: {codigo}")

        print(f"Nome: {fruta['nome']}")

        print(f"Preço: R$ {fruta['preco']:.2f}")

        print("--------------------")

login = "admin"

senha = "123456"

while True:

    usuario_login = input("Digite o login: ")

    usuario_senha = input("Digite a senha: ")

    if usuario_login == login and usuario_senha == senha:

        print("Login realizado com sucesso!")

        break

    else:

        print("Login ou senha incorretos. Tente novamente.")

opcao = None

while opcao != "0":

    exibir_menu()

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":

        realizar_compra()

    elif opcao == "2":

        listar_itens()

    elif opcao == "3": 

        while True:

            

            print("===== MENU =====")

            print("1. Alterar preço de um produto")

            print("2. Adicionar novo produto")

            print("3. =======Voltar==============")

            opcao = input("Digite a opção desejada: ")

           

            if opcao == "1":

                alterar_preco()

                

            elif opcao == "2":

                adicionar_produto()

                

            elif opcao == "3":     

                break

    elif opcao == "0":

        print("Encerrando o programa...")

    else:

        print("Opção inválida. Tente novamente.")