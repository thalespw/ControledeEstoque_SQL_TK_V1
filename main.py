from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

######## funcionalidades do sistema #############
import sqlite3
import time

conn = sqlite3.connect('Estoque.db')
cursor = conn.cursor()


from main_window_tk import criar_interface
window,canvas,background_img ,nome_insumo, lote_insumo, data_insumo, qtde_insumo, b_search,b_delete,b_edit,b_add,b_save_add,b_save_edit,b_cancel,img0,img1,img2,img3,img4,img5,img6 = criar_interface()



def limpar_tela():
    habilitar_campos()
    lote_insumo.delete(0,END)
    data_insumo.delete(0,END)
    qtde_insumo.delete(0,END)
    nome_insumo.delete(0,END)
    desabilitar_campos()

def carregar_ultimo():
    limpar_tela()
    habilitar_campos()
    cursor.execute("SELECT Produto, Quantidade, DataValidade, Lote FROM Estoque ORDER BY id DESC LIMIT 1")
    ultimo = cursor.fetchone()

    if ultimo:
        nome_insumo.insert(0, ultimo[0])
        lote_insumo.insert(0, ultimo[3])
        qtde_insumo.insert(0, str(ultimo[1]))
        data_insumo.set_date(ultimo[2])
    desabilitar_campos()

def adicionar_insumo():
    limpar_tela()
    habilitar_campos()
    mostrar_botao_salvar_add()
    mostrar_botao_cancelar()
    nome_insumo.focus()
    
    
def deletar_insumo():
    print("deletar_insumo")
    if len(nome_insumo.get()) < 2:
        messagebox.showerror("ERRO","Produto Inválido")
        nome_insumo.delete(0,END)
        carregar_ultimo()
        return
    
    cursor.execute(f"""
    DELETE FROM Estoque
    WHERE Produto = "{nome_insumo.get()}"
    """)
    conn.commit()
    messagebox.showinfo("EXCLUSÃO",f"{nome_insumo.get()} excluído com sucesso!")
    habilitar_campos()
    limpar_tela()
    carregar_ultimo()
    desabilitar_campos()

def editar():
    pass

def salvar_edit():
    produto_original = nome_insumo.get()
    lote_original = lote_insumo.get()
    print(produto_original)
    print(lote_original)
    return


def abrir_janela_pesquisa():
    # Cria uma nova janela independente (filha da principal)
    janela_pesquisa = Toplevel(window)
    centralizar_janela(janela_pesquisa,300,200)
    janela_pesquisa.title("Pesquisar Produto")
    #janela_pesquisa.geometry("300x200")
    janela_pesquisa.configure(bg="#555555")
    janela_pesquisa.resizable(False, False)
    # Faz a janela ficar modal e sempre na frente
    janela_pesquisa.transient(window)   # filha da janela principal
    janela_pesquisa.grab_set()          # bloqueia a principal enquanto aberta
    janela_pesquisa.focus_force()       # coloca o foco nessa janela

    # Label e Entry para nome do produto
    Label(janela_pesquisa, text="Nome do Produto:",fg="#ffffff", bg="#555555").place(x=20, y=30)
    entry_nome = Entry(janela_pesquisa, width=30)
    entry_nome.place(x=20, y=50)

    # Label e Entry para lote
    Label(janela_pesquisa, text="Lote:", fg="#ffffff", bg="#555555").place(x=20, y=90)
    entry_lote = Entry(janela_pesquisa, width=30)
    entry_lote.place(x=20, y=110)
    entry_nome.focus()
    # Função interna que será ligada ao botão "Pesquisar"
   
    def pesquisar():
        nome = entry_nome.get().strip()
        lote = entry_lote.get().strip()
    
        if len(nome) < 2 or len(lote) < 1:
            messagebox.showerror("ERRO","Informe corretamente o Produto e Lote")
            return
        cursor.execute(f"""
        SELECT Produto, Quantidade, DataValidade, Lote 
        FROM Estoque 
        WHERE Produto = ? AND Lote = ?
        """, (nome, lote))

        resultado = cursor.fetchone()
        if resultado is None:
            messagebox.showerror("ERRO", f"Produto {nome} não encontrado.")
            return
        limpar_tela()
        habilitar_campos()
        nome_insumo.insert(0, resultado[0])
        lote_insumo.insert(0, resultado[3])
        qtde_insumo.insert(0, str(resultado[1]))
        data_insumo.set_date(resultado[2])
        desabilitar_campos()
        janela_pesquisa.destroy()

    # Botão de pesquisa
    Button(janela_pesquisa, text="Pesquisar", command=pesquisar).place(x=110, y=150)
    


def visualizar_insumo():
    carregar_ultimo()

def salvar_add():
    cursor.execute(f"""
    INSERT INTO Estoque(Produto,Quantidade,DataValidade,Lote)
    VALUES
    ("{nome_insumo.get()}", {qtde_insumo.get()}, "{data_insumo.get()}", {lote_insumo.get()})
    """)
    conn.commit()
    
    messagebox.showinfo("ADICIONAR",f"{nome_insumo.get()} adicionado com sucesso!")
    esconder_botao_salvar_add()
    limpar_tela()
    carregar_ultimo()

def cancelar():
    limpar_tela()
    carregar_ultimo()
    esconder_botao_salvar_add()
    esconder_botao_salvar_edit()
    esconder_botao_cancelar()

#########BOTOES SALVAR E CANCELAR - MOSTRAR / ESCONDER    
def mostrar_botao_salvar_add():
    b_save_add.place(x=69, y=550, width=40, height=46)
    nome_insumo.focus()

def esconder_botao_salvar_add():
    b_save_add.place_forget()

def mostrar_botao_salvar_edit():
    b_save_edit.place(x=69, y=550, width=40, height=46)

def esconder_botao_salvar_edit():
    b_save_edit.place_forget()

def mostrar_botao_cancelar():
    b_cancel.place(x=69, y=490, width=42, height=41)

def esconder_botao_cancelar():
    b_cancel.place_forget()

######### HABILITAR/DESABILITAR CAMPOS PARA EDIÇÃO #######

def habilitar_campos():
    nome_insumo.config(state="normal")
    lote_insumo.config(state="normal")
    data_insumo.config(state="normal")
    qtde_insumo.config(state="normal")
    nome_insumo.focus()

def desabilitar_campos():
    lote_insumo.config(state="disabled",disabledforeground="black")
    nome_insumo.config(state="disabled",disabledforeground="black")
    data_insumo.config(state="disabled",disabledforeground="black")
    qtde_insumo.config(state="disabled",disabledforeground="black")
    nome_insumo.focus()

b_add.config(command=adicionar_insumo)
b_edit.config(command=editar)
b_search.config(command=abrir_janela_pesquisa)
b_delete.config(command=deletar_insumo)
b_save_add.config(command=salvar_add)
b_save_edit.config(command=salvar_edit)
b_cancel.config(command=cancelar)
    
def centralizar_janela(janela,largura,altura):
    #pegar a resolução da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    #calcular posição
    x = (largura_tela - largura) //2
    y = (altura_tela - altura) //2
    #ajustar a tela
    janela.geometry(f'{largura}x{altura}+{x}+{y}')



carregar_ultimo()

window.resizable(False, False)
centralizar_janela(window,711,646)
window.mainloop()

cursor.close()
conn.close()