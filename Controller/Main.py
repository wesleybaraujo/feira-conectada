import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from datetime import time
from Model.Fornecedor import Fornecedor
from Model.Feira import Feira
from Model.Programacao import Programacao
from Controller.FornecedorController import FornecedorController
from Controller.FeiraController import FeiraController

class Main:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.fornecedor_controller = FornecedorController()
        self.feira_controller = FeiraController()
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                
                fornecedores_data = data.get('fornecedores', [])
                for f_data in fornecedores_data:
                    self.fornecedor_controller.create_fornecedor(**f_data)

                feiras_data = data.get('feiras', [])
                for f_data in feiras_data:
                    programacoes = []
                    for p_data in f_data.get('programacoes', []):
                        p_data['hora_inicio'] = time.fromisoformat(p_data['hora_inicio'])
                        p_data['hora_fim'] = time.fromisoformat(p_data['hora_fim'])
                        programacoes.append(Programacao(**p_data))
                    
                    fornecedores_feira = []
                    for cod_fornecedor in f_data.get('fornecedores', []):
                        fornecedor = self.fornecedor_controller.get_fornecedor(cod_fornecedor)
                        if fornecedor:
                            fornecedores_feira.append(fornecedor)

                    feira = Feira(
                        cod_feira=f_data['cod_feira'],
                        nome_feira=f_data['nome_feira'],
                        programacoes=programacoes,
                        fornecedores=fornecedores_feira
                    )
                    self.feira_controller.feiras.append(feira)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_data(self):
        data = {
            'fornecedores': [f.to_dict() for f in self.fornecedor_controller.get_all_fornecedores()],
            'feiras': [f.to_dict() for f in self.feira_controller.get_all_feiras()]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def create_feira(self, cod_feira, nome_feira):
        feira = self.feira_controller.create_feira(cod_feira, nome_feira)
        self.save_data()
        return feira

    def get_feira(self, cod_feira):
        return self.feira_controller.get_feira(cod_feira)

    def update_feira(self, cod_feira, nome_feira):
        feira = self.feira_controller.update_feira(cod_feira, nome_feira)
        self.save_data()
        return feira

    def delete_feira(self, cod_feira):
        result = self.feira_controller.delete_feira(cod_feira)
        self.save_data()
        return result

    def get_all_feiras(self):
        return self.feira_controller.get_all_feiras()

    def create_fornecedor(self, cod_fornecedor, razao_social, nome_resp, num_doc):
        fornecedor = self.fornecedor_controller.create_fornecedor(cod_fornecedor, razao_social, nome_resp, num_doc)
        self.save_data()
        return fornecedor

    def get_fornecedor(self, cod_fornecedor):
        return self.fornecedor_controller.get_fornecedor(cod_fornecedor)

    def update_fornecedor(self, cod_fornecedor, razao_social, nome_resp, num_doc):
        fornecedor = self.fornecedor_controller.update_fornecedor(cod_fornecedor, razao_social, nome_resp, num_doc)
        self.save_data()
        return fornecedor

    def delete_fornecedor(self, cod_fornecedor):
        result = self.fornecedor_controller.delete_fornecedor(cod_fornecedor)
        self.save_data()
        return result

    def get_all_fornecedores(self):
        return self.fornecedor_controller.get_all_fornecedores()

    def adicionar_fornecedor_a_feira(self, cod_feira, cod_fornecedor):
        fornecedor = self.fornecedor_controller.get_fornecedor(cod_fornecedor)
        if fornecedor:
            result = self.feira_controller.adicionar_fornecedor_a_feira(cod_feira, fornecedor)
            self.save_data()
            return result
        return False

    def remover_fornecedor_da_feira(self, cod_feira, cod_fornecedor):
        fornecedor = self.fornecedor_controller.get_fornecedor(cod_fornecedor)
        if fornecedor:
            result = self.feira_controller.remover_fornecedor_da_feira(cod_feira, fornecedor)
            self.save_data()
            return result
        return False

    def adicionar_programacao_a_feira(self, cod_feira, cod_programacao, dia, hora_inicio, hora_fim):
        programacao = Programacao(cod_programacao, dia, hora_inicio, hora_fim)
        result = self.feira_controller.adicionar_programacao_a_feira(cod_feira, programacao)
        self.save_data()
        return result
        
    def remover_programacao_da_feira(self, cod_feira, cod_programacao):
        feira = self.get_feira(cod_feira)
        if feira:
            for prog in feira.programacoes:
                if prog.cod_programacao == cod_programacao:
                    result = self.feira_controller.remover_programacao_da_feira(cod_feira, prog)
                    self.save_data()
                    return result
        return False

    def run(self):
        while True:
            print("\n--- Menu ---")
            print("1. Gerenciar Fornecedores")
            print("2. Gerenciar Feiras")
            print("0. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.menu_fornecedores()
            elif choice == '2':
                self.menu_feiras()
            elif choice == '0':
                break
            else:
                print("Opção inválida!")

    def menu_fornecedores(self):
        while True:
            print("\n--- Fornecedores ---")
            print("1. Adicionar Fornecedor")
            print("2. Listar Fornecedores")
            print("3. Atualizar Fornecedor")
            print("4. Deletar Fornecedor")
            print("0. Voltar")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                cod = int(input("Código: "))
                razao = input("Razão Social: ")
                nome = input("Nome do Responsável: ")
                doc = input("Documento: ")
                self.create_fornecedor(cod, razao, nome, doc)
                print("Fornecedor adicionado!")
            elif choice == '2':
                for f in self.get_all_fornecedores():
                    print(f"Cód: {f.cod_fornecedor}, Razão Social: {f.razao_social}")
            elif choice == '3':
                cod = int(input("Código do fornecedor a ser atualizado: "))
                razao = input("Nova Razão Social: ")
                nome = input("Novo Nome do Responsável: ")
                doc = input("Novo Documento: ")
                if self.update_fornecedor(cod, razao, nome, doc):
                    print("Fornecedor atualizado!")
                else:
                    print("Fornecedor não encontrado.")
            elif choice == '4':
                cod = int(input("Código do fornecedor a ser deletado: "))
                if self.delete_fornecedor(cod):
                    print("Fornecedor deletado!")
                else:
                    print("Fornecedor não encontrado.")
            elif choice == '0':
                break
            else:
                print("Opção inválida!")

    def menu_feiras(self):
        while True:
            print("\n--- Feiras ---")
            print("1. Adicionar Feira")
            print("2. Listar Feiras")
            print("3. Atualizar Feira")
            print("4. Deletar Feira")
            print("5. Adicionar Fornecedor à Feira")
            print("6. Adicionar Programação à Feira")
            print("0. Voltar")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                cod = int(input("Código: "))
                nome = input("Nome da Feira: ")
                self.create_feira(cod, nome)
                print("Feira adicionada!")
            elif choice == '2':
                for f in self.get_all_feiras():
                    print(f"Cód: {f.cod_feira}, Nome: {f.nome_feira}")
            elif choice == '3':
                cod = int(input("Código da feira a ser atualizada: "))
                nome = input("Novo Nome: ")
                if self.update_feira(cod, nome):
                    print("Feira atualizada!")
                else:
                    print("Feira não encontrada.")
            elif choice == '4':
                cod = int(input("Código da feira a ser deletada: "))
                if self.delete_feira(cod):
                    print("Feira deletada!")
                else:
                    print("Feira não encontrada.")
            elif choice == '5':
                cod_feira = int(input("Código da Feira: "))
                cod_fornecedor = int(input("Código do Fornecedor: "))
                if self.adicionar_fornecedor_a_feira(cod_feira, cod_fornecedor):
                    print("Fornecedor adicionado à feira!")
                else:
                    print("Feira ou fornecedor não encontrado.")
            elif choice == '6':
                cod_feira = int(input("Código da Feira: "))
                cod_prog = int(input("Código da Programação: "))
                dia = input("Dia: ")
                h_inicio = time.fromisoformat(input("Hora Início (HH:MM:SS): "))
                h_fim = time.fromisoformat(input("Hora Fim (HH:MM:SS): "))
                self.adicionar_programacao_a_feira(cod_feira, cod_prog, dia, h_inicio, h_fim)
                print("Programação adicionada à feira!")
            elif choice == '0':
                break
            else:
                print("Opção inválida!")

if __name__ == '__main__':
    main = Main()
    main.run()
