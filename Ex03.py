import customtkinter as ctk

janela = ctk.CTk()

#Configurações da janela

janela.title("Aula 3")
janela.geometry("700x350")
janela.resizable(width=False, height=False)

#Customizando tema da aplicação

janela._set_appearance_mode("system")

janela.mainloop()