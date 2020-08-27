import tkinter as tk
from tkinter import ttk
import webbrowser
from time import sleep


def open_reddit(permalink, window, interval):
    webbrowser.open(f"https://www.reddit.com{permalink}")
    window.destroy()
    if interval != None:
        print(f"If Commenting Wait {interval / 60} Min")
        sleep(int(interval))


def next_post(window):
    window.destroy()


def notification(sub, title, score, comments, time, permalink, interval):
    win = tk.Tk()
    win.title("Reddit Notification")

    group = tk.LabelFrame(win, text=sub, padx=10,
                          pady=10)
    group.pack(padx=10, pady=10)
    tk.Label(
        group, text=title, font=(None, 12), wraplength=300, anchor="n").grid(row=0, column=1, pady=12, sticky='n')
    inner_group = tk.Frame(group, padx=10, pady=10)
    inner_group.grid(row=0, column=0)

    lbl_1 = tk.LabelFrame(inner_group, text="Score", padx=5)
    tk.Label(lbl_1, text=score).pack(pady=5)

    lbl_2 = tk.LabelFrame(inner_group, text="Comments", padx=5)
    tk.Label(lbl_2, text=comments).pack(pady=5)

    lbl_3 = tk.LabelFrame(inner_group, text="Time", padx=5)
    tk.Label(lbl_3, text=time).pack(pady=5)

    lbl = [lbl_1, lbl_2, lbl_3]
    for i in lbl:
        i.grid(sticky="nswe")
        i.rowconfigure(0, weight=1)
        i.columnconfigure(0, weight=1)

    btn_group = tk.Frame(win, padx=10, pady=5)
    btn_group.pack(padx=10, pady=10)

    ttk.Button(btn_group, text="Open", command=lambda: open_reddit(permalink, win, interval)).grid(
        row=0, column=0, padx=10, pady=5)
    ttk.Button(btn_group, text="Next", command=lambda: next_post(win)).grid(
        row=0, column=1, padx=10, pady=5)

    win.mainloop()


if __name__ == "__main__":
    notification("Tkinter", "Tkinter Tkinter Tkinter Tkinter Tkinter Tkinter Tkinter Tkinter Tkinter Tkinter Tkinter",
                 "20K", "2.1K", "15:15 PM", "Link")
