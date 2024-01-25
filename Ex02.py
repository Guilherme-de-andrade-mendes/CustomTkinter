import customtkinter as ck 

janela = ck.CTk()

#Configurando a janela principal

janela.title("Aula 2") #Define o título da janela

#Estabele o tamanho da janela principal, levando em consideração largura X altura
janela.geometry("700x400") 

#Delimita o tamanho máximo da janela
janela.maxsize(width=900, height=550) 

#Delimita o tamanho mínimo da janela
janela.minsize(width= 400, height=200) 

#impede que um usuário altere o tamanho da janela em um ou ambos os eixos.
janela.resizable(width=False, height=False) 

# Assim que o programa lê essa função ele fecha a janela atual
janela.iconify()

# Assim que o programa lê essa função ele recupera a janela fechada
janela.deiconify()

janela.mainloop()