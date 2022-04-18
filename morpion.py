from tkinter import *
from tkinter.messagebox import *

def click_management(evt):
    global turn, A, B, C

    #emplacement du clique
    cursor_x = evt.x 
    cursor_y = evt.y

    #on va placer une croix ou un rond selon le tour du joueur et l'emplacement du clique et rendre le placement d'un signe sur un autre impossible
    #partie des croix
    if turn == 0:
        if cursor_x > 0 and cursor_x < 100 and cursor_y < 100:
            if A[0] == 5 or A[0] == 4:
                pass
            else:
                Croix(50, 50)
                A[0] = 4
                turn = 1
        if cursor_x > 100 and cursor_x < 200 and cursor_y < 100:
            if A[1] == 5 or A[1] == 4:
                pass
            else:
                Croix(150, 50)
                A[1] = 4
                turn = 1
        if cursor_x > 200 and cursor_x < 300 and cursor_y < 100:
            if A[2] == 5 or A[2] == 4:
                pass
            else:
                Croix(250, 50)
                A[2] = 4
                turn = 1
        if cursor_x > 0 and cursor_x < 100 and cursor_y > 100 and cursor_y < 200:
            if B[0] == 5 or B[0] == 4:
                pass
            else:
                Croix(50, 150)
                B[0] = 4
                turn = 1
        if cursor_x > 100 and cursor_x < 200 and cursor_y > 100 and cursor_y < 200:
            if B[1] == 5 or B[1] == 4:
                pass
            else:
                Croix(150, 150)
                B[1] = 4
                turn = 1
        if cursor_x > 200 and cursor_x < 300 and cursor_y > 100 and cursor_y < 200:
            if B[2] == 5 or B[2] == 4:
                pass
            else:
                Croix(250, 150)
                B[2] = 4
                turn = 1
        if cursor_x > 0 and cursor_x < 100 and cursor_y > 200 and cursor_y < 300:
            if C[0] == 5 or C[0] == 4:
                pass
            else:
                Croix(50, 250)
                C[0] = 4
                turn = 1
        if cursor_x > 100 and cursor_x < 200 and cursor_y > 200 and cursor_y < 300:
            if C[1] == 5 or C[1] == 4:
                pass
            else:
                Croix(150, 250)
                C[1] = 4
                turn = 1
        if cursor_x > 200 and cursor_x < 300 and cursor_y > 200 and cursor_y < 300:
            if C[2] == 5 or C[2] == 4:
                pass
            else:
                Croix(250, 250)
                C[2] = 4
                turn = 1
        Result()

    #partie des ronds
    if turn == 1:
        if cursor_x > 0 and cursor_x < 100 and cursor_y < 100:
            if A[0] == 5 or A[0] == 4:
                pass
            else:
                Rond(50, 50)
                A[0] = 5
                turn = 0
        if cursor_x > 100 and cursor_x < 200 and cursor_y < 100:
            if A[1] == 5 or A[1] == 4:
                pass
            else:
                Rond(150, 50)
                A[1] = 5
                turn = 0
        if cursor_x > 200 and cursor_x < 300 and cursor_y < 100:
            if A[2] == 5 or A[2] == 4:
                pass
            else:
                Rond(250, 50)
                A[2] = 5
                turn = 0
        if cursor_x > 0 and cursor_x < 100 and cursor_y > 100 and cursor_y < 200:
            if B[0] == 5 or B[0] == 4:
                pass
            else:
                Rond(50, 150)
                B[0] = 5
                turn = 0
        if cursor_x > 100 and cursor_x < 200 and cursor_y > 100 and cursor_y < 200:
            if B[1] == 5 or B[1] == 4:
                pass
            else:
                Rond(150, 150)
                B[1] = 5
                turn = 0
        if cursor_x > 200 and cursor_x < 300 and cursor_y > 100 and cursor_y < 200:
            if B[2] == 5 or B[2] == 4:
                pass
            else:
                Rond(250, 150)
                B[2] = 5
                turn = 0
        if cursor_x > 0 and cursor_x < 100 and cursor_y > 200 and cursor_y < 300:
            if C[0] == 5 or C[0] == 4:
                pass
            else:
                Rond(50, 250)
                C[0] = 5
                turn = 0
        if cursor_x > 100 and cursor_x < 200 and cursor_y > 200 and cursor_y < 300:
            if C[1] == 5 or C[1] == 4:
                pass
            else:
                Rond(150, 250)
                C[1] = 5
                turn = 0
        if cursor_x > 200 and cursor_x < 300 and cursor_y > 200 and cursor_y < 300:
            if C[2] == 5 or C[2] == 4:
                pass
            else:
                Rond(250, 250)
                C[2] = 5
                turn = 0
        Result()

