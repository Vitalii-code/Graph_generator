import tkinter as tk

graph_info = [
    ["A", {"B": 2, "C": 3}],
    ["B", {"D": 7, "E": 3, "C": 5}],
    ["C", {"E": 4, "B": 6}],
    ["D", {"C": 1}],
    ["E", {"D": 7}],
    ["F", {"A": 1}],
]


def draw_circle(canvas, x, y, r, letter, color="blue"):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
    canvas.create_text(
        x,
        y,
        fill="white",
        text=letter,
    )


# return a middle poin between two points
def find_middle_pos(x1, y1, x2, y2):
    # middle x
    mx = (x1 + x2) / 2
    # middle y
    my = (y1 + y2) / 2

    return mx, my


def most_connections(graph_info):
    biggest = ["", 0]
    for i, node in enumerate(graph_info):
        length = len(node[1])
        if length > biggest[1]:
            biggest = [node[0], length]

    return biggest[0]


class Graph:
    def __init__(self, graph_info) -> None:
        self.__graph_info = graph_info

    # Tells you what circles and where to render them
    def circles_to_render(self):
        x = 50
        y = 50
        circ_pos = {}
        for i, node in enumerate(self.__graph_info):
            circ_pos[node[0]] = [x, y]

            x += 100
            # if y <= 150:
            #     y += 100
            #
            # elif y >= 150:
            #     x += 100

        return circ_pos

    def lines_to_render(self, circ_info):
        x = 50
        y = 50
        # this stores the positions of each line and the number that is suppose to be
        line_pos = []
        for i, node in enumerate(graph_info):
            for to_node in node[1].items():
                line_pos.append(
                    [
                        circ_info[node[0]][0],  # x position of the main node
                        circ_info[node[0]][1],  # y position of the main node
                        circ_info[to_node[0]][0],  # x position of the target node
                        circ_info[to_node[0]][1],  # y position of the target node
                        to_node[1],  # distance to the other node from user input
                        node[0],  # letter
                    ]
                )

                # canvas.create_line(
                #     circ_info[node[0]][0],  # x position of the main node
                #     circ_info[node[0]][1],  # y position of the main node
                #     circ_info[to_node[0]][0],  # x position of the target node
                #     circ_info[to_node[0]][1],  # y position of the target node
                # )

            x += 100
            # if y <= 150:
            #     y += 100
            #
            # elif y >= 150:
            #     x += 100

        return line_pos


res_x = 900
res_y = 720

root = tk.Tk()
root.geometry(f"{res_x}x{res_y}")
root.title("Canvas Demo")

canvas = tk.Canvas(root, width=res_x, height=res_y, bg="white")
my_graph1 = Graph(graph_info)


circ_info = my_graph1.circles_to_render()
lines_info = my_graph1.lines_to_render(circ_info)

# draw stuff
# draw the lines
for i in lines_info:
    letter = i[5]
    distance = i[4]
    main_x = i[0]
    main_y = i[1]
    # target x
    tx = i[2]
    # target y
    ty = i[3]

    canvas.create_line(main_x, main_y, tx, ty)

    mx, my = find_middle_pos(main_x, main_y, tx, ty)

    draw_circle(canvas, mx, my, r=10, letter="", color="black")
    canvas.create_text(
        mx,
        my,
        fill="white",
        text=distance,
    )


# draw the circles
for i in circ_info.items():
    draw_circle(canvas, i[1][0], i[1][1], r=20, letter=i[0])


canvas.pack(anchor=tk.CENTER, expand=True)
root.mainloop()

# x = 50
# y = 50
# for i, node in enumerate(graph_info):
#     for to_node in node[1]:
#         canvas.create_line(circ_pos[node[0]][0], circ_pos[node[0]][1],
#                            circ_pos[to_node][0], circ_pos[to_node][1])

#     if y <= 150:
#         y += 100

#     elif y >= 150:
#         x += 100


# for i in lines_info.items():
#     print(i)
#     canvas.create_line(circ_info[node[0]][0],
#            circ_info[node[0]][1],
#            circ_info[to_node][0],
#            circ_info[to_node][1])
