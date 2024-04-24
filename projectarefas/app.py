
#Logica
class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa): 
        self.tarefas.append({'tarefa': tarefa, 'concluida': False}) 

    def visualizar_tarefas(self): 
        print("\n") 
        print("Lista de tarefas: ")
        if self.tarefas:    
            for i, tarefa in enumerate(self.tarefas , 1):
                status = 'Concluida' if tarefa['concluida'] else 'Não Concluida'  
                print(f"{i}.[{status}] {tarefa['tarefa']}")
                print("\n")
        else:
            print("Lista de tarefas vazia")
    
    def marcar_como_concluida(self , entrada):
        if entrada.isdigit():
            indice = int(entrada)
            if 1 <= indice <= len(self.tarefas):
                if not self.tarefas[indice -1]['concluida']:
                    self.tarefas[indice -1]['concluida'] = True
                    print("Tarefa marcada como concluida")
                else:
                    print("Está tarefa já está marcada como concluida.")
            else:
                print("Indice de tarefa invalido")
        else:
            tarefa_encontrada = False
            for i , tarefa in enumerate (self.tarefas , 1):
                if tarefa['tarefa'] == entrada:
                    tarefa_encontrada = True
                    if not tarefa['concluida']:
                        self.tarefas[i -1]['concluida'] = True
                        print("Tarefa marcada como concluida.") 
                    else:
                        print("Esta tarefa ja está marcada como concluida")
                
            if not tarefa_encontrada:
                print("Tarefa não encontrada.")        
    

    def excluir_tarefa(self, indice):
        if 1 <= indice <= len(self.tarefas):
            del self.tarefas[indice - 1]
            print("Tarefa excluída.")
        else:
            print("Índice de tarefa inválido.")

#Execuçao
def menu():
    lista_tarefas = ListaDeTarefas()
    while True:
        print("=======Lista de Tarefas========")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Excluir uma tarefa")
        print("5. Sair")
        print("...                ...")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa que quer ser adicionada: ")
            print("\n")
            lista_tarefas.adicionar_tarefa(tarefa)
        elif opcao == '2':
            lista_tarefas.visualizar_tarefas()
        elif opcao == '3':
            print("\n")
            entrada = str(input("Digite o numero ou nome da tarefa ser marcada como concluída: "))
            if entrada.isdigit():
                entrada = int(entrada)    
            lista_tarefas.marcar_como_concluida(str(entrada))
        elif opcao == '4':
            indice = int(input("Digite o índice da tarefa a ser excluída: "))
            lista_tarefas.excluir_tarefa(indice)
        elif opcao == '5':
            print("Saindo do aplicativo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



menu()
