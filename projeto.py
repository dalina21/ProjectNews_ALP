from ChatGPT import *
from Uteis import *

logado = False
tipo_usuario = None
idade = 0
id = 1

user_reporter = {}
user_leitor = {}
novo_coment = {}
dados = {}
coment_users = []

# Informações pré-cadastradas para testes
dados['dalina'] = {'senha': '1231', 'tipo': 'r', 'nome': 'Dalina'}
dados['daniel'] = {'senha': '1231', 'tipo': 'r', 'nome': 'Daniel'}
dados['dalina21'] = {'senha': '1231', 'tipo': 'l', 'nome': 'Dalina2'}
dados['daiani16'] = {'senha': '1231', 'tipo': 'l', 'nome': 'Daiani'}
noticias = [
    {"ID": 1,
     "Titulo": "Leis de Newton",
     "Descricao": "As leis de Newton estão entre as mais importantes leis da Física e são usadas para determinar a dinâmica dos corpos.",
     "Noticia": "As leis de Newton fundamentam a base da Mecânica Clássica. São um conjunto de três leis capazes de explicar a dinâmica "
                "que envolve o movimento dos corpos. Essas leis foram publicadas pela primeira vez pelo físico inglês Isaac Newton, no ano "
                "de 1687, em sua obra de três volumes intitulada Princípios Matemáticos da Filosofia Natural. A Primeira Lei de Newton é "
                "chamada de Lei da Inércia, Essa lei diz que, ao menos que haja alguma força resultante não nula sobre um corpo, esse deverá "
                "manter-se em repouso ou se mover ao longo de uma linha reta com velocidade constante. A Lei de Inércia também explica o "
                "surgimento das forças inerciais, isto é, as forças que surgem quando os corpos estão sujeitos a alguma força capaz de produzir "
                "neles uma aceleração. Por exemplo: ao pisar no acelerador do carro, um motorista pode sentir-se comprimido em seu banco, como se "
                "houvesse uma força puxando-o para trás. A Segunda Lei de Newton, também conhecida como Lei da Superposição de Forças ou como "
                "Princípio Fundamental da Dinâmica. A Terceira Lei de Newton recebe o nome de Lei da Ação e Reação. Essa lei diz que todas as "
                "forças surgem aos pares: ao aplicarmos uma força sobre um corpo (ação), recebemos desse corpo a mesma força (reação), com mesmo "
                "módulo e na mesma direção, porém com sentido oposto.",
     "autor": "dalina",
     "DataDia": 10, "DataMes": 12, "DataAno": 2023,
     "Comentarios": [],
     "Curtidas": 0}
]

def criarConta():
    while True:
        print('\n\t\t====== Criar Conta ======')
        while True:
            nome = input("\nDigite seu nome: ")
            if nome:
                break
            else:
                print("\n\t\033[31mInformação Inválida!\033[m")

        while True:
            user = input("Usuario: ")
            if user:
                if user in dados:
                    print("\n\t\033[31mEsse nome de usuário já existe.\n\033[m")
                else:
                    break
            else:
                print("\n\t\033[31mInformação Inválida!\n\033[m")

        while True:
            senh = input("Senha : ")
            if len(senh) < 4:
                print('\n\t\033[31mSua senha precisa ter no mínimo 4 dígitos\n\033[m')
            else:
                break

        while True:
            senh1 = input("Confirme a Senha: ")
            if senh != senh1:
                print("\n\t\033[31mSenhas não Coincidem\n\033[m")
            else:
                break

        while True:
            log = False
            tipo_usuario = input(
                "\nDigite:\nR para criar uma conta de reporter ou\nL para criar uma conta de leitor: ")
            if tipo_usuario.lower() not in ["l", "r"]:
                print("\n\t\033[31mTipo de Usuário Inválido.\033[m")
            if tipo_usuario.lower() == "r":
                try:
                    idade = int(input("\nDigite sua idade: "))
                except ValueError:
                    print("\n\t\033[31mInformação Inválida!\033[m")
                    continue

                if idade < 18:
                    print("\n\t\033[31mPara criar conta como repórter você precisa ter \n\tpelo menos 18 anos.\n\033[m")
                    main()
                elif idade >= 18:
                    print(f"\n\t\033[32mUsuário Repórter cadastrado com Sucesso!\n\033[m")
                    dados[user] = {'senha': senh, 'tipo': tipo_usuario, 'nome': nome}
                    log = True
                    break
            elif tipo_usuario.lower() == "l":
                print(f"\n\t\033[32mUsuário Leitor cadastrado com Sucesso!\n\033[m")
                dados[user] = {'senha': senh, 'tipo': tipo_usuario, 'nome': nome}
                log = True
                break

        if log:
            break
    return tipo_usuario

