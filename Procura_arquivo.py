import os
import shutil
from IPython.display import clear_output

def procura_extensao():
    extensao_procura = []
    run = 1
    while(run == 1):
        try:
            op = int(input("(1) Adicionar extensoes a serem procuradas (2) Finalizar "))
            if(op == 1):
                run2 = 1
                while(run2 == 1):
                    print("")
                    print("Digite 'sair' para encerrar a seleção de extensões")
                    procura = str(input("Qual extensão você quer procurar? Ex: .pdf\n"))
                    if procura[0] == ".":
                        extensao_procura.append(procura)
                    elif procura[0] != "." and procura != "sair":
                        print("Adicione o ponto antes da extensão!")
                        print("Ex: .pdf")
                    elif procura.lower() == "sair":
                        run2 = 0
            elif(op == 2):
                print("Fim da seleção de extensões")
                if not extensao_procura:
                    print("Nenhuma extensao a ser procurada")
                    op3 = str(input("Deseja realmente finalizar o programa?? S ou N\n"))
                    if op3.lower() == "s":
                        run = 0
                        print("Programa Encerrado")
                    elif op3.lower() == "n":
                        procura_extensao()
                else:
                    clear_output()
                    print("Extensões a serem procuradas: ", extensao_procura)
                    run = 0
            else:
                print("opção invalida")
        except Exception as e:
            print("Entre com um valor inteiro!")
    return extensao_procura

def copia_arquivos(caminho_procura, extensao_procura):
    
    tst = 1
    
    while(tst == 1):
        
        novo_nome = input("Nome nova pasta: \n")
        caminho_novo = caminho_procura + str("\\") + novo_nome

        try:
            os.mkdir(caminho_novo)
            for root, dirs, files in os.walk(caminho_procura):
                for file in files:
                    for extensao in extensao_procura:
                        if extensao in file:
                            caminho_original = os.path.join(root, file)
                            caminho_novo_arquivo = os.path.join(caminho_novo, file)
                            try:
                                shutil.copy(caminho_original, caminho_novo_arquivo)
                                print(f"Arquivo {file} copiado para a pasta {novo_nome}!")
                            except:
                                pass
            tst = 0

        except FileExistsError as e:
            print(f"Pasta {e} já existe!")
            
    return (novo_nome, caminho_novo)

def zip_file(novo_nome, caminho_procura, caminho_novo):
    shutil.make_archive(caminho_novo, "zip", caminho_procura, novo_nome)
    print("Pasta Compactada!")
    print("Caminho da pasta: ")
    print(caminho_novo)
    
caminho_procura = input("Entre com o caminho da pasta:\n")
extensao_procura = procura_extensao()
cont = 0
cont2 = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        for extensao in extensao_procura:
            if extensao in arquivo:
                try:
                    cont += 1
                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                    tamanho_arquivo = os.path.getsize(caminho_completo)
                    print("")
                    print("Arquivo encontrado: ", caminho_completo)
                    print("Nome do arquivo: ", nome_arquivo)
                    print("Extensão: ", extensao_arquivo)
                    print("Tamanho: ", tamanho_arquivo)
                except PermissionError as e:
                    print("Sem permissão")
                except FileNotFoundError as e:
                    print("Arquivo não encontrado")
                except Exception as e:
                    print("Erro desconhecido: ", e)

print(f"{cont} Arquivo(s) Encontrado(s)")
                                      
while(cont2 == 0):
    op3 =  input("Deseja copiar estes arquivos?\nS / N?")
    if op3.lower() == "s":
        clear_output()
        novo_nome, caminho_novo = copia_arquivos(caminho_procura, extensao_procura)
        op4 = input("Deseja compactar essa pasta?\n S / N?\n")
        if op4.lower() == "s":
            zip_file(novo_nome, caminho_procura, caminho_novo)
        elif op4.lower() == "n":
            print("Programa Encerrado")
            pass
        else:
            pass
        cont2 = 1
    elif op3.lower() == "n":
        cont2 = 1
    else:
        print("Opção invalida!")