from turtle import Turtle, Screen
t = Turtle()
screen = Screen()
screen.listen()


def in_fata():
    """Se misca in fata"""
    t.forward(10)


def in_spate():
    """Se duce in spate"""
    t.back(10)


def la_stanga():
    """Unghi spre stanga"""
    unghi_nou = t.heading() + 10
    t.setheading(unghi_nou)


def la_dreapta():
    """Unghi spre dreapta"""
    unghi_nou = t.heading() - 10
    t.setheading(unghi_nou)


def reseteaza():
    """Sterge tot desenu' si revine la pozitia initiala"""
    t.clear()
    t.reset()


screen.onkey(key='w', fun=in_fata)
screen.onkey(key='s', fun=in_spate)
screen.onkey(key='a', fun=la_stanga)
screen.onkey(key='d', fun=la_dreapta)
screen.onkey(key='c', fun=reseteaza)
screen.exitonclick()