def login():
    tent = 4
    for i in range(0, tent):

        tent -= 1
        print('\n\t\t====== Login ======')
        while True:
            login1 = input("\nUsuário: ")
            if login1:
                break
            else:
                print(f"\n\033[31mInformação Inválida!\033[m")
        while True:
            senha1 = input("Senha: ")
            if senha1:
                break
            else:
                print(f"\n\033[31mInformação Inválida!\n\033[m")

        if (login1 in dados) and (senha1 in dados[login1]["senha"]):
            print("=" * 61)
            print(f"\n\033[32mBem Vindo(a) ao Sistema de Notícias da Católica, {dados[login1]['nome']}!\033[m\n")
            if dados[login1]['tipo'] == "r":
                user_reporter['reporter'] = login1
                if reporterMenu():
                    break
            elif dados[login1]['tipo'] == "l":
                user_leitor['leitor'] = login1
                if leitorMenu():
                    break
        if tent > 1:
            print(f"\n\033[31mUsuário ou Senha Incorretos. Você tem mais {tent} Tentativas.\033[m")
        elif tent == 1:
            print(f"\n\033[31mUsuário ou Senha Incorretos. Você tem mais {tent} Tentativa.\033[m")
        elif tent == 0:
            print(f"\n\033[31mUsuário ou Senha Incorretos. Você foi desconectado.\033[m")
    main()

def reporterMenu():
    global id
    while True:
        print("=" * 61)
        print('\n\t\t\tMenu Repórter\n')
        print('Escolha uma opção para prosseguir:\n'
              '\n\t[1] Criar Notícias\n '
              '\t[2] Editar Notícias\n'
              '\t[3] Remover Notícias\n'
              '\t[4] Ver ID Notícias\n'
              '\t[5] Abrir Notícias\n'
              '\t[6] Mudar Senha\n'
              '\t[0] Deslogar')
        pgReporter = input("\n")
        print("_" * 61)
        if pgReporter == "0":
            main()
            break

        elif pgReporter == "1":
            print('\n\t\t====== Criar Notícias ======')
            autor = user_reporter['reporter']
            while True:
                noticiaTitu = input("\nDigite o Título : ")
                if noticiaTitu:
                    break
                else:
                    print('\n\t\033[31mÉ preciso digitar alguma informação no campo do Título!\033[m')
                    continue
            while True:
                noticiaDesc = input("Digite a Descrição : ")
                if noticiaDesc:
                    break
                else:
                    print('\n\t\033[31mÉ preciso digitar alguma informação no campo da Descrição!\n\033[m')
                    continue
            while True:
                noticiaComp = input("Digite a Notícia : ")
                if noticiaComp:
                    break
                else:
                    print('\n\t\033[31mÉ preciso digitar alguma informação no campo da Notícia!\n\033[m')
                    continue

            print('\nDigite a Data: ')
            while True:
                try:
                    data_dia = int(input('Dia: '))
                    data_mes = int(input('Mês: '))
                    data_ano = int(input('Ano: '))
                except ValueError:
                    print('\n\t\033[31mInformação Inválida!\n\033[m')
                    continue
                if (1 <= data_dia <= 31) and (1 <= data_mes <= 12) and (0 < data_ano <= 2023):
                    id += 1
                    noticias.append({"ID": id, "Titulo": noticiaTitu, "Descricao": noticiaDesc, "Noticia": noticiaComp,
                                     "autor": autor, "DataDia": data_dia,
                                     "DataMes": data_mes, "DataAno": data_ano, "Comentarios": [], "Curtidas": 0})
                    print("\n\t\033[32mNotícia Enviada com Sucesso!\n\033[m")

                    SalvarNoticias(noticias, autor)

                    for noticia in noticias:
                        id = noticia['ID']
                    print(f'\t=> O ID dessa notícia é: {id}\n')
                    break
                else:
                    print('\n\t\033[31mData Inválida!\n\033[m')
                    print('Digite novamente: ')


        elif pgReporter == "2":
            while True:
                print('\n\t\t====== Editar Notícia ======\n')
                print('=> Apenas o usuário que publicou a notícia poderá editá-la!')
                confirmar = input('\nAperte ENTER para prosseguir')
                if len(confirmar) > 0:
                    print("\n\t\033[31mNão insira nenhuma informação, apenas aperte ENTER!\033[m")
                else:
                    break
            try:
                id_edit = int(input("\nDigite o ID da notícia que deseja editar: "))
            except ValueError:
                print("\n\t\033[31mInformação Inválida!\n\033[m")
                continue
            id_check = False
            for noticia in noticias:
                if noticia['ID'] == id_edit:
                    id_check = True
                    while True:
                        if user_reporter['reporter'] in dados and dados[user_reporter['reporter']]["tipo"] == 'r' and user_reporter['reporter'] == noticia['autor']:
                            while True:
                                senh_editar = input('Digite sua senha: ')
                                if senh_editar:
                                    break
                                else:
                                    print("\n\t\033[31mInformação Inválida!\n\033[m")
                            if senh_editar == dados[user_reporter['reporter']]["senha"]:
                                while True:
                                    while True:
                                        print('\n=> Deseja editar a notícia toda? (s/n) ')
                                        resposta = input('')
                                        if resposta:
                                            break
                                        else:
                                            print("\n\t\033[31mInformação Inválida!\n\033[m")
                                    if resposta.lower() == 's':
                                        while True:
                                            noticia['Titulo'] = input("Digite o novo título: ")
                                            if noticia['Titulo']:
                                                break
                                            else:
                                                print(
                                                    '\n\t\033[31mÉ preciso digitar alguma informação no campo do Título!\033[m')
                                                continue
                                        while True:
                                            noticia['Descricao'] = input("Digite a nova descrição: ")
                                            if noticia['Descricao']:
                                                break
                                            else:
                                                print(
                                                    '\n\t\033[31mÉ preciso digitar alguma informação no campo ds Descrição!\033[m')
                                                continue
                                        while True:
                                            noticia['Noticia'] = input("Digite a nova notícia: ")
                                            if noticia['Noticia']:
                                                break
                                            else:
                                                print('\n\t\033[31mÉ preciso digitar alguma informação no campo da Notícia!\033[m')
                                                continue
                                        while True:
                                            try:
                                                noticia['DataDia'] = int(input('Dia: '))
                                                noticia['DataMes'] = int(input('Mês: '))
                                                noticia['DataAno'] = int(input('Ano: '))
                                            except ValueError:
                                                print('\n\t\033[31mInformação Inválida!\n\033[m')
                                                continue

                                            if (1 <= noticia['DataDia'] <= 31) and (
                                                    1 <= noticia['DataMes'] <= 12) and (
                                                    0 < noticia['DataAno'] <= 2023):
                                                break
                                            else:
                                                print('\n\t\033[31mData Inválida!\n\033[m')
                                                print('Digite novamente: ')
                                            print("\n\t\033[32mNotícia atualizada com sucesso!\n\033[m")
                                            break
                                        SalvarNoticias(noticias, user_reporter['reporter'])
                                        reporterMenu()
                                        break
                                    elif resposta.lower() == 'n':
                                        while True:
                                            print('\nQual parte da notícia deseja editar?\n'
                                                  'T - Título\n'
                                                  'D - Descrição\n'
                                                  'N - Notícia\n'
                                                  'DT - Data\n'
                                                  '0 - Menu do usuário\n')
                                            resp_02 = input('')
                                            if resp_02.lower() == 't':
                                                while True:
                                                    noticia['Titulo'] = input("Digite o novo título: ")
                                                    if noticia['Titulo']:
                                                        print("\n\t\033[32mNotícia atualizada com sucesso!\n\033[m")
                                                        SalvarNoticias(noticias, user_reporter['reporter'])
                                                        break
                                                    else:
                                                        print('\n\t\033[31mÉ preciso digitar alguma informação no campo do Título!\033[m')
                                                        continue

                                            elif resp_02.lower() == 'd':
                                                while True:
                                                    noticia['Descricao'] = input("Digite a nova descrição: ")
                                                    if noticia['Titulo']:
                                                        print("\n\t\033[32mNotícia atualizada com sucesso!\n\033[m")
                                                        SalvarNoticias(noticias, user_reporter['reporter'])
                                                        break
                                                    else:
                                                        print(
                                                            '\n\t\033[31mÉ preciso digitar alguma informação no campo da Descrição!\033[m')
                                                        continue
                                            elif resp_02.lower() == 'n':
                                                while True:
                                                    noticia['Noticia'] = input("Digite a nova notícia: ")
                                                    if noticia['Noticia']:
                                                        print("\n\t\033[32mNotícia atualizada com sucesso!\n\033[m")
                                                        SalvarNoticias(noticias, user_reporter['reporter'])
                                                        break
                                                    else:
                                                        print('\n\t\033[31mÉ preciso digitar alguma informação no campo da Notícia!\033[m')

                                                        continue
                                            elif resp_02.lower() == 'dt':
                                                while True:
                                                    try:
                                                        noticia['DataDia'] = int(input('Dia: '))
                                                        noticia['DataMes'] = int(input('Mês: '))
                                                        noticia['DataAno'] = int(input('Ano: '))
                                                    except ValueError:
                                                        print('\n\t\033[31mInformação Inválida!\n\033[m')
                                                        continue

                                                    if (1 <= noticia['DataDia'] <= 31) and (
                                                            1 <= noticia['DataMes'] <= 12) and (
                                                            0 < noticia['DataAno'] <= 2023):
                                                        print("\n\t\033[32mNoticia atualizada com sucesso!\n\033[m")
                                                        SalvarNoticias(noticias, user_reporter['reporter'])
                                                        break
                                                    else:
                                                        print('\n\t\033[31mData Inválida!\n\033[m')
                                                        print('Digite novamente: ')

                                            elif resp_02 == '0':
                                                reporterMenu()
                                                break
                                            else:
                                                print('\n\t\033[31mResposta Inválida!\n\033[m')
                                    else:
                                        print('\n\t\033[31mResposta Inválida!\n\033[m')
                                        break
                            else:
                                print("\n\t\033[31mSenha Incorreta.\n\033[m")
                                break
                        else:
                            print("\n\033[31m=> Essa notícia não foi publicada por você.\033[m")
                            print("\033[31m=> Apenas o usuário que publicou a notícia poderá elitá-la!\n\033[m")
                            reporterMenu()
                            break
            if not id_check:
                print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

        elif pgReporter == "3":
            while True:
                print('\n\t====== Remover Notícia ======\n')
                print('=> Apenas o usuário que publicou a notícia poderá removê-la!')
                confirmar2 = input('\nAperte ENTER para prosseguir')
                if len(confirmar2) > 0:
                    print("\n\t\033[31mNão insira nenhuma informação, apenas aperte ENTER!\033[m")
                else:
                    break
            try:
                id_remove = int(input("\nDigite o ID da noticia que deseja remover: "))
            except ValueError:
                print("\n\t\033[31mInformação Inválida!\n\033[m")
                continue
            remove_id = False
            for noticia in noticias:
                if noticia['ID'] == id_remove:
                    remove_id = True
                    while True:
                        if user_reporter['reporter'] in dados and dados[user_reporter['reporter']]["tipo"] == 'r' and user_reporter['reporter'] == noticia['autor']:
                            while True:
                                senh_remover = input('Digite sua senha: ')
                                if senh_remover:
                                    break
                                else:
                                    print("\n\t\033[31mInformação Inválida!\n\033[m")
                            if senh_remover == dados[user_reporter['reporter']]["senha"]:
                                confirm = input("\nTem certeza que deseja remover esta notícia? (s/n): ")
                                if confirm.lower() == 's':
                                    noticias.remove(noticia)
                                    print("\n\t\033[32mNotícia removida com sucesso!\n\033[m")
                                    SalvarNoticias(noticias, user_reporter['reporter'])
                                    break
                                elif confirm.lower() == 'n':
                                    print("\n\t\033[31mOperação cancelada.\n\033[m")
                                    break
                            else:
                                print("\n\t\033[31mSenha Incorreta!\n\033[m")
                        else:
                            print("\n\033[31m=> Essa notícia não foi publicada por você.\033[m")
                            print("\033[31m=> Apenas o usuário que publicou a notícia poderá removê-la!\n\033[m")
                            break
                    break

            if not remove_id:
                print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

        elif pgReporter == "4":
            if noticias:
                for noticia in noticias:
                    print("_" * 61)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}"
                        f"\nPublicada por: {noticia['autor']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\n")

            else:
                print("\n\t\033[31mNenhuma notícia foi criada ainda.\n\033[m")

        elif pgReporter == "5":
            while True:
                print('-' * 61)
                print('\n\t====== Abrir Notícias ======\n')
                print('Escolha uma das opções abaixo:\n')
                print('\t[1] Abrir notícia por ID')
                print('\t[2] Abrir apenas suas publicações')
                print('\t[3] Abrir todas as notícias')
                print('\t[4] Gerar PDF da notícia')
                print('\t[5] Fazer pesquisa no Chat GPT')
                print('\t[0] Sair')
                visualizar = input('\n')

                if visualizar == '0':
                    break

                elif visualizar == '1':
                    try:
                        id_view = int(input("\nDigite o ID da notícia que deseja ver: "))
                    except ValueError:
                        print("\n\t\033[31mInformação Inválida.\n\033[m")
                        continue
                    id_encontrado = False
                    for noticia in noticias:
                        if noticia['ID'] == id_view:
                            id_encontrado = True
                            print('-' * 61)
                            print(f'Título: {noticia["Titulo"]}\n')
                            print(f'Descrição: {noticia["Descricao"]}\n')
                            news = noticia["Noticia"]
                            print('Notícia:', textwrap.fill(news, width=100))
                            print(f'\nID da notícia: {noticia["ID"]}')
                            print(f'Data de publicação: {noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}')
                            print(f'Publicada por: {noticia["autor"]}')
                            print(f'\nCurtidas: {noticia["Curtidas"]}\n')
                            print('======================== Comentários ========================')
                            for dicionario in coment_users:
                                if dicionario["id"] == noticia["ID"]:
                                    print(f'\t => {dicionario["usuario"]}: {dicionario["comentario"]}\n')

                    if not id_encontrado:
                        print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

                elif visualizar == '2':
                    noticia_user = []
                    usuario = False
                    user = user_reporter['reporter']

                    for noticia in noticias:
                        if noticia['autor'] == user:
                            usuario = True
                            noticia_user.append(noticia)

                    if user in dados:
                        if dados[user]['tipo'] == 'r' and len(noticia_user) == 0:
                            print("\n\t\033[31mEsse usuário não publicou nenhuma notícia ainda.\n\033[m")
                            print('Deseja publicar sua primeira notícia?\n'
                                  '\n\t[1] Sim'
                                  '\n\t[2] Não')
                            resp = input('\n')
                            if resp == '1':
                                print('\n\t\t====== Criar Notícias ======')
                                autor = user_reporter['reporter']
                                while True:
                                    noticiaTitu = input("\nDigite o Título : ")
                                    if noticiaTitu:
                                        break
                                    else:
                                        print(
                                            '\n\t\033[31mÉ preciso digitar alguma informação no campo do Título!\033[m')
                                        continue
                                while True:
                                    noticiaDesc = input("Digite a Descrição : ")
                                    if noticiaDesc:
                                        break
                                    else:
                                        print(
                                            '\n\t\033[31mÉ preciso digitar alguma informação no campo da Descrição!\n\033[m')
                                        continue
                                while True:
                                    noticiaComp = input("Digite a Notícia : ")
                                    if noticiaComp:
                                        break
                                    else:
                                        print(
                                            '\n\t\033[31mÉ preciso digitar alguma informação no campo da Notícia!\n\033[m')
                                        continue

                                print('\nDigite a Data: ')
                                while True:
                                    try:
                                        data_dia = int(input('Dia: '))
                                        data_mes = int(input('Mês: '))
                                        data_ano = int(input('Ano: '))
                                    except ValueError:
                                        print('\n\t\033[31mInformação Inválida!\n\033[m')
                                        continue
                                    if (1 <= data_dia <= 31) and (1 <= data_mes <= 12) and (0 < data_ano <= 2023):
                                        id += 1
                                        noticias.append({"ID": id, "Titulo": noticiaTitu, "Descricao": noticiaDesc,
                                                         "Noticia": noticiaComp,
                                                         "autor": autor, "DataDia": data_dia,
                                                         "DataMes": data_mes, "DataAno": data_ano, "Comentarios": [],
                                                         "Curtidas": 0})
                                        print("\n\t\033[32mNotícia Enviada com Sucesso!\n\033[m")

                                        SalvarNoticias(noticias, autor)

                                        for noticia in noticias:
                                            id = noticia['ID']
                                        print(f'\t=> O ID dessa notícia é: {id}\n')
                                        break
                                    else:
                                        print('\n\t\033[31mData Inválida!\n\033[m')
                                        print('Digite novamente: ')
                                    break
                            elif resp == '2':
                                break
                            else:
                                print('\n\t\033[31mInformação Inválida!\n\033[m')
                                break

                    else:
                        print("\n\t\033[31mEste usuário não se encontra cadastrado no sistema.\n\033[m")

                    if usuario:
                        print('-' * 61)
                        print(f'\n\t======= Notícias do usuário(a): {user}  =======\n')

                        n = len(noticia_user)
                        for i in range(n):
                            for j in range(0, n - i - 1):
                                if noticia_user[j]['Curtidas'] < noticia_user[j + 1]['Curtidas']:
                                    auxiliar = noticia_user[j]
                                    noticia_user[j] = noticia_user[j + 1]
                                    noticia_user[j + 1] = auxiliar

                        for noticia in noticia_user:
                            print('-' * 61)
                            print(f'Título: {noticia["Titulo"]}\n')
                            print(f'Descrição: {noticia["Descricao"]}\n')
                            news = noticia["Noticia"]
                            print('Notícia:', textwrap.fill(news, width=100))
                            print(f'\nID da notícia: {noticia["ID"]}')
                            print(f'Data de publicação: {noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}')
                            print(f'Publicada por: {noticia["autor"]}')
                            print(f'\nCurtidas: {noticia["Curtidas"]}\n')
                            print('======================== Comentários ========================')
                            for dicionario in coment_users:
                                if dicionario["id"] == noticia["ID"]:
                                    print(f'\t => {dicionario["usuario"]}: {dicionario["comentario"]}\n')
                            print('=' * 61)

                elif visualizar == '3':
                    if noticias:
                        n = len(noticias)
                        for i in range(n):
                            for j in range(0, n - i - 1):
                                if noticias[j]['Curtidas'] < noticias[j + 1]['Curtidas']:
                                    auxiliar = noticias[j]
                                    noticias[j] = noticias[j + 1]
                                    noticias[j + 1] = auxiliar

                        for noticia in noticias:
                            print('-' * 61)
                            print(f'Título: {noticia["Titulo"]}\n')
                            print(f'Descrição: {noticia["Descricao"]}\n')
                            news = noticia["Noticia"]
                            print('Notícia:', textwrap.fill(news, width=100))
                            print(f'\nID da notícia: {noticia["ID"]}')
                            print(f'Data de publicação: {noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}')
                            print(f'Publicada por: {noticia["autor"]}')
                            print(f'\nCurtidas: {noticia["Curtidas"]}\n')
                            print('======================== Comentários ========================')
                            for dicionario in coment_users:
                                if dicionario["id"] == noticia["ID"]:
                                    print(f'\t => {dicionario["usuario"]}: {dicionario["comentario"]}\n')
                            print('=' * 61)

                    else:
                        print(f"\n\t\033[31mNenhuma notícia foi publicada ainda!\n\033[m")

                elif visualizar == '4':
                    print('\n\t====== Gerar PDF da notícia ======\n')
                    try:
                        id_pdf = int(input("Digite o ID da notícia que deseja gera o PDF: "))
                    except ValueError:
                        print("\n\t\033[31mInformação Inválida.\n\033[m")
                        continue
                    pdf_check = False
                    for noticia in noticias:
                        if noticia['ID'] == id_pdf:
                            pdf_check = True
                            GerarPDF(noticias, id_pdf)

                    if not pdf_check:
                        print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

                elif visualizar == '5':
                    print('-' * 61)
                    print('\n\t====== Fazer pesquisa no Chat GPT ======\n')
                    print('=> O programa fará uma pesquisa resumida no Chat GPT, sobre\no assunto da notícia que for fornecida o ID\n')
                    try:
                        id_chat = int(input("Digite o ID da notícia que deseja fazer a pesquisa: "))
                    except ValueError:
                        print("\n\t\033[31mInformação Inválida.\n\033[m")
                        continue
                    pesquisa = False
                    for noticia in noticias:
                        if noticia['ID'] == id_chat:
                            print(f'\nAssunto dessa notícia: "{noticia["Titulo"]}"\n')
                            pesquisa = True
                            conteudo = str({noticia["Titulo"]})
                            PesquisarChatGPT(conteudo)
                            break

                    if not pesquisa:
                        print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

                else:
                    print('\n\t\033[31mInformação Inválida! \n\tResponda com 1, 2, 3, 4, 5 ou 0\n\033[m')

        elif pgReporter == "6":
            print('\n\t\t====== Mudar Senha ======')
            while True:
                mudar_senha = input("\nTem certeza que deseja mudar sua senha? (s/n): ")
                if mudar_senha.lower() == 's':
                    while True:
                        senha_atual = input('\nDigite sua senha atual: ')
                        if senha_atual:
                            break
                        else:
                            print('\n\t\033[31mNenhuma informação foi inserida!\033[m')

                    if senha_atual == dados[user_reporter['reporter']]["senha"]:
                        while True:
                            while True:
                                nova_senha = input('\n=> Digite sua nova senha: ')
                                if nova_senha:
                                    break
                                else:
                                    print('\n\t\033[31mNenhuma informação foi inserida!\n\033[m')

                            while True:
                                nova_senha2 = input("=> Confirme a Senha : ")
                                if nova_senha2:
                                    break
                                else:
                                    print('\n\t\033[31mNenhuma informação foi inserida!\n\033[m')

                            if len(nova_senha) < 4:
                                print('\n\t\033[31mSua senha precisa ter no mínimo 4 digitos\n\033[m')
                            elif nova_senha != nova_senha2:
                                print("\n\t\033[31mSenhas não Coincidem\033[m")
                            else:
                                print("\n\t\033[32mSenha atualizada com sucesso!\n\033[m")
                                dados[user_reporter['reporter']]['senha'] = nova_senha
                                reporterMenu()
                                break
                    else:
                        print(f"\n\t\033[31mSenha Incorreta!\033[m")
                elif mudar_senha.lower() == 'n':
                    break
                else:
                    print(f"\n\t\033[31mResposta Inválida!\033[m")
        else:
            print('\n\t\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5, 6 ou 0\033[m')


def leitorMenu():
    while True:
        print("=" * 61)
        print('\n\t\t\tMenu Leitor\n')
        print('Escolha uma opção para prosseguir:\n'
              '\n\t[1] Buscar notícia\n'
              '\t[2] Comentar notícia\n'
              '\t[3] Curtir notícia\n'
              '\t[4] Ver notícias por ID\n'
              '\t[5] Mudar Senha\n'
              '\t[6] Gerar PDF da notícia\n'
              '\t[7] Fazer pesquisa no Chat GPT\n'
              '\t[0] Deslogar')
        pgLeitor = input("\n")
        print("_" * 61)

        if (pgLeitor == '0'):
            main()
            break

        elif (pgLeitor == '1'):
            print('\n\t\t====== Buscar notícia ======\n')
            print('Escolha uma opção para prosseguir:\n'
                  "\n\t[1] Buscar por ID\n"
                  "\t[2] Buscar por Assunto\n")
            pgL1 = input("")
            if pgL1 == "1":
                try:
                    verId2 = int(input('\nDigite o ID da notícia que vc quer buscar: '))
                except ValueError:
                    print("\n\t\033[31mInformação Inválida!\033[m")
                    continue
                busca2 = False
                for noticia in noticias:
                    if noticia['ID'] == verId2:
                        busca2 = True
                        print('-' * 61)
                        print(f'Título: {noticia["Titulo"]}\n')
                        print(f'Descrição: {noticia["Descricao"]}\n')
                        news = noticia["Noticia"]
                        print('Notícia:', textwrap.fill(news, width=100))
                        print(f'\nID da notícia: {noticia["ID"]}')
                        print(f'Data de publicação: {noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}')
                        print(f'Publicada por: {noticia["autor"]}')
                        print(f'\nCurtidas: {noticia["Curtidas"]}\n')
                        print('======================== Comentários ========================')
                        for dicionario in coment_users:
                            if dicionario["id"] == noticia["ID"]:
                                print(f'\t => {dicionario["usuario"]}: {dicionario["comentario"]}\n')
                        break
                if not busca2:
                    print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

            elif pgL1 == "2": #Falta Testar
                noticias_assunto = []
                while True:
                    verId3 = input('\nDigite o Assunto que você quer buscar: ')
                    if verId3:
                        break
                    else:
                        print("\n\t\033[31mInformação Inválida!\033[m")

                print("_" * 61)
                assunto = False

                for noticia in noticias:
                    if verId3 in noticia['Noticia'] or verId3 in noticia['Titulo']:
                        assunto = True
                        noticias_assunto.append(noticia)

                n = len(noticias_assunto)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if noticias_assunto[j]['Curtidas'] < noticias_assunto[j + 1]['Curtidas']:
                            auxiliar = noticias_assunto[j]
                            noticias_assunto[j] = noticias_assunto[j + 1]
                            noticias_assunto[j + 1] = auxiliar

                for noticia in noticias_assunto:
                    print('-' * 61)
                    print(f'Título: {noticia["Titulo"]}\n')
                    print(f'Descrição: {noticia["Descricao"]}\n')
                    news = noticia["Noticia"]
                    print('Notícia:', textwrap.fill(news, width=100))
                    print(f'\nID da notícia: {noticia["ID"]}')
                    print(f'Data de publicação: {noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}')
                    print(f'Publicada por: {noticia["autor"]}')
                    print(f'\nCurtidas: {noticia["Curtidas"]}\n')
                    print('======================== Comentários ========================')
                    for dicionario in coment_users:
                        if dicionario["id"] == noticia["ID"]:
                            print(f'\t => {dicionario["usuario"]}: {dicionario["comentario"]}\n')

                if not assunto:
                    print("\n\t\033[31mAssunto não encontrado.\n\033[m")

            else:
                print("_" * 61)
                print("\n\t\033[31mInformação Inválida!\n\033[m")

        elif (pgLeitor == '2'):
            print('\n\t\t====== Comentar notícia ======\n')
            comentario = False
            try:
                busca = int(input('Digite o ID da notícia que você deseja comentar: '))
            except ValueError:
                print("\n\t\033[31mInformação Inválida!\n\033[m")
                continue
            for noticia in noticias:
                if noticia['ID'] == busca:
                    while True:
                        comentario = input('\nDigite o comentário que você deseja adicionar: ')
                        if comentario:
                            break
                        else:
                            print("\n\t\033[31mInformação Inválida!\033[m")

                    usuario = user_leitor['leitor']
                    noticia['Comentarios'].append(comentario)
                    print('\n\t\033[32mSeu comentário foi adicionado a notícia!\033[m')
                    novo_coment = {'usuario': usuario, 'comentario': comentario, 'id': busca}
                    coment_users.append(novo_coment)
                    comentario = True
                    break

            if not comentario:
                print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

        elif (pgLeitor == '3'):
            print('\n\t\t====== Curtir notícia ======\n')
            curtir = False
            try:
                curtida = int(input('Digite o ID da notícia que você deseja curtir: '))
            except ValueError:
                print("\n\t\033[31mInformação Inválida!\n\033[m")
                continue
            for noticia in noticias:
                if noticia['ID'] == curtida:
                    curtir = True
                    noticia['Curtidas'] += 1
                    print('\n\t\033[32mSua curtida foi contabilizada!\033[m')
            if not curtir:
                print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

        elif (pgLeitor == '4'):
            print('\n\t\t====== Ver notícias por ID ======\n')
            if noticias:
                for noticia in noticias:
                    print("_" * 61)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}"
                        f"\nPublicada por: {noticia['autor']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\n")

            else:
                print("\n\t\033[31Nenhuma notícia foi criada ainda.\n\033[m")

        elif pgLeitor == '5':
            print('\n\t\t====== Mudar Senha ======\n')
            while True:
                mudar_senha = input("\nTem certeza que deseja mudar sua senha? (s/n): ")
                if mudar_senha:
                    break
                else:
                    print("\n\t\033[31mInformação Inválida!\033[m")
            while True:
                if mudar_senha.lower() == 's':
                    while True:
                        senha_atual = input('\nDigite sua senha atual: ')
                        if senha_atual:
                            break
                        else:
                            print("\n\t\033[31mInformação Inválida!\033[m")

                    if senha_atual == dados[user_leitor['leitor']]["senha"]:
                        while True:
                            while True:
                                nova_senha_leitor = input('\n=> Digite sua nova senha: ')
                                if nova_senha_leitor:
                                    break
                                else:
                                    print("\n\t\033[31mInformação Inválida!\033[m")
                            while True:
                                nova_senha2_leitor = input("=> Confirme sua Senha : ")
                                if nova_senha2_leitor:
                                    break
                                else:
                                    print("\n\t\033[31mInformação Inválida!\033[m")

                            if len(nova_senha_leitor) < 4:
                                print('\n\t\033[31mSua senha precisa ter no mínimo 4 digitos\n\033[m')
                            elif nova_senha_leitor != nova_senha2_leitor:
                                print("\n\t\033[31mSenhas não Coincidem\n\033[m")
                            else:
                                print("\n\t\033[32mSenha atualizada com sucesso!\n\033[m")
                                dados[user_leitor['leitor']]['senha'] = nova_senha_leitor
                                leitorMenu()
                                break
                    else:
                        print(f"\n\t\033[31mSenha Incorreta!\033[m")
                elif mudar_senha.lower() == 'n':
                    break
                else:
                    print(f"\n\t\033[31mInformação Inválida!\033[m")

        elif pgLeitor == '6':
            try:
                id_pdf2 = int(input("\nDigite o ID da notícia que deseja gerar o PDF: "))
            except ValueError:
                print("\n\t\033[31mInformação Inválida.\n\033[m")
                continue
            pdf_check2 = False
            for noticia in noticias:
                if noticia['ID'] == id_pdf2:
                    pdf_check2 = True
                    GerarPDF(noticias, id_pdf2)

            if not pdf_check2:
                print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

        elif pgLeitor == '7':
            print('-' * 61)
            print('\n\t====== Fazer pesquisa no Chat GPT ======\n')
            print('=> O programa fará uma pesquisa resumida no Chat GPT, sobre\no assunto da notícia que for fornecida o ID\n')
            try:
                id_chat2 = int(input("Digite o ID da notícia que deseja fazer a pesquisa: "))
            except ValueError:
                print("\n\t\033[31mInformação Inválida.\n\033[m")
                continue
            pesquisa2 = False
            for noticia in noticias:
                if noticia['ID'] == id_chat2:
                    print(f'\nAssunto dessa notícia: {noticia["Titulo"]}\n')
                    pesquisa2 = True
                    conteudo = str({noticia["Titulo"]})
                    PesquisarChatGPT(conteudo)
                    break

            if not pesquisa2:
                print("\n\t\033[31mEsse ID não está vinculado a nenhuma notícia.\n\033[m")

        else:
            print('\n\t\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5, 6 ou 0\033[m')

def main():
    global tipo_usuario
    while True:
        print("=" * 61)
        print('\n\tBem vindo(a) ao Sistema de Notícias da Católica\n')
        print("=" * 61)
        print('\nEscolha uma opção para prosseguir:\n'
              '\n\t[1] Criar Conta\n'
              '\t[2] Login\n'
              '\t[0] sair\n')
        pgMenu = input("")
        print("_" * 61)
        if pgMenu == "0":
            exit()
        elif pgMenu == "1":
            criarConta()
        elif pgMenu == "2":
            if login():
                break
        else:
            print('\n\t\033[31mInformação Inválida! \n\tResponda com 1, 2 ou 0\n\033[m')

main()