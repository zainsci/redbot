import tkinter as tk
import webbrowser


def popup_window(title, link):
    window = tk.Tk()
    window.geometry("300x150")

    title = tk.Label(text=title)
    title.pack()

    link = tk.Button(
        text="Open", command=webbrowser.open(f"https://www.reddit.com{link}")
    )
    link.pack()

    window.mainloop()
