import customtkinter as ctk

janela = ctk.CTk()

#Configurações da janela

janela.title("Aula 4")
janela.geometry("700x350")
janela.resizable(width=False, height=False)

#Customizando tema da aplicação

janela._set_appearance_mode("system")

#Criando nova janela

def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="lightseagreen")
    nova_janela.geometry("350x250")

btn_nova_tela = ctk.CTkButton(master=janela, text="Abrir nova janela", command=nova_tela).place(x=300, y=100)


janela.mainloop()