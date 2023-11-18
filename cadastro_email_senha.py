while True:
    cadastro = int(input(""""
ESCOLHA UMA OPÇÃO:
1 - CRIAR UMA CONTA:
2 - FAZER LOGIN:
"""))
    match cadastro:
        case 1:
            email_cadastrado = input("Digite um email:")
            senha_cadastrado = input("Digite uma senha:")
          
            cadastro1 = [email_cadastrado,senha_cadastrado]

            input("Paciente cadastado com sucesso, precione enter para continuar:")
            print("\n" * 50)
        case 2:
                email_digitado = input("Digite um email:")
                senha_digitado = input("Digite uma senha:")
                if email_cadastrado == email_digitado and senha_cadastrado == senha_digitado:
                    print("login realizado com sucesso!!!")
                    break
                else:
                    print('Email ou Senha errado, Tente novamnte!!!')