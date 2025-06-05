import tkinter as tk
from tkinter import ttk, PhotoImage

# Funções de conversão
def converter():
    try:
        if combo.get() == "Decimal para Binário":
            numero = int(entrada.get())
            resultado["text"] = bin(numero)[2:]  
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
janela.title("Decimal Binary Conversor")
janela.geometry("600x400")
janela.resizable(False, False)
janela.configure(background="#428af5")

#logo do programa
icon = PhotoImage(file='C:\\Users\\jvbmo\\Downloads\\calc-Photoroom.png')
janela.iconphoto(True,icon)


#Frame do Título
frame_topo = tk.Frame(janela, bg="#428af5",height=60)
frame_topo.pack(fill="x")

titulo = tk.Label(frame_topo, text="Conversor Decimal e Binário", bg="#428af5",font=("Rubik", 16, "bold"),
fg="#cf3ca5")
titulo.pack(pady=10)

frame_meio = tk.Frame(janela, padx=10, pady=10, bg="#428af5")
frame_meio.pack(fill="x")

# Label e Entry para digitação do número desejado
tk.Label(frame_meio, text="Digite o número:",font=("Rubik",12,'bold'),
bg="#428af5",fg="#cf3ca5"
).grid(row=0, column=0, sticky="w", pady=9)
entrada = tk.Entry(frame_meio, width=20)
entrada.grid(row=0, column=1, pady=9)

# Combobox para conversão desejada
tk.Label(frame_meio, text="Conversão:", font=("Rubik",12,'bold'),bg="#428af5"
,fg="#cf3ca5").grid(row=1, column=0, sticky="w", pady=5)
combo = ttk.Combobox(frame_meio, values=["Decimal para Binário", "Binário para Decimal"], state="readonly", width=22)
combo.grid(row=1, column=1, pady=5)
combo.current(0)

#Frame Inferior (Botões e Resultado)
frame_baixo = tk.Frame(janela, pady=10,bg="#428af5")
frame_baixo.pack()

# Botões
btn_converter = tk.Button(frame_baixo, text="Converter",font=("Rubik",10,'bold'),fg="black", command=converter, width=12, bg="lightgreen")
btn_converter.grid(row=0, column=0, padx=5, pady=5)

btn_limpar = tk.Button(frame_baixo, text="Limpar",font=("Rubik",10,'bold'),fg="black",bg="tomato",command=limpar, width=12)
btn_limpar.grid(row=0, column=1, padx=5, pady=5)

# Resultado
tk.Label(frame_baixo, text="Resultado:",bg="#428af5",font=("Rubik",15,'bold'),fg="#cf3ca5"
).grid(row=1, column=0, sticky="w", pady=9)
resultado = tk.Label(frame_baixo, text="", font=("Rubik",15,'bold'), fg="#ed4cbd",bg="#428af5")
resultado.grid(row=1, column=1, sticky="w", pady=9)

# janela para execução do programa
janela.mainloop()
