import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Escolher Data")

# Cria um campo de data com calendário
data_entry = DateEntry(
    root,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="dd/mm/yyyy"  # formato da data
)
data_entry.pack(padx=20, pady=20)

def mostrar_data():
    data_selecionada = data_entry.get_date()
    print("Data escolhida:", data_selecionada)

botao = tk.Button(root, text="Confirmar", command=mostrar_data)
botao.pack(pady=10)

root.mainloop()
