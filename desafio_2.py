import textwrap
def menu():

    menu = """\n
    =================== MENU ================
    [d]\t Depositar 
    [s]\t Sacar
    [e]\t Extrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\t Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
        if valor >0:
            saldo +=valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("\n== Deposito realizado com sucesso!")
        else:
            print("Operação falhou! O Valor informado é invalido.")
        return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
      
        excedeu_saldo = valor >saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >=limite_saques
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Numero maximo de saques excedido")
        elif valor>0:
            saldo -= valor
            extrato +=f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n == Saque realizado com sucesso! ==")
        else:
            print("Operação falhou! O valor informafo é inválido.")
        return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
     print("\n================= EXTRATO ===============")
     print("Não foram relizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("===========================================")
def criar_usuario(usuarios):
     cpf = input("Informe o CPF (somente número):")
     usuario = filtrar_usuario(cpf, usuarios)
     if usuario:
          print ("\n @@@ Já existe usuario com esse CPF! @@@")
          return
     nome = input("Informe o nome completo:")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaa):")
     endereco= input ("Informe o endereço (logradouro, nro - bairro - cidade):")

     usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf,"endereco":endereco})
     print("== Usuário criado com sucesso!==")
     
def filtrar_usuario(cpf,usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia,numero_conta,usuarios):
     cpf= input("Informe o CPF do usuário:")
     usuario = filtrar_usuario(cpf,usuarios)
     if usuario:
          print("\== Conta criada com sucesso! ===")
          return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
def listar_contas(contas):
    for conta in contas:
        linha=f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def sair(q):
        print ("Operação invalida, por favor selecione novamente a operação desejada")

   
    

       
   
def main():
    AGENCIA= "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques=0
    
    usuarios=[]
    contas =[]
    numero_conta = 1
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do deposito"))
            saldo, extrato = depositar(saldo,valor,extrato)
        elif opcao =="s":
            valor =float(input("Informe o valor do saque:"))

            saldo,extrato =sacar(
             saldo=saldo,
             valor=valor,
             extrato=extrato,
             limite=limite,
             numero_saques=numero_saques,
             limite_saques=LIMITE_SAQUES,
            )
    
        elif opcao == "e":
         exibir_extrato(saldo,extrato=extrato)
    
        elif opcao == "nu":
         criar_usuario(usuarios)
         
    
        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
                numero_conta +=1
        elif opcao =="lc":
            listar_contas(contas) 
        elif opcao =="q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação")
    

main()