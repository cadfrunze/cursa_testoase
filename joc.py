import random
from turtle import Turtle, Screen
from colors import culori
screen = Screen()

screen.setup(width=500, height=400)


def innregistrare_jucatori_culori():
    """Innregistrare playeri si culorile acestora"""
    dictionar_provizoriu = {}
    lista_provizorie = []
    lista_culori = []
    numar_jucatori = int(screen.numinput(title='Adauga un numar de testoase....',
                                         prompt='Alege un numar (Max: 6, Min: 1)'))
    while numar_jucatori < 1 or numar_jucatori > 6:
        if numar_jucatori < 1:
            numar_jucatori = int(screen.numinput(title='Adauga un numar de testoase....',
                                                 prompt='HEYY!!!!....Trebuie sa alegi minim un jucator'))
        else:
            numar_jucatori = int(screen.numinput(title='Adauga un numar de testoase....',
                                                 prompt='HEYY!!!!....'
                                                        'Ai ales mai mult de 6 jucatori (Max 6 playeri pot juca'))

    for n in range(numar_jucatori):
        alege_nume = screen.textinput(title="Alege un nume", prompt="Alege un nume").capitalize()

        while alege_nume in dictionar_provizoriu.keys() or len(alege_nume) < 3:
            if len(alege_nume) < 3:
                alege_nume = screen.textinput(title="Alege un nume",
                                              prompt="Te rog alege un nume din minim 3 caractere").capitalize()
                continue
            else:
                alege_nume = screen.textinput(title="Alege un nume",
                                              prompt="Alege alt nume. Acest nume: " + "\"" + alege_nume + "\"" +
                                                     " a mai fost ales").capitalize()
                continue
        alegere_culoare = screen.textinput(title="Fa un parius",
                                           prompt="Alege o culoare").lower()
        while alegere_culoare in lista_culori or alegere_culoare not in culori:
            if alegere_culoare in lista_culori:
                alegere_culoare = screen.textinput(title="Culorile",
                                                   prompt="Alege alta culoare Aceasta culoare " + "\"" + alegere_culoare +
                                                          "\"" + " a mai fost aleasa").lower()
                continue
            else:
                alegere_culoare = screen.textinput(title="Culorile",
                                                   prompt="Nu recunosc aceasta culoare: " + "\"" + alegere_culoare + "\"" +
                                                          " te rog alege alta culoare").lower()
                continue
        lista_culori.append(alegere_culoare)
        dictionar_provizoriu[alege_nume] = alegere_culoare
        culori.remove(alegere_culoare)
    return dictionar_provizoriu


dictionar_provizoriu = innregistrare_jucatori_culori()
print(dictionar_provizoriu)
numar_jucatori_provizoriu = []
for valoare in dictionar_provizoriu:
    print({valoare})
print(numar_jucatori_provizoriu)
# numere_lista = []
# for k in range(len(numar_jucatori_provizoriu) + 1, 7):
#     # noinspection PyTypeChecker
#     numar_jucatori_provizoriu.append(k)
#     numere_lista.append(k)
# print(culorile_jucatori)
# print(culori)
# lista_jucatori = []
# for n in range(len(numar_jucatori_provizoriu)):
#     element = random.choice(numar_jucatori_provizoriu)
#     lista_jucatori.append(element)
#     numar_jucatori_provizoriu.remove(element)
# for j in range(len(lista_jucatori)):
#     if lista_jucatori[j] in numere_lista:
#         lista_jucatori[j] = j + 1




















x = -240
y = -150

























screen.exitonclick()