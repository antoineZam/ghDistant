import tkinter as tk
from Constantes import HELLO_WORLD_TITLE, HELLO_WORLD_TEXT
from datetime import datetime

def main():
    window = tk.Tk()
    window.title(HELLO_WORLD_TITLE)
    window.geometry("350x200")
    window.configure(bg="white")  # Fond par défaut (modifié dans les commits)

    label = tk.Label(
        window,
        text=HELLO_WORLD_TEXT,
        fg="black",
        bg="yellow",
        font=("Arial", 12),
        justify="center"
    )
    label.pack(expand=True)
    

    window.mainloop()

if __name__ == "__main__":
    main()