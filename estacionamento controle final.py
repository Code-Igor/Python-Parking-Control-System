import numpy as np
import random
import string

# Inicialização das seções e vagas
vagas_a = np.array([1, 2, 3, 4, 5])
vagas_b = np.array([1, 2, 3, 4, 5])
vagas_c = np.array([1, 2, 3, 4, 5])
secao = [vagas_a, vagas_b, vagas_c]


#ocupadas

vaga_a_ocup = np.array([])
vaga_b_ocup = np.array([])
vaga_c_ocup = np.array([])

# Dicionário para armazenar os veículos estacionados
registro = {}


########################################################################################################################################

#gera uma palca aleatória, será usada e resgatda nas seções posteriores
def gerar_placa():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    return f"{letras}{numeros}"


#####################################################################################################################################

def ocupar_vaga():
    global vagas_a
    global vagas_b
    global vagas_c

    global vaga_a_ocup
    global vaga_b_ocup
    global vaga_c_ocup

    

    # Escolha diretamente das arrays
    escolha_secao = random.choice([vagas_a, vagas_b, vagas_c])

    if np.array_equal(escolha_secao, vagas_a):

        if vagas_a.size == 0:
            print("Nenhuma vaga disponível na Seção A.")
            return None

        escolha_vaga = random.choice(vagas_a.tolist())
        placa = gerar_placa()
        registro[placa] = ('A', escolha_vaga)
        vaga_a_ocup = np.append(escolha_vaga, vaga_a_ocup)
        print("")

        print(
            f"A vaga de número {escolha_vaga} da Seção A foi ocupada pelo veículo {placa}.")
        

        vagas_a = vagas_a[vagas_a != escolha_vaga]
        return placa

    elif np.array_equal(escolha_secao, vagas_b):

        if vagas_b.size == 0:
            print("Nenhuma vaga disponível na Seção B.")
            return None

        escolha_vaga = random.choice(vagas_b.tolist())
        placa = gerar_placa()
        registro[placa] = ('B', escolha_vaga)
        vaga_b_ocup = np.append(escolha_vaga, vaga_b_ocup)
        
        print("")
        print(
            f"A vaga de número {escolha_vaga} da Seção B foi ocupada pelo veículo {placa}.")
    

        vagas_b = vagas_b[vagas_b != escolha_vaga]
        return placa

    elif np.array_equal(escolha_secao, vagas_c):

        if vagas_c.size == 0:
            print("Nenhuma vaga disponível na Seção C.")
            return None

        escolha_vaga = random.choice(vagas_c.tolist())
        placa = gerar_placa()
        registro[placa] = ('C', escolha_vaga)
        vaga_c_ocup = np.append(escolha_vaga, vaga_c_ocup)
        print("")

        print(
            f"A vaga de número {escolha_vaga} da Seção C foi ocupada pelo veículo {placa}.")
        
        vagas_c = vagas_c[vagas_c != escolha_vaga]
        return placa

    print("Nenhuma seção encontrada.")
    return None



########################################################################################################################
def liberar_vaga():

    global vaga_a_ocup
    global vaga_b_ocup
    global vaga_c_ocup

    global vagas_a
    global vagas_b
    global vagas_c
   

    esecao = input("Escolha qual seção você quer liberar a vaga (A,B,C) ")
    if "A" in esecao:
        
        evaga = int(input("Escolha umas das 5 vagas "))
        if np.isin(evaga, vaga_a_ocup):

            print("A vaga foi liberada!")
            vaga_a_ocup = vaga_a_ocup[vaga_a_ocup != evaga]
            vagas_a = np.append(evaga, vagas_a)
        else:
            print("Esta vaga está livre.")

    if "B" in esecao:
        
        evaga = int(input("Escolha umas das 5 vagas "))
        if np.isin(evaga, vaga_b_ocup):

            print("A vaga foi liberada!")
            vaga_b_ocup = vaga_b_ocup[vaga_b_ocup != evaga]
            vagas_b = np.append(evaga, vagas_b)
        else:
            print("Esta vaga está livre.")

    if "C" in esecao:
        
        evaga = int(input("Escolha umas das 5 vagas "))
        if np.isin(evaga, vaga_c_ocup):

            print("A vaga foi liberada!")
            vaga_c_ocup = vaga_c_ocup[vaga_c_ocup != evaga]
            vagas_c = np.append(evaga, vagas_c)
        else:
            print("Esta vaga está livre. Escolha outra.")




########################################################################################################################

def exibir_vaga():
    exibir = input("Deseja exibir as vagas disponíveis no estacionamento? ")
    if exibir.lower() == 'sim':
        print("")
        print("As vagas disponíveis da Seção A são:", vagas_a)
        print("")
        print("As vagas disponíveis da Seção B são:", vagas_b)
        print("")
        print("As vagas disponíveis da Seção C são:", vagas_c)
    elif exibir.lower() == 'não':
        print("Ok então.")
    else:
        print("Não entendi nada, tmj.")


############################################################################################################################################


# consulta o veículo pela palca ou pela vaga a qual o veículo ocupa

def consultar_veiculo():
    consulta = input("Você deseja consultar por placa ou por número da vaga? (digite 'placa' ou 'vaga') ").strip().lower()

    if consulta == 'placa':
        placa = input("Digite a placa do veículo: ").strip().upper()
        if placa in registro:
            secao, vaga = registro[placa]
            print(f"O veículo {placa} está estacionado na Seção {secao}, vaga {vaga}.")
        else:
            print("Veículo não foi encontrado.")

#peguei ajuda do chat para fazer essa parte funcionar
#p = palca, s = seção, v = vaga
    elif consulta == 'vaga':
        secao = input("Digite a seção (A, B ou C): ").strip().upper()
        vaga = int(input("Digite o número da vaga: "))
        
        if secao == 'A' and vaga in vaga_a_ocup:
            placa = [p for p, (s, v) in registro.items() if s == 'A' and v == vaga]
            print(f"A vaga {vaga} da Seção A está ocupada pelo veículo: {placa[0]}." if placa else "Vaga não encontrada.")
        
        elif secao == 'B' and vaga in vaga_b_ocup:
            placa = [p for p, (s, v) in registro.items() if s == 'B' and v == vaga]
            print(f"A vaga {vaga} da Seção B está ocupada pelo veículo: {placa[0]}." if placa else "Vaga não encontrada.")
        
        elif secao == 'C' and vaga in vaga_c_ocup:
            placa = [p for p, (s, v) in registro.items() if s == 'C' and v == vaga]
            print(f"A vaga {vaga} da Seção C está ocupada pelo veículo: {placa[0]}." if placa else "Vaga não encontrada.")
        
        else:
            print("Esta vaga está livre ou a seção está incorreta.")

    else:
        print("Opção inválida. Tente novamente.")




for _ in range(5):
    ocupar_vaga()
    print(registro)

print()
exibir_vaga()
print()

liberar_vaga()
print()

consultar_veiculo()
print()
exibir_vaga()






