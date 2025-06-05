from tkinter import Tk, PhotoImage, Label, Button, Entry,Text,RAISED

#configuração do formato e título do programa
window = Tk()
window.geometry("600x600")
window.title("Decimal Binary Caculator")
window.resizable(False, False)

# configuração da logo do programa
icon = PhotoImage(file='C:\\Users\\jvbmo\\Downloads\\testes\\calc\\calculadora.png')
window.iconphoto(True,icon)
window.config(background="#428af5")


label = Label(window,text="Welcome to Decimal Binary Calculator!",
font=('Rubik',22,'bold'),fg='#3b11ba',
bg='#428af5',
bd=10,
pady=5,)
label.place()
label.pack()

button=Button(window,text="Binary to Decimal",
font=('Rubik',15,'bold'),fg='#139bd1',
bg='#3b11ba',relief=RAISED,
bd=10,activebackground='#3b11ba',
padx=20,
pady=2,)
button.place(x=180,y=200)
button.pack()

entry= Entry(window,font=("Arial",30))
entry.pack(padx=90,pady=90)

import tkinter as tk
from tkinter import ttk, messagebox


def converter():
    opcao = opcao_var.get()
    entrada = entrada_numero.get()

    if opcao == "Decimal para Binário":
        try:
            numero_decimal = int(entrada)
            numero_binario = bin(numero_decimal)[2:]  # Remove o '0b'
            resultado_var.set(numero_binario)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número decimal inteiro válido.")

    elif opcao == "Binário para Decimal":
        try:
            # Verifica se o binário é válido (apenas 0 e 1)
            if not set(entrada).issubset({'0', '1'}):
                raise ValueError

            numero_decimal = int(entrada, 2)
            resultado_var.set(str(numero_decimal))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número binário válido (apenas 0 e 1).")


# Criação da janela principal
janela = tk.Tk()
janela.title("Conversor Decimal ↔ Binário")
janela.geometry("400x250")
janela.resizable(False, False)

# Label título
tk.Label(janela, text="Conversor Decimal ↔ Binário", font=("Arial", 14, "bold")).pack(pady=10)

# Menu de seleção da conversão
opcao_var = tk.StringVar(value="Decimal para Binário")
opcoes = ["Decimal para Binário", "Binário para Decimal"]

tk.Label(janela, text="Escolha a conversão:", font=("Arial", 12)).pack()
menu_opcoes = ttk.Combobox(janela, textvariable=opcao_var, values=opcoes, state="readonly", font=("Arial", 12))
menu_opcoes.pack(pady=5)

# Entrada de número
tk.Label(janela, text="Digite o número:", font=("Arial", 12)).pack()
entrada_numero = tk.Entry(janela, font=("Arial", 12), justify="center")
entrada_numero.pack(pady=5)

# Botão de conversão
botao_converter = tk.Button(
    janela, text="Converter", font=("Arial", 12), command=converter
)
botao_converter.pack(pady=10)

# Resultado da conversão
resultado_var = tk.StringVar()
tk.Label(janela, text="Resultado:", font=("Arial", 12)).pack(pady=5)
resultado_label = tk.Label(
    janela, textvariable=resultado_var, font=("Arial", 14, "bold"), fg="blue"
)
resultado_label.pack()

# Executar a janela
janela.mainloop()


window.mainloop()
