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