#croix placé à un emplacement défini par x et y   
def Croix(x,y):
    canvas.create_line(x-45,y-45,x+45,y+45, fill="blue", width=3)
    canvas.create_line(x+45,y-45,x-45,y+45, fill="blue", width=3)

#rond placé à un emplacement défini par x et y
def Rond(x, y):
    canvas.create_oval(x-45,y-45,x+45,y+45, fill="red", width=3)

def Result():
    global turn,A,B,C
    #on annonce la victoire du joueur croix
    if A[0] == 4 and A[1] == 4 and A[2] == 4:
        canvas.create_line(5, 50, 295, 50, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if B[0] == 4 and B[1] == 4 and B[2] == 4:
        canvas.create_line(5, 150, 295, 150, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if C[0] == 4 and C[1] == 4 and C[2] == 4:
        canvas.create_line(5, 250, 295, 250, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if A[0] == 4 and B[0] == 4 and C[0] == 4:
        canvas.create_line(50, 5, 50, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if A[1] == 4 and B[1] == 4 and C[1] == 4:
        canvas.create_line(150, 5, 150, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if A[2] == 4 and B[2] == 4 and C[2] == 4:
        canvas.create_line(250, 5, 250, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if A[0] == 4 and B[1] == 4 and C[2] == 4:
        canvas.create_line(5, 5, 295, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    if A[2] == 4 and B[1] == 4 and C[0] == 4:
        canvas.create_line(295, 5, 5, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur croix")
        turn = 2
    #on annonce la victoire du joueur rond
    if A[0] == 5 and A[1] == 5 and A[2] == 5:
        canvas.create_line(5, 50, 295, 50, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if B[0] == 5 and B[1] == 5 and B[2] == 5:
        canvas.create_line(5, 150, 295, 150, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if C[0] == 5 and C[1] == 5 and C[2] == 5:
        canvas.create_line(5, 250, 295, 250, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if A[0] == 5 and B[0] == 5 and C[0] == 5:
        canvas.create_line(50, 5, 50, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if A[1] == 5 and B[1] == 5 and C[1] == 5:
        canvas.create_line(150, 5, 150, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if A[2] == 5 and B[2] == 5 and C[2] == 5:
        canvas.create_line(250, 5, 250, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if A[0] == 5 and B[1] == 5 and C[2] == 5:
        canvas.create_line(5, 5, 295, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2
    if A[2] == 5 and B[1] == 5 and C[0] == 5:
        canvas.create_line(295, 5, 5, 295, fill="yellow", width=5)
        showinfo(title="Morpion", message="Résultat : Victoire du joueur rond")
        turn = 2

#tour : 0 étant le tour de la croix et 1 le tour du rond
turn = 0

# la valeur de la croix = 4; la valeur du rond = 5
A = [1, 2, 3]
B = [1, 2, 3]
C = [1, 2, 3]

#configuration de la fenetre
window = Tk()
window.title("Morpion")
window.geometry("720x480")
window.config(bg="#CCAACC")

title = Label(window, text="Morpion", font=("Impact", 50), bg="#CCAACC", fg="yellow")
title.pack()

#configuration du canevas
width = 300
height = 300
canvas = Canvas(window, width=width, height=height, bg="#FF749E")
canvas.create_line(100, 0, 100, 310, fill="white", width=3)
canvas.create_line(200, 0, 200, 310, fill="white", width=3)
canvas.create_line(0, 100, 310, 100, fill="white", width=3)
canvas.create_line(0, 200, 310, 200, fill="white", width=3)
canvas.pack(expand=YES)
canvas.bind('<Button-1>', click_management)

#afficher la fenetre
window.mainloop()