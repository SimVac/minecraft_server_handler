import tkinter as tk
from tkinter import font

palette = {'background': '#121212',
          'menu_bar': '#181818',
          'top_gradient': '#404040',
          'bottom_gradient': '#282828',
          'primary_text': '#FFFFFF',
          'secondary_text': '#B3B3B3'}

window = tk.Tk()
window.geometry("600x600")
window.title("Minecraft Server Manager")
window.wm_attributes('-transparentcolor','grey')
window.configure(background=palette['background'])
tk.Label(text="Minecraft Server Manager", font=("Arial", 20, "bold"), bg=palette['background'], fg=palette['primary_text']).pack()
window.mainloop()