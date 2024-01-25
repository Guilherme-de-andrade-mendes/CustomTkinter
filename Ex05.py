import customtkinter as ctk

janela = ctk.CTk()

#Configurações da janela

janela.title("Aula 5")
janela.geometry("900x600")
janela.resizable(width=True, height=True)

#Declarando frames
frame1 = ctk.CTkFrame(master= janela, width=200, height=350, fg_color="lightgray", bg_color="transparent", border_width=5, corner_radius=10, border_color="lightblue").place(x= 10, y= 60)
frame2 = ctk.CTkFrame(janela, width=200, height=350, fg_color="#5665DB", bg_color="transparent", border_width=5, corner_radius=10, border_color="lightblue").place(x=220 ,y=60)
frame3 = ctk.CTkFrame(janela, width=200, height=350, fg_color="#121E4D", bg_color="transparent", border_width=5, corner_radius=10, border_color="lightblue").place(x=430 ,y=60)

janela.mainloop()