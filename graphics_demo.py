from graphics import *


def main():
    win = GraphWin("My Animation", 300, 300, autoflush=False)

    start = Point(10, 0)
    end = Point(10, 100)

    line = Line(start, end)
    line.setArrow("first")
    line.setWidth(5)

    line.draw(win)
    win.getMouse()
    for i in range(28):
        line.move(10, 10)
        update(24)

      # pause for click in window

    win.getMouse()

    win.close()


main()
