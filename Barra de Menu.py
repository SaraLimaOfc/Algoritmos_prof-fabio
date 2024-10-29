from tkinter import Tk, Label, Menu, messagebox, Frame, Button

def semComando():
    print("Comando não implementado.")

def sobreProgramador():
    messagebox.showinfo("Dados do Programador", "Nome: Sara Lima Mamedes Souza\nIdade: 23")

def mostrarInformacoes():
    # Limpar a área de exibição antes de mostrar novas informações
    for widget in app.winfo_children():
        widget.destroy()

    frame_info = Frame(app, bg="#dde")
    frame_info.pack(fill="both", expand=True)

    label_programa = Label(frame_info, text="Programa", bg="#dde", font=("Arial", 14))
    label_programa.pack(pady=10)

    button_programador = Button(frame_info, text="Programador", command=sobreProgramador)
    button_programador.pack(pady=10)

    button_sair = Button(frame_info, text="Sair", command=sairComMensagem)
    button_sair.pack(pady=10)

def mostrarRelatorios(relatorio_num):
    if relatorio_num == 1:
        messagebox.showinfo("Relatório", "Conferimos que a profissão da Sara é Técnica de Informática.")
    elif relatorio_num == 2:
        messagebox.showinfo("Relatório", "Conferimos que o nome completo da Sara é Sara Lima Mamedes de Souza.")
    elif relatorio_num == 3:
        messagebox.showinfo("Relatório", "Conferimos que a Sara tem a idade de 23 anos.")

def mostrarBancoDeDados():
    messagebox.showinfo("Banco de Dados", "Aqui você pode gerenciar seu banco de dados.")

def mostrarPrograma():
    messagebox.showinfo("Programa", "Programação é a arte de escrever instruções para que o computador execute.")

def sairComMensagem():
    messagebox.showinfo("Sair", "Valeu, até a próxima!")
    app.quit()

app = Tk()
app.title("Simulado 2")
app.geometry("300x300")
app.configure(background="#dde")

# Criação da barra de menus
barraDeMenus = Menu(app)

# Menu Contatos
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=semComando)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=sairComMensagem)
barraDeMenus.add_cascade(label="Contato", menu=menuContatos)

# Menu Manutenção
menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=mostrarBancoDeDados)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

# Menu Relatórios
menuRelatorios = Menu(barraDeMenus, tearoff=0)
menuRelatorios.add_command(label="Relatório 1", command=lambda: mostrarRelatorios(1))
menuRelatorios.add_command(label="Relatório 2", command=lambda: mostrarRelatorios(2))
menuRelatorios.add_command(label="Relatório 3", command=lambda: mostrarRelatorios(3))
barraDeMenus.add_cascade(label="Relatórios", menu=menuRelatorios)

# Menu Informações
menuInformacoes = Menu(barraDeMenus, tearoff=0)
menuInformacoes.add_command(label="Programa", command=mostrarPrograma)
menuInformacoes.add_command(label="Programador", command=sobreProgramador)
menuInformacoes.add_separator()
menuInformacoes.add_command(label="Sair", command=sairComMensagem)
barraDeMenus.add_cascade(label="Informações", menu=menuInformacoes)

# Adicionar um rótulo abaixo da barra de menu
label_descricao = Label(app, text="Bem-vindo ao Simulador de Programação!\nExplore o menu acima para conhecer mais.", bg="#dde", font=("Arial", 10))
label_descricao.pack(pady=20)

# Configurações finais
app.config(menu=barraDeMenus)

# Label no canto inferior direito (apenas um)
label_rodape = Label(app, text="By: Sara", bg="#dde")
label_rodape.place(relx=1.0, rely=1.0, anchor="se")

app.mainloop()
