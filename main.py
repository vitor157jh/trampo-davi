import tkinter as tk, sqlite3

# 1. Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Minha Primeira Janela")

# Define o tamanho inicial
janela.geometry("300x300")

def create_new_input(label_text):
    label = tk.Label(janela, text=label_text)
    label.pack(pady=2)

    input = tk.Entry(janela, text=label_text)
    input.pack(pady=2)
    return input

input_name = create_new_input("Nome:")
input_ra = create_new_input("Ra:")
input_nota = create_new_input("Nota:")
input_jus = create_new_input("Jus:")

conn = sqlite3.connect("app_data.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ra TEXT NOT NULL,
        nota INTEGER  NOT NULL,
        jus TEXT
    )
""")

conn.commit()

def submit_data():
    data_name = input_name.get()
    data_ra = input_ra.get()
    data_nota = input_nota.get()
    data_jus = input_jus.get()

    cursor.execute("""
    INSERT INTO users (name, ra, nota, jus) 
    VALUES (?, ?, ?, ?)
    """, (data_name, data_ra, data_nota, data_jus))
    
    conn.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

btn = tk.Button(janela, text="submit", command=submit_data)
btn.pack(pady=4)

janela.mainloop()
