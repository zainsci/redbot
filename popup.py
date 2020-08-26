import tkinter as tk
from tkinter import ttk
import webbrowser
from time import sleep


def open_reddit(permalink, window):
    webbrowser.open(f"https://www.reddit.com{permalink}")
    window.destroy()
    print("If Commenting Wait 10Min")
    sleep(600)


def next_post(window):
    window.destroy()


def popup_window(title, permalink):

    window = tk.Tk()
    window.geometry("400x200")
    window.title("Reddit Notification")

    btn_style = ttk.Style()
    btn_style.map("C.TButton",)

    main_frame = tk.Frame(window)
    main_frame.pack()

    frame = tk.Frame(main_frame)
    frame.grid(row=0, column=0)
    btn_frame = tk.Frame(main_frame)
    btn_frame.grid(row=1, column=0)

    lbl_title = ttk.Label(
        frame,
        text=title,
        wraplength=300,
        font=(None, 14),
        justify=tk.CENTER,
    )
    btn_open = ttk.Button(
        btn_frame,
        text="Open",
        command=lambda: open_reddit(permalink, window),
        style="C.TButton"
    )
    btn_next = ttk.Button(btn_frame, text="Next",
                          command=lambda: next_post(window))

    lbl_title.grid(row=0, column=0, pady=20)
    btn_open.grid(row=0, column=0, padx=10)
    btn_next.grid(row=0, column=1, padx=10)

    window.mainloop()


if __name__ == "__main__":
    popup_window(
        title="How To Work With TkinterHow To Work With TkinterHow To Work With TkinterHow To Work With Tkinter",
        permalink="/r/Askreddit",
    )
