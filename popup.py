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
    window.configure(background="#ffffff")

    frame = tk.Frame(window, bg="#ffffff")
    frame.pack(side=TOP)

    lbl_title = tk.Label(
        frame,
        text=title,
        wraplength=300,
        font=(None, 16),
        justify=CENTER,
        bg="#ffffff",
        fg="#000000",
    )
    btn_open = tk.Button(
        frame,
        text="Open",
        height=1,
        width=10,
        font=(None, 16),
        bg="#7952B3",
        fg="#fff",
        command=lambda: open_reddit(permalink, window),
    )

    lbl_title.grid(row=0, column=0, pady=10, sticky=N)
    btn_open.grid(row=1, column=0, pady=10, sticky=N)

    window.mainloop()


if __name__ == "__main__":
    popup_window(
        title="How To Work With TkinterHow To Work With TkinterHow To Work With TkinterHow To Work With Tkinter",
        permalink="/r/Askreddit",
    )
