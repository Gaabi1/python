from tkinter import * 

def funcClicar():
        print("Botão Precionado")

#Tk(): Cria a janela principal do aplicativo. 
janelaprincipal= Tk()

#Label(): Cria um widget de rótulo (label) que exibe texto ou imagens.
#master=janelaprincipal: Especifica a janela principal (ou contêiner) onde o widget será colocado.
#text="Minha Janela Exibida": Define o texto que será exibido no rótulo.
texto= Label(master= janelaprincipal, text= "Minha Janela Exibida")

#place(): Esse método posiciona o widget dentro da janela de maneira absoluta, com base nas coordenadas fornecidas.
texto.place(x=50, y=100)

#
texto.pack()

#Button(): Cria um botão na interface gráfica.
#master=janelaprincipal: define que o botão será colocado dentro da janela janelaprincipal.
#command=funcClicar: A função command especifica qual função será chamada quando o botão for pressionado.
botao= Button(master= janelaprincipal, text="Clique", command= funcClicar)

#tenta ajustar o widget automaticamente dentro da janela, com base na ordem de adição e o espaço disponível.
botao.pack()

#Esse método inicia o loop principal da interface gráfica. Ele fica rodando indefinidamente, esperando por interações do usuário
janelaprincipal.mainloop()
