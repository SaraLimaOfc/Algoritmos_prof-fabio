import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # Importando o DateEntry para o calendário
from datetime import datetime

class App:
    def __init__(self, master):
        self.master = master
        master.title("Tela de Login")

        # Dicionário de usuários com Sara Lima e senha 2468
        self.usuarios = {
            "Sara Lima": "2468"
        }

        # Widgets da tela de login
        self.label_nome = tk.Label(master, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(master)
        self.entry_nome.pack()

        self.label_senha = tk.Label(master, text="Senha:")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(master, show="*")
        self.entry_senha.pack()

        self.button_entrar = tk.Button(master, text="Entrar", command=self.entrar)
        self.button_entrar.pack(pady=5)

        self.button_sair = tk.Button(master, text="Sair", command=self.sair)
        self.button_sair.pack(pady=5)

    def sair(self):
        messagebox.showinfo("Saindo", "Até a próxima!")
        self.master.quit()

    def entrar(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()
        if nome in self.usuarios and self.usuarios[nome] == senha:
            self.tela_cadastro()  # Abre a tela de cadastro
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    def tela_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self.master)
        self.janela_cadastro.title("Cadastro")

        # Cabeçalho
        self.label_cadastro = tk.Label(self.janela_cadastro, text="Cadastro", font=("Arial", 16))
        self.label_cadastro.pack(pady=10)

        # Nome
        self.label_nome_cadastro = tk.Label(self.janela_cadastro, text="Nome:")
        self.label_nome_cadastro.pack()
        self.entry_nome_cadastro = tk.Entry(self.janela_cadastro)
        self.entry_nome_cadastro.pack()

        # Sexo
        self.label_sexo = tk.Label(self.janela_cadastro, text="Sexo:")
        self.label_sexo.pack()
        self.var_sexo = tk.StringVar(value="M")  # Padrão: Masculino
        self.radio_masculino = tk.Radiobutton(self.janela_cadastro, text="Masculino", variable=self.var_sexo, value="M")
        self.radio_feminino = tk.Radiobutton(self.janela_cadastro, text="Feminino", variable=self.var_sexo, value="F")
        self.radio_outro = tk.Radiobutton(self.janela_cadastro, text="Outro", variable=self.var_sexo, value="O")
        self.radio_masculino.pack(pady=2)
        self.radio_feminino.pack(pady=2)
        self.radio_outro.pack(pady=2)

        # Data de Nascimento com calendário
        self.label_data_nasc = tk.Label(self.janela_cadastro, text="Data de Nascimento:")
        self.label_data_nasc.pack()
        self.entry_data_nasc = DateEntry(self.janela_cadastro, date_pattern='dd/mm/yyyy')
        self.entry_data_nasc.pack()

        # Profissão
        self.label_profissao = tk.Label(self.janela_cadastro, text="Profissão:")
        self.label_profissao.pack()
        self.profissoes = ["Professor", "Técnico de Informática", "Padeiro", "Mecânico"]
        self.combo_profissao = ttk.Combobox(self.janela_cadastro, values=self.profissoes)
        self.combo_profissao.pack()

        # Observação
        self.label_observacao = tk.Label(self.janela_cadastro, text="Observação:")
        self.label_observacao.pack(pady=5)
        self.entry_observacao = tk.Entry(self.janela_cadastro)
        self.entry_observacao.insert(0, "No céu tem pão")  # Insere a mensagem padrão
        self.entry_observacao.pack()

        # Botões
        self.button_voltar = tk.Button(self.janela_cadastro, text="Voltar", command=self.janela_cadastro.destroy)
        self.button_voltar.pack(pady=5)
        self.button_gravar = tk.Button(self.janela_cadastro, text="Gravar", command=self.gravar_usuario)
        self.button_gravar.pack(pady=5)

    def gravar_usuario(self):
        nome = self.entry_nome_cadastro.get()
        sexo = self.var_sexo.get()
        data_nasc = self.entry_data_nasc.get()
        profissao = self.combo_profissao.get()

        if nome and sexo and data_nasc and profissao:
            idade = self.calcular_idade(data_nasc)
            self.tela_informacoes(nome, sexo, idade, profissao)
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

    def tela_informacoes(self, nome, sexo, idade, profissao):
        self.janela_info = tk.Toplevel(self.master)
        self.janela_info.title("Informações do Usuário")

        # Informações do usuário
        tk.Label(self.janela_info, text=f"Nome: {nome}").pack()
        tk.Label(self.janela_info, text=f"Sexo: {sexo}").pack()
        tk.Label(self.janela_info, text=f"Idade: {idade} anos").pack()
        tk.Label(self.janela_info, text=f"Profissão: {profissao}").pack()

        # Botão Voltar
        self.button_voltar_info = tk.Button(self.janela_info, text="Voltar", command=self.janela_info.destroy)
        self.button_voltar_info.pack(pady=5)

    def calcular_idade(self, data_nasc):
        try:
            data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
            idade = datetime.now().year - data_nasc.year - ((datetime.now().month, datetime.now().day) < (data_nasc.month, data_nasc.day))
            return idade
        except ValueError:
            return "Data inválida"

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
