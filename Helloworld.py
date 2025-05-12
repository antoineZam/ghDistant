import tkinter as tk
from Constantes import HELLO_WORLD_TITLE, HELLO_WORLD_TEXT
from datetime import datetime

def main():
    window = tk.Tk()
    window.title(HELLO_WORLD_TITLE)
    window.geometry("200x200")
    window.configure(bg="white")  # Fond par défaut (modifié dans les commits)

    label = tk.Label(
        window,
        text=HELLO_WORLD_TEXT,
        fg="black",     # Couleur du texte (bleu dans un commit futur)
        bg="yellow",    # Fond du label (modifié dans les commits)
        font=("Arial", 12),
        justify="center"
    )
    label.pack(expand=True)

    # Exemple d'ajout ultérieur (ex: ajout de la date dans un commit futur)
    # date_label = tk.Label(window, text=datetime.now().strftime("%Y-%m-%d"))
    # date_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()