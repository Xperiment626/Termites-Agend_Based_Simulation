def walk(steps = 1000, interval = 1, termites = 10, chips = 10, maxLimit = 10):
    import turtle as t
    import random as r
    import termite as te

    t.setworldcoordinates(-maxLimit-2, -maxLimit-2, maxLimit+2, maxLimit+2)
    limits = [-maxLimit, maxLimit, -maxLimit, maxLimit]
    termList = []  # Lista de objetos termitas
    chipList = []  # Lista de objetos chips
    clist = list()  # Lista de objetos turtle para los chips
    tlist = list()  # Lista de objetos turtle para las termitas

    """
    Crea una lista de objetos turtle y objetos termite
    """
    for pi in range(termites):
        termList.append(te.Termite((r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        # Asigna forma circulo a cada turtle
        tlist.append(t.Turtle(shape="turtle"))
        tlist[pi].color(termList[pi].getColor())  # Asigna color rojo a turtle
        tlist[pi].speed(0)  # Asigna la velocidad mas alta posible
        tlist[pi].shapesize(0.4, 0.6)  # Asigna el tamano de forma
        tlist[pi].penup()  # Pen up para no dejar rastro del camino
        # Va a la posicion inicial de cada termite
        tlist[pi].goto(termList[pi].getPos())

    """
    Crea una lista de objetos chips y sus turtle correspondientes
    """
    for pi in range(chips):
        chipList.append(te.Chip(pi, (r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        clist.append(t.Turtle(shape="square"))
        # Asigna color del chip a turtle
        clist[pi].color(chipList[pi].getColor())
        clist[pi].speed(0)  # Asigna la velocidad mas alta posible
        clist[pi].shapesize(0.4, 0.6)  # Asigna el tamano de forma
        clist[pi].penup()  # Pen up para no dejar rastro del camino
        # Va a la posicion inicial de cada chip
        clist[pi].goto(chipList[pi].getPos())

    screen = t.getscreen()  # Obtiene la pantalla de turtle para hacer tracer
    screen.bgcolor("#00FFC1") # Make background color change

    # Simulations based on the steps passed through terminal
    for ts in range(steps):
        # Iterate every turtle element in 'tlist'
        # i represent the index in the list
        # tc represent the turtle object in canvas
        for i, tc in enumerate(tlist):
            # postions of all Chips in the canvas
            posChips = {c.getPos(): c.index for c in chipList}
            
            posP = None
            posD = None
            auxPos = None
            
            # Checking if the current Termite has a Chip loaded
            if termList[i].getLoad() == None:
                # pickChip method returns the current position of the Termite
                posP = termList[i].pickChip(chipList, posChips)
            # The current Termite has no Chip loaded
            else:
                # Checking if in the current postion of the Termite is a Chip
                if termList[i].getPos() in posChips:
                    # Save the current position before move again
                    auxPos = termList[i].getPos()
                    # Generate movement for the Termite
                    termList[i].move(r, limits, interval)
                    # dropChip method return the current position of the Termite
                    posD = termList[i].dropChip(chipList, posChips, auxPos)
            
            # Update Chips position in canvas
            posChips = {c.getPos(): c.index for c in chipList}
            
            # Checking if the pickChip method return a position or None
            if posP is not None:
                # Getting the current index of the Chip in our position
                ind = posChips[posP]
                # With the index get the position of the Chip we are currently working with. Then we update its position
                clist[ind].goto(chipList[ind].getPos())
                 
            # Checking if the dropChip method return a position or None
            if posD is not None:
                # Getting the current index of the Chip in the current position after moving forward or backwards
                ind = posChips[posD]
                # With the index get the position of the Chip we are currently working with. Then we update its position
                clist[ind].goto(chipList[ind].getPos())

            # In order to have a Termite with memory we are setting the previous position of the Termite before moving again.
            termList[i].setPrevPos(termList[i].getPos())
            # Generate movement for the Termite
            termList[i].move(r, limits, interval)
            # Update the last position of the Termite to the current
            tc.goto(termList[i].getPos())

        screen.tracer(10000000000)  # Se refrescara la pantalla cada 10 ejecuciones

    t.exitonclick()  # Al hacer clic sobre la ventana grafica se cerrara

def main(args):
    """
    Uso:
    python walkTermites.py steps interval termites chips canvas_limit
    Parametros:
    steps: numero de pasos
    inteval: longitud del paso
    termites: number of termites
    chips: number of chips
    canvas_limit: canvas x,y in (-canvas_limit, canvas_limit)
    Ejemplo:
    python walkTermites.py 1000 1 10 10 10
    """

    if len(args) == 5:
        steps = int(args[0])
        interval = int(args[1])
        termites = int(args[2])
        chips = int(args[3])
        canvas_limit = int(args[4])
        walk(steps, interval, termites, chips, canvas_limit)
    else:
        print(main.__doc__)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
