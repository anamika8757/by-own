import tkinter as tk

root = tk.Tk()

def press(n):
    print(n)

numbers = [
    (1, 2, 0), (2, 2, 1), (3, 2, 2),
    (4, 3, 0), (5, 3, 1), (6, 3, 2),
    (7, 4, 0), (8, 4, 1), (9, 4, 2),
    (0, 5, 0)
]

for num, r, c in numbers:
    tk.Button(
        root,
        text=str(num),
        bg='grey',
        width=7,
        command=lambda n=num: press(n)
    ).grid(row=r, column=c)

root.mainloop()
