import customtkinter as ctk

janela = ctk.CTk()

janela.title("Aula 6")
janela.geometry("700x400")
janela.resizable(width=False, height=False)

#Criando Abas

tabview = ctk.CTkTabview(master=janela, width=400, corner_radius=20, fg_color="white", border_color="blue", border_width=5, segmented_button_fg_color="blue", segmented_button_selected_color="darkblue", segmented_button_unselected_color="lightblue")
tabview.pack()

itens = ["Nomes","Idades","Gênero"]
for x in (itens):
    tabview.add(x)
    tabview.tab(x).grid_rowconfigure(0, weight=1)

#Adicionando elementos na Aba
    
text1 = ctk.CTkLabel(tabview.tab(itens[0]), text="Guilherme Mendes.\nAna lívia Motta.\nLucas Lima Mendes.").pack()
text2 = ctk.CTkLabel(tabview.tab(itens[1]), text="20 anos.\n21 anos.\n19 anos.").pack()
text3 = ctk.CTkLabel(tabview.tab(itens[2]), text="Masculino.\nFeminino.\nMasculino.").pack()


janela.mainloop()