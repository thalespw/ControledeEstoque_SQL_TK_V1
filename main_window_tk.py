from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

def criar_interface():
    window = Tk()
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
    b_search = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b_search.place(
        x = 64, y = 326,
        width = 50,
        height = 53)

    img1 = PhotoImage(file = f"janela/imgbg_delete.png")
    b_delete = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b_delete.place(
        x = 69, y = 397,
        width = 40,
        height = 46)

    img2 = PhotoImage(file = f"janela/imgbg_edit.png")
    b_edit = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b_edit.place(
        x = 66, y = 258,
        width = 50,
        height = 50)

    img3 = PhotoImage(file = f"janela/imgbg_add.png")
    b_add = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b_add.place(
        x = 64, y = 190,
        width = 49,
        height = 53)

    img4 = PhotoImage(file = f"janela/imgcheck.png")
    b_save_add = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    img5 = PhotoImage(file = f"janela/imgcheck.png")
    b_save_edit = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")
    
    img6 = PhotoImage(file = f"janela/imgbg_cancel.png")
    b_cancel = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")


    ###### CAIXAS DE TEXTO #############

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
        highlightthickness = 0,
        state="disabled",disabledforeground="black")

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
        highlightthickness = 0,
        state="disabled",disabledforeground="black")

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
        highlightthickness = 0,
        state="disabled",disabledforeground="black")

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
        highlightthickness = 0,
        state="disabled",disabledforeground="black")

    qtde_insumo.place(
        x = 377, y = 420,
        width = 280,
        height = 31)

    return window,canvas,background_img,nome_insumo, lote_insumo, data_insumo, qtde_insumo, b_search,b_delete,b_edit,b_add,b_save_add,b_save_edit,b_cancel,img0,img1,img2,img3,img4,img5,img6