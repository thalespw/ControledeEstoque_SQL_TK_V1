from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

######## funcionalidades do sistema #############
import sqlite3
import time

conn = sqlite3.connect('Estoque.db')
cursor = conn.cursor()




def limpar_tela():
    lote_insumo.delete(0,END)
    data_insumo.delete(0,END)
    qtde_insumo.delete(0,END)
    nome_insumo.delete(0,END)

def carregar_ultimo():
    limpar_tela()
    cursor.execute("SELECT Produto, Quantidade, DataValidade, Lote FROM Estoque ORDER BY id DESC LIMIT 1")
    ultimo = cursor.fetchone()

    if ultimo:
        nome_insumo.insert(0, ultimo[0])
        lote_insumo.insert(0, ultimo[3])
        qtde_insumo.insert(0, str(ultimo[1]))
        data_insumo.set_date(ultimo[2])

def adicionar_insumo():
    limpar_tela()
    b4.config(state="normal")
    
    
def deletar_insumo():
    print("deletar_insumo")
    if len(nome_insumo.get()) < 2:
        messagebox.showerror("ERRO","Produto Inválido")
        nome_insumo.delete(0,END)
        return
    
    cursor.execute(f"""
    DELETE FROM Estoque
    WHERE Produto = "{nome_insumo.get()}"
    """)
    conn.commit()
    messagebox.showinfo("EXCLUSÃO",f"{nome_insumo.get()} excluído com sucesso!")
    nome_insumo.delete(0,END)
    
def consumir_insumo():
    if len(nome_insumo.get()) < 2 or len(lote_insumo.get()) < 1:
        messagebox.showerror("ERRO","Informe corretamente o Produto e Lote")
        lote_insumo.delete(0,END)
        nome_insumo.delete(0,END)

def visualizar_insumo():
    carregar_ultimo()

def salvar_add():
    cursor.execute(f"""
    INSERT INTO Estoque(Produto,Quantidade,DataValidade,Lote)
    VALUES
    ("{nome_insumo.get()}", {qtde_insumo.get()}, "{data_insumo.get()}", {lote_insumo.get()})
    """)
    conn.commit()
    caixa_texto.delete("1.0", END)
    
    messagebox.showinfo("ADICIONAR",f"{nome_insumo.get()} adicionado com sucesso!")
    b4.config(state="disable")
    limpar_tela()
    
    
######### criação da Janela ##################
    
window = Tk()
window.iconbitmap(r"C:\net\hashtag\ControledeEstoque_SQL_TK_V1\janela\mann.ico")
window.geometry("711x646")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 646,
    width = 711,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"janela/background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file = f"janela/imgbg_search.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = visualizar_insumo,
    relief = "flat")

b0.place(
    x = 64, y = 326,
    width = 50,
    height = 53)

img1 = PhotoImage(file = f"janela/imgbg_delete.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = deletar_insumo,
    relief = "flat")

b1.place(
    x = 69, y = 397,
    width = 40,
    height = 46)

img2 = PhotoImage(file = f"janela/imgbg_edit.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = consumir_insumo,
    relief = "flat")

b2.place(
    x = 66, y = 258,
    width = 50,
    height = 50)

img3 = PhotoImage(file = f"janela/imgbg_add.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = adicionar_insumo,
    relief = "flat")

b3.place(
    x = 64, y = 190,
    width = 49,
    height = 53)

img4 = PhotoImage(file = f"janela/img_check.png")
b4 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = salvar_add,
    relief = "flat")

b4.place(
    x = 69, y = 550,
    width = 40,
    height = 46)
b4.config(state="disable")

entry0_img = PhotoImage(file = f"janela/img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image = entry0_img)

caixa_texto = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

caixa_texto.place(
    x = 250, y = 502,
    width = 410,
    height = 114)

entry1_img = PhotoImage(file = f"janela/img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image = entry1_img)

nome_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

nome_insumo.place(
    x = 377, y = 278,
    width = 280,
    height = 31)

entry2_img = PhotoImage(file = f"janela/img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image = entry2_img)

data_insumo = DateEntry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

data_insumo.place(
    x = 377, y = 324,
    width = 280,
    height = 31)

entry3_img = PhotoImage(file = f"janela/img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image = entry3_img)

lote_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

lote_insumo.place(
    x = 377, y = 372,
    width = 280,
    height = 31)

entry4_img = PhotoImage(file = f"janela/img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image = entry4_img)

qtde_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

qtde_insumo.place(
    x = 377, y = 420,
    width = 280,
    height = 31)



carregar_ultimo()

window.resizable(False, False)
window.mainloop()

cursor.close()
conn.close()