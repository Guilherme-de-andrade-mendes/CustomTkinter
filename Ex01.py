import customtkinter as custk

janela = custk.CTk() #Criar a janela principal utilizando o customtkinter

button = custk.CTkButton(janela, text="Olá") # Criando um botão
button.pack() #Faz com que o botão apareça dentro da janela

janela.mainloop()