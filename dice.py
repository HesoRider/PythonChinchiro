"""
Copyright (C) 2022 ヘソライダー All Rights Reserved.
"""
import random, tkinter

root = tkinter.Tk()
root.title("Pythonチンチロ")
root.minsize(900, 600)

dices = [
    tkinter.PhotoImage(file='1.png').subsample(2, 2),
    tkinter.PhotoImage(file='2.png').subsample(2, 2),
    tkinter.PhotoImage(file='3.png').subsample(2, 2),
    tkinter.PhotoImage(file='4.png').subsample(2, 2),
    tkinter.PhotoImage(file='5.png').subsample(2, 2),
    tkinter.PhotoImage(file='6.png').subsample(2, 2),
]

canvas = tkinter.Canvas(root, width=900, height=600)

# さいころを振る
def play():
    numbers = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]
    for i in range(0, len(numbers)): canvas.create_image(300*i+150, 300, image=dices[numbers[i]])
    numbers.sort()
    # 役がある目だけ表示
    if numbers == [3, 4, 5]: label["text"] = "シゴロ, 倍付け"
    elif numbers[0] == numbers[1] == numbers[2]:
        if numbers[0] == 0: label["text"] = "ピンゾロ, 5倍付け"
        else: label["text"] = "ゾロ目, 3倍付け"
    elif numbers == [0, 1, 2]: label["text"] = "ヒフミ, 倍払い"
    else: label["text"] = "役なし"

title = tkinter.Label(root, font=("", 50))
title.pack(pady=20)
title["text"] = "Pythonチンチロ"
button = tkinter.Button(root, text="振る", font=("", 20), width=10)
button["command"] = play
button.pack(pady=20)
label = tkinter.Label(root, font=("", 20))    
label.pack()
canvas.pack()

root.mainloop()