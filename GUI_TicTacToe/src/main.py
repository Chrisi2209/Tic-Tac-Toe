from argparse import ArgumentError
import tkinter as tk
import time


def canvas_setup():
    CANVAS.create_line(SCALE_FACTOR, 0, SCALE_FACTOR, 3 * SCALE_FACTOR, fill="white")
    CANVAS.create_line(
        2 * SCALE_FACTOR, 0, 2 * SCALE_FACTOR, 3 * SCALE_FACTOR, fill="white"
    )
    CANVAS.create_line(0, SCALE_FACTOR, 3 * SCALE_FACTOR, SCALE_FACTOR, fill="white")
    CANVAS.create_line(
        0, 2 * SCALE_FACTOR, 3 * SCALE_FACTOR, 2 * SCALE_FACTOR, fill="white"
    )


def convert_list_into_player(list, x_list):
    if list == x_list:
        return "x"
    return "o"


def win_draw_check(x, o):
    # 3 in a row
    won = False
    for player in x, o:
        for row in range(3):
            won = True
            for column in range(3):
                if (column, row) not in player:
                    won = False
            if won == True:
                return convert_list_into_player(player, x)
    # 3 in a column
    won = False
    for player in x, o:
        for column in range(3):
            won = True
            for row in range(3):
                if (column, row) not in player:
                    won = False
            if won == True:
                return convert_list_into_player(player, x)
    # diagonal
    for player in x, o:
        for inverter in range(2):
            won = True
            for i in range(3):
                # y coor is inverted for bottom left -> top right
                if (i, i + (-2 * i + 2) * inverter) not in player:
                    won = False
            if won == True:
                return convert_list_into_player(player, x)

    if len(x + o) >= 9:
        return "draw"

    return None


def draw_cross(grid_field, x_sprites):
    x_sprites.append(
        (
            CANVAS.create_line(
                (grid_field[0] + OFFSET) * SCALE_FACTOR,
                (grid_field[1] + OFFSET) * SCALE_FACTOR,
                (grid_field[0] + 1 - OFFSET) * SCALE_FACTOR,
                (grid_field[1] + 1 - OFFSET) * SCALE_FACTOR,
                fill="white",
            ),
            CANVAS.create_line(
                (grid_field[0] + 1 - OFFSET) * SCALE_FACTOR,
                (grid_field[1] + OFFSET) * SCALE_FACTOR,
                (grid_field[0] + OFFSET) * SCALE_FACTOR,
                (grid_field[1] + 1 - OFFSET) * SCALE_FACTOR,
                fill="white",
            ),
        )
    )


def draw_circle(grid_field, o_sprites):
    o_sprites.append(
        CANVAS.create_oval(
            (grid_field[0] + OFFSET) * SCALE_FACTOR,
            (grid_field[1] + OFFSET) * SCALE_FACTOR,
            (grid_field[0] + 1 - OFFSET) * SCALE_FACTOR,
            (grid_field[1] + 1 - OFFSET) * SCALE_FACTOR,
            outline="white",
        )
    )


def reset(x_coors, o_coors, x_sprites, o_sprites):
    x_coors.clear()
    o_coors.clear()
    for sprite1, sprite2 in x_sprites:
        CANVAS.delete(sprite1)
        CANVAS.delete(sprite2)
    for sprite in o_sprites:
        CANVAS.delete(sprite)


def root_updater(func):
    root.update()
    func()


# @root_updater
def draw_animation():
    root.update()
    big_draw = CANVAS.create_text(
        WIDTH / 2, HEIGHT / 2, text="DRAW", font=50, color="white"
    )
    root.update()
    time.sleep(END_DELAY)
    CANVAS.delete(big_draw)
    root.update()


# @root_updater
def x_win_animation():
    root.update()
    big_x = (
        CANVAS.create_line(
            OFFSET * SCALE_FACTOR,
            OFFSET * SCALE_FACTOR,
            (3 - OFFSET) * SCALE_FACTOR,
            (3 - OFFSET) * SCALE_FACTOR,
            fill="white",
        ),
        CANVAS.create_line(
            (3 - OFFSET) * SCALE_FACTOR,
            OFFSET * SCALE_FACTOR,
            OFFSET * SCALE_FACTOR,
            (3 - OFFSET) * SCALE_FACTOR,
            fill="white",
        ),
    )

    root.update()
    time.sleep(END_DELAY)

    for element in big_x:
        CANVAS.delete(element)

    root.update()


# @root_updater
def o_win_animation():
    root.update()
    big_o = CANVAS.create_oval(
        OFFSET * SCALE_FACTOR,
        OFFSET * SCALE_FACTOR,
        (3 - OFFSET) * SCALE_FACTOR,
        (3 - OFFSET) * SCALE_FACTOR,
        outline="white",
    )

    root.update()
    time.sleep(END_DELAY)

    CANVAS.delete(big_o)
    root.update()


def click(event, x_coors, o_coors, x_sprites, o_sprites):
    global turn
    grid_field = (event.x // SCALE_FACTOR, event.y // SCALE_FACTOR)
    if grid_field not in x_coors and grid_field not in o_coors:
        if turn:
            x_coors.append(grid_field)
            draw_cross(grid_field, x_sprites)
        else:
            o_coors.append(grid_field)
            draw_circle(grid_field, o_sprites)

        match win_draw_check(x_coors, o_coors):
            case "draw":
                print("draw!")
                reset(x_coors, o_coors, x_sprites, o_sprites)
                draw_animation()
                turn = True
            case "x":
                print("x won")
                reset(x_coors, o_coors, x_sprites, o_sprites)
                x_win_animation()
                turn = True
            case "o":
                print("o won")
                reset(x_coors, o_coors, x_sprites, o_sprites)
                o_win_animation()
                turn = True
            case None:
                turn = not turn
            case _:
                raise ArgumentError()


if __name__ == "__main__":
    root = tk.Tk()
    SCALE_FACTOR = 345
    WIDTH = 3 * SCALE_FACTOR
    HEIGHT = 3 * SCALE_FACTOR
    OFFSET = 0.1
    END_DELAY = 2
    CANVAS = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    CANVAS.pack()
    turn = True  # True means cross, False means circle
    x_coors = []
    o_coors = []
    x_sprites = []
    o_sprites = []
    canvas_setup()
    root.bind(
        "<Button-1>", lambda event: click(event, x_coors, o_coors, x_sprites, o_sprites)
    )

    root.mainloop()
