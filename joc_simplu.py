import random
import time
import os
from tkinter import messagebox
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=800, height=600)


def jocul():
    """Jocul cu testoasele"""
    # Innregistrare culori si nr. jucatori
    culori = ['red', 'blue', 'pink', 'purple', 'yellow', 'brown', 'orange', 'black']
    messagebox.showinfo(title='Regulament', message='Primadata trebuie sa alegi un numar de jucatori (min: 2,max: 6) \n'
                                                    'Apoi obligatoriu o culoare')
    num_jucatori = screen.numinput(title='Numar jucatori', prompt='Numar jucatori')
    num_jucatori = int(num_jucatori)
    while num_jucatori <= 1 or num_jucatori > 6:
        if num_jucatori <= 1:
            messagebox.showerror(title='Eroare!', message='Hey! ai ales un numar prea mic, trebuie s alegi minim 2 '
                                                          'jucatori')
            num_jucatori = screen.numinput(title='Numar jucatori', prompt='Numar jucatori')
        else:
            messagebox.showerror(title='Eroare!', message='Hey! ai ales un numar prea mare, poti alege maxim 6 jucatori')
            num_jucatori = screen.numinput(title='Numar jucatori', prompt='Numar jucatori')
    game0 = True
    lista_jucatori = []
    lista_culori_prov = []
    while game0 and len(lista_culori_prov) < num_jucatori:
        alegere_culoare = screen.textinput(title='Alegere culoare', prompt=f"Alege o culoare:\n{culori}").lower()
        if alegere_culoare in lista_culori_prov:
            messagebox.showerror(title='Alegere culoare',
                                               message="HEY, vezi ca aceasta " + "\"" + alegere_culoare + "\"" + "a "
                                                                                                                "mai "
                                                                                                                "fost "
                                                                                                                "aleasa").lower()
            continue
        elif alegere_culoare not in culori and alegere_culoare not in lista_culori_prov:
            messagebox.showerror(title='Alegere culoare', message="N-am inteles! Apasa \"ok\" pentru a continua")
            continue
        culori.remove(alegere_culoare)
        lista_culori_prov.append(alegere_culoare)
        if len(lista_culori_prov) < num_jucatori:
            question0 = screen.textinput(title='',
                                         prompt='Mai vrei sa alegi o culoare la alt jucator? Scrie "da", "yes" sau '
                                                '"nu", "no" ').lower()
        else:
            game0 = False
            continue
        while question0 != "da" and question0 != "yes" and question0 != "no" and question0 != "nu":
            question0 = screen.textinput(title='',
                                         prompt='N-am inteles! Scrie "da", "yes" sau "nu", "no" ').lower()
            continue
        if question0 == 'yes' or question0 == 'da':
            continue
        elif question0 == 'no' or question0 == 'nu':
            game0 = False
    while game0 is False and len(lista_culori_prov) < num_jucatori:
        culoare_random = random.choice(culori)
        culori.remove(culoare_random)
        lista_culori_prov.append(culoare_random)

    # Creearea obiectelor ion dictionar
    for a in range(int(num_jucatori)):
        dictionarul = {}
        testoasa = Turtle()
        testoasa.hideturtle()
        dictionarul['culoarea'] = lista_culori_prov[a]
        dictionarul['obiectul'] = testoasa
        dictionarul['obiectul'].color(dictionarul['culoarea'])
        dictionarul['obiectul'].hideturtle()
        dictionarul['obiectul'].shape('turtle')
        dictionarul['scor'] = 0
        lista_jucatori.append(dictionarul)
    # print(lista_culori_prov)
    # print(lista_jucatori)
    # print(len(lista_jucatori))

    # Punerea aleatoriu in lista
    lista_juc = []
    for b in range(len(lista_jucatori)):
        alegere = random.choice(lista_jucatori)
        lista_juc.append(alegere)
        lista_jucatori.remove(alegere)
    # print(lista_juc)
    # print(len(lista_juc))

    # Coordonatele si desenarea traseului
    # screen.setup(width=800, height=600)
    x = -380
    y = -150
    y = (y * num_jucatori) / 6
    # print(y)
    z = y
    for j in range(int(num_jucatori + 1)):
        j = Turtle()
        j.hideturtle()
        j.speed(100)
        j.penup()
        j.goto(x=x, y=y)
        j.pendown()
        for k in range(40):
            j.speed(100)
            j.forward(10)
            j.penup()
            j.speed(100)
            j.forward(10)
            j.pendown()
        y = y + 40
    # print(y)
    # Trasarea liniei finish
    linia_finish = Turtle()
    linia_finish.hideturtle()
    linia_finish.penup()
    linia_finish.goto(x=380, y=z)
    linia_finish.left(90)
    linia_finish.pendown()
    linia_finish.color('red')
    linia_finish.forward(abs(y - z) - 40)

    # Punerea la start a jucatorilor
    for pozitie in lista_juc:
        pozitie['obiectul'].showturtle()
        pozitie['obiectul'].penup()
        pozitie['obiectul'].goto(x=x, y=z + 20)
        z = z + 40

    # Start joc
    messagebox.showinfo(title='Start joc', message='Apasa "ok" pentru a incepe')
    primul = random.choice(lista_juc)
    random_primul = random.randint(5, 30)
    game1 = True
    while game1:
        for start in lista_juc:
            random_start = random.randint(5, 30)
            if primul['scor'] == 0:
                primul['obiectul'].speed(1)
                primul['obiectul'].forward(random_primul)
                primul['scor'] += random_start
            start['obiectul'].speed(1)
            start['obiectul'].forward(random_start)
            start['scor'] += random_start
            if start['scor'] >= 747:
                game1 = False
                mesajul = f"Castigatorul este {start['culoarea'].capitalize()}"
                messagebox.showinfo(title='Felicitari ', message=mesajul)
                break



jocul()
time.sleep(2)
game2 = True
while game2:
    intrebare = screen.textinput(title='Continuare', prompt='Doresti sa joci in continuare?("da", "yes" sau "nu", "no"').lower()
    if intrebare == "da" or intrebare == "yes":
        screen.clear()
        jocul()
    elif intrebare == "nu" or intrebare == "no":
        messagebox.showinfo(title='Inchidere joc', message='Jocul se va inchide!')
        time.sleep(2)
        game2 = False
        os.system('exit')
    elif intrebare != "da" and intrebare != "yes" and intrebare != "no" and intrebare != "nu":
        messagebox.showerror(title='Eroare', message="Nu inteleg raspunsul")
        continue




# screen.exitonclick()
