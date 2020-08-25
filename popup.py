from tkinter import *
import tkinter as tk
import webbrowser


def open_reddit(permalink, window):
    try:
        webbrowser.open(f"https://www.reddit.com{permalink}")
        window.destroy()
    except:
        pass


def popup_window(title, permalink):

    window = Tk()
    window.geometry("400x200")
    window.title("Reddit Notification")
    window.rowconfigure(0, minsize=400, weight=1)
    window.columnconfigure(0, minsize=150, weight=1)

    fr_title = tk.Frame(master=window, height=150, bg="#ffffff")

    lbl_title = tk.Label(fr_title, text=title,
                         bg="#ffffff", fg="#000000")
    btn_open = tk.Button(master=window, text="Open", height=1, width=5, bg="#7952B3", fg="#fff",
                         command=lambda: open_reddit(permalink, window))

    fr_title.grid(row=0, column=0, stick="n")
    lbl_title.grid(row=0, column=0, padx=10, pady=10)
    btn_open.grid(row=0, column=0, pady=150, sticky="n")

    window.mainloop()


if __name__ == "__main__":
    popup_window(title="How To Work With Tkinter", permalink="/r/Askreddit")
