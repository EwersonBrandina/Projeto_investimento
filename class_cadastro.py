import mysql.connector
from class_usuario import*
from class_movimentacao import*

class bancoDados:

    def __init__(self, msg = 'Segue a Lista Abaixo:'):
        self.msg = msg
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='investimentos'
        )
        self.meu_cursor = self.conexao.cursor() 

    def cadastros(self, cpf_cnpj, nome, dataNasc, telefone):
        comando_sql = f'select * from Usuarios'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        contador=0
        for i in lista:
            if cpf_cnpj == i[0]:
                contador=1
                print('CPF/CNPJ já Cadastrado')
                break
        if contador == 0:
            obj_cadastros = Usuario(cpf_cnpj, nome, dataNasc, telefone)
            comando_sql = f"insert into Usuarios (cpf_cnpj, nome, dataNasc, telefone) value ('{obj_cadastros.cpf_cnpj}','{obj_cadastros.nome}','{obj_cadastros.dataNasc}','{obj_cadastros.telefone}')"
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit()

    def listar_usuarios(self):
        comando_sql = f'select * from Usuarios'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            self.msg += f'\nCpf/CNPJ: {i[0]}, Nome: {i[1]}, Data Nasc.: {i[2]}, Tel.:{i[3]}'
        print(self.msg)
        self.msg='Segue a Lista Abaixo'