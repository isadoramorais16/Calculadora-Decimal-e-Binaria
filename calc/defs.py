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

window.mainloop()

import tkinter as tk
from tkinter import ttk


# Funções de conversão
def converter():
    try:
        if combo.get() == "Decimal para Binário":
            numero = int(entrada.get())
            resultado["text"] = bin(numero)[2:]  # Remove o '0b'
        elif combo.get() == "Binário para Decimal":
            numero = int(entrada.get(), 2)
            resultado["text"] = str(numero)
        else:
            resultado["text"] = "Selecione uma opção"
    except:
        resultado["text"] = "Entrada inválida"


def limpar():
    entrada.delete(0, tk.END)
    resultado["text"] = ""


# Janela principal
janela = tk.Tk()
janela.title("Conversor Decimal ↔ Binário")
janela.geometry("400x250")
janela.resizable(False, False)

# -------------------------------
# 🔷 Frame Superior (Título)
frame_topo = tk.Frame(janela, bg="lightblue", height=60)
frame_topo.pack(fill="x")

titulo = tk.Label(frame_topo, text="Conversor Decimal ↔ Binário", bg="lightblue", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# -------------------------------
# 🔷 Frame do Meio (Formulário)
frame_meio = tk.Frame(janela, padx=10, pady=10)
frame_meio.pack(fill="x")

# Label + Entry
tk.Label(frame_meio, text="Digite o número:").grid(row=0, column=0, sticky="w", pady=5)
entrada = tk.Entry(frame_meio, width=25)
entrada.grid(row=0, column=1, pady=5)

# Combobox
tk.Label(frame_meio, text="Conversão:").grid(row=1, column=0, sticky="w", pady=5)
combo = ttk.Combobox(frame_meio, values=["Decimal para Binário", "Binário para Decimal"], state="readonly", width=22)
combo.grid(row=1, column=1, pady=5)
combo.current(0)

# -------------------------------
# 🔷 Frame Inferior (Botões e Resultado)
frame_baixo = tk.Frame(janela, pady=10)
frame_baixo.pack()

# Botões
btn_converter = tk.Button(frame_baixo, text="Converter", command=converter, width=12, bg="lightgreen")
btn_converter.grid(row=0, column=0, padx=5, pady=5)

btn_limpar = tk.Button(frame_baixo, text="Limpar", command=limpar, width=12, bg="tomato")
btn_limpar.grid(row=0, column=1, padx=5, pady=5)

# Resultado
tk.Label(frame_baixo, text="Resultado:").grid(row=1, column=0, sticky="w", pady=5)
resultado = tk.Label(frame_baixo, text="", font=("Arial", 14, "bold"), fg="blue")
resultado.grid(row=1, column=1, sticky="w", pady=5)

# -------------------------------
janela.mainloop()



