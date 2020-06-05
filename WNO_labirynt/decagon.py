import numpy as np
import matplotlib.pyplot as plt


class Pole:
    def __init__(self, c_type, position_y, position_x):
        self.left_side = 1
        self.right_side = 1
        self.top_left1_side = 1
        self.top_left2_side = 1
        self.top_right1_side = 1
        self.top_right2_side = 1
        self.down_left1_side = 1
        self.down_left2_side = 1
        self.down_right1_side = 1
        self.down_right2_side = 1

        self.cell_type = c_type  # 0 dziesieciokat, 1 gwiazdka

        self.pos = [position_y, position_x]

    def get_type(self):
        return self.cell_type

    def get_pos(self):
        return self.pos


def draw_decagon(decagon, rad):
    center = decagon.get_pos()
    points = np.zeros((10, 2))
    radius = rad
    for i in range(10):
        angle = i * 36 - 18
        points[i] = [center[0] + radius * np.sin(np.radians(angle)), center[1] + radius * np.cos(np.radians(angle))]

    line_fade = "0.85"
    if decagon.right_side == 1:
        ax.plot([points[0, 1], points[1, 1]], [points[0, 0], points[1, 0]], 'k-')
    else:
        ax.plot([points[0, 1], points[1, 1]], [points[0, 0], points[1, 0]], 'k:', color=line_fade)
    if decagon.top_right1_side == 1:
        ax.plot([points[1, 1], points[2, 1]], [points[1, 0], points[2, 0]], 'k-')
    else:
        ax.plot([points[1, 1], points[2, 1]], [points[1, 0], points[2, 0]], 'k:', color=line_fade)
    if decagon.top_right2_side == 1:
        ax.plot([points[2, 1], points[3, 1]], [points[2, 0], points[3, 0]], 'k-')
    else:
        ax.plot([points[2, 1], points[3, 1]], [points[2, 0], points[3, 0]], 'k:', color=line_fade)
    if decagon.top_left2_side == 1:
        ax.plot([points[3, 1], points[4, 1]], [points[3, 0], points[4, 0]], 'k-')
    else:
        ax.plot([points[3, 1], points[4, 1]], [points[3, 0], points[4, 0]], 'k:', color=line_fade)
    if decagon.top_left1_side == 1:
        ax.plot([points[4, 1], points[5, 1]], [points[4, 0], points[5, 0]], 'k-')
    else:
        ax.plot([points[4, 1], points[5, 1]], [points[4, 0], points[5, 0]], 'k:', color=line_fade)
    if decagon.left_side == 1:
        ax.plot([points[5, 1], points[6, 1]], [points[5, 0], points[6, 0]], 'k-')
    else:
        ax.plot([points[5, 1], points[6, 1]], [points[5, 0], points[6, 0]], 'k:', color=line_fade)
    if decagon.down_left1_side == 1:
        ax.plot([points[6, 1], points[7, 1]], [points[6, 0], points[7, 0]], 'k-')
    else:
        ax.plot([points[6, 1], points[7, 1]], [points[6, 0], points[7, 0]], 'k:', color=line_fade)
    if decagon.down_left2_side == 1:
        ax.plot([points[7, 1], points[8, 1]], [points[7, 0], points[8, 0]], 'k-')
    else:
        ax.plot([points[7, 1], points[8, 1]], [points[7, 0], points[8, 0]], 'k:', color=line_fade)
    if decagon.down_right2_side == 1:
        ax.plot([points[8, 1], points[9, 1]], [points[8, 0], points[9, 0]], 'k-')
    else:
        ax.plot([points[8, 1], points[9, 1]], [points[8, 0], points[9, 0]], 'k:', color=line_fade)
    if decagon.down_right1_side == 1:
        ax.plot([points[-1, 1], points[0, 1]], [points[-1, 0], points[0, 0]], 'k-')
    else:
        ax.plot([points[-1, 1], points[0, 1]], [points[-1, 0], points[0, 0]], 'k:', color=line_fade)



def create_maze(y_len, x_len, rysuj_droge):
    y_length = y_len * 2 - 1
    x_length = x_len
    maze = [[None for i in range(x_length)] for j in range(y_length)]

    #Tworzenie labiryntu - lista obiktów klasy Pole (na przemian rzędy pól dekagonalnych i gwiazdek)
    radius = 5
    for i in range(y_length):
        for j in range(x_length):
            if i % 2 == 0:
                cell_type = 0
                cen_y = -(radius + i * radius)
                cen_x = radius + 2 * j * radius * np.cos(np.radians(18))
            else:
                cell_type = 1
                cen_y = -(radius + i * radius)
                cen_x = 2 * j * radius * np.cos(np.radians(18))

            maze[i][j] = Pole(cell_type, cen_y, cen_x)

    #Tworzenie ścian w labiryncie za pomocą metody recursive backtracking
    maze_values = np.zeros((y_length, x_length))  #Macierz stanu pól labiryntu
    # (0 - nieodwiedzone, 1 - odwiedzone, 2 - odwiedzone bez nieodwiedzonych sąsiadów)
    stack_cells = []  #Stos pól, po których możemy backtrackwać. Jak jest pusty to koniec algorytmu
    cell_y = 0
    cell_x = 0
    stack_cells.append([cell_y, cell_x])
    while stack_cells:
        cell_y = stack_cells[len(stack_cells) - 1][0]
        cell_x = stack_cells[len(stack_cells) - 1][1]
        if maze_values[cell_y, cell_x] != 2:
            maze_values[cell_y, cell_x] = 1
            curr_cell = maze[cell_y][cell_x]
            #Szukanie sasiadow
            '''
            Reguly sasiedztwa(9 - obecna komorka, 1 - sasiad gwiazdka, 2 - sasiad decagon, 0 - inne(niewazne) komorki):
            Decagon  |  Gwiazdka
            0 1 1 0  |   0 2 2 0
            2 9 2 0  |   0 0 9 0
            0 1 1 0  |   0 2 2 0
            '''
            neighbours = []
            if curr_cell.get_type() == 0:  #Dziesieciokat
                if cell_x != 0 and maze_values[cell_y, cell_x - 1] == 0:  #Lewy sasiad
                    neighbours.append([cell_y, cell_x - 1])
                if cell_x != 0 and cell_y != 0 and maze_values[cell_y - 1, cell_x] == 0:  #Lewy gorny sasiad
                    neighbours.append([cell_y - 1, cell_x])
                if cell_x != 0 and cell_y != y_length - 1 and maze_values[cell_y + 1, cell_x] == 0:  #Lewy dolny sasiad
                    neighbours.append([cell_y + 1, cell_x])
                if cell_x != x_length - 1 and maze_values[cell_y, cell_x + 1] == 0:  #Prawy sasiad
                    neighbours.append([cell_y, cell_x + 1])
                if cell_x != x_length - 1 and cell_y != 0 and maze_values[cell_y - 1, cell_x + 1] == 0:  #Prawy gorny sasiad
                    neighbours.append([cell_y - 1, cell_x + 1])
                if cell_x != x_length - 1 and cell_y != y_length - 1 and maze_values[cell_y + 1, cell_x + 1] == 0:  #Prawy dolny sasiad
                    neighbours.append([cell_y + 1, cell_x + 1])
            else:  #Gwiazdka
                if maze_values[cell_y - 1, cell_x - 1] == 0:  #Lewy gorny sasiad
                    neighbours.append([cell_y - 1, cell_x - 1])
                if maze_values[cell_y + 1, cell_x - 1] == 0:  #Lewy dolny sasiad
                    neighbours.append([cell_y + 1, cell_x - 1])
                if maze_values[cell_y - 1, cell_x] == 0:  #Prawy gorny sasiad
                    neighbours.append([cell_y - 1, cell_x])
                if maze_values[cell_y + 1, cell_x] == 0:  #Prawy dolny sasiad
                    neighbours.append([cell_y + 1, cell_x])

            #Losowanie sasiada
            if len(neighbours) == 0:  #Jak nie ma sasiadow to zapisujemy komorke jako typ 2
                maze_values[cell_y, cell_x] = 2
            else:
                if len(neighbours) == 1:
                    new_y, new_x = neighbours[0]
                else:
                    new_y, new_x = neighbours[np.random.randint(0, len(neighbours) - 1)]
                diff_y = new_y - cell_y
                diff_x = new_x - cell_x
                '''
                Reguly sasiedztwa(9 - obecna komorka, 1 - sasiad gwiazdka, 2 - sasiad decagon, 0 - inne(niewazne) komorki):
                Decagon  |  Gwiazdka
                0 1 1 0  |   0 2 2 0
                2 9 2 0  |   0 0 9 0
                0 1 1 0  |   0 2 2 0
                '''
                if curr_cell.get_type() == 0:  # Dziesieciokat
                    if diff_x == -1:  # Lewy sasiad
                        maze[cell_y][cell_x].left_side = 0
                        maze[new_y][new_x].right_side = 0
                    elif diff_x == 0 and diff_y == -1:  # Lewy gorny sasiad
                        maze[cell_y][cell_x].top_left1_side = 0
                        maze[cell_y][cell_x].top_left2_side = 0
                        maze[new_y][new_x].down_right1_side = 0
                        maze[new_y][new_x].down_right2_side = 0
                    elif diff_x == 0 and diff_y == 1:  # Lewy dolny sasiad
                        maze[cell_y][cell_x].down_left1_side = 0
                        maze[cell_y][cell_x].down_left2_side = 0
                        maze[new_y][new_x].top_right1_side = 0
                        maze[new_y][new_x].top_right2_side = 0
                    elif diff_x == 1 and diff_y == 0:  # Prawy sasiad
                        maze[cell_y][cell_x].right_side = 0
                        maze[new_y][new_x].left_side = 0
                    elif diff_x == 1 and diff_y == -1:  # Prawy gorny sasiad
                        maze[cell_y][cell_x].top_right1_side = 0
                        maze[cell_y][cell_x].top_right2_side = 0
                        maze[new_y][new_x].down_left1_side = 0
                        maze[new_y][new_x].down_left2_side = 0
                    elif diff_x == 1 and diff_y == 1:  # Prawy dolny sasiad
                        maze[cell_y][cell_x].down_right1_side = 0
                        maze[cell_y][cell_x].down_right2_side = 0
                        maze[new_y][new_x].top_left1_side = 0
                        maze[new_y][new_x].top_left2_side = 0
                else:  # Gwiazdka
                    if diff_x == -1 and diff_y == -1:  # Lewy gorny sasiad
                        maze[cell_y][cell_x].top_left1_side = 0
                        maze[cell_y][cell_x].top_left2_side = 0
                        maze[new_y][new_x].down_right1_side = 0
                        maze[new_y][new_x].down_right2_side = 0
                    elif diff_x == -1 and diff_y == 1:  # Lewy dolny sasiad
                        maze[cell_y][cell_x].down_left1_side = 0
                        maze[cell_y][cell_x].down_left2_side = 0
                        maze[new_y][new_x].top_right1_side = 0
                        maze[new_y][new_x].top_right2_side = 0
                    elif diff_x == 0 and diff_y == -1:  # Prawy gorny sasiad
                        maze[cell_y][cell_x].top_right1_side = 0
                        maze[cell_y][cell_x].top_right2_side = 0
                        maze[new_y][new_x].down_left1_side = 0
                        maze[new_y][new_x].down_left2_side = 0
                    elif diff_x == 0 and diff_y == 1:  # Prawy dolny sasiad
                        maze[cell_y][cell_x].down_right1_side = 0
                        maze[cell_y][cell_x].down_right2_side = 0
                        maze[new_y][new_x].top_left1_side = 0
                        maze[new_y][new_x].top_left2_side = 0

                stack_cells.append([new_y, new_x])
        else:
            stack_cells.pop()

    #Szukanie drogi w labiryncie za pomocą metody recursive backtracking
    start_y = 0
    start_x = 0
    finish_y = y_length - 1
    finish_x = x_length - 1
    maze_values = np.zeros((y_length, x_length))  # Macierz stanu pól labiryntu
    # (0 - nieodwiedzone, 1 - odwiedzone, 2 - odwiedzone bez nieodwiedzonych sąsiadów)
    stack_cells = []  # Stos pól, po których możemy backtrackwać. Jak sie skonczy, to droga nie zostala znaleziona.
    # W stosie tym znajdują się nasza droga (wszystkie pola, po których musieliśmy przejść, aby dojść do końcowego pola)
    cell_y = start_y
    cell_x = start_x
    stack_cells.append([cell_y, cell_x])
    while stack_cells:
        cell_y = stack_cells[len(stack_cells) - 1][0]
        cell_x = stack_cells[len(stack_cells) - 1][1]
        if cell_y == finish_y and cell_x == finish_x:  #Jak wykryjemy pole koncowe, to konczymy algorytm
            break
        elif maze_values[cell_y, cell_x] != 2:
            maze_values[cell_y, cell_x] = 1
            curr_cell = maze[cell_y][cell_x]
            #Szukanie sasiadow
            '''
            Reguly sasiedztwa(9 - obecna komorka, 1 - sasiad gwiazdka, 2 - sasiad decagon, 0 - inne(niewazne) komorki):
            Decagon  |  Gwiazdka
            0 1 1 0  |   0 2 2 0
            2 9 2 0  |   0 0 9 0
            0 1 1 0  |   0 2 2 0
            '''
            neighbours = []
            if curr_cell.get_type() == 0:  # Dziesieciokat
                if curr_cell.left_side == 0 and maze_values[cell_y, cell_x - 1] == 0:  # Lewy sasiad
                    neighbours.append([cell_y, cell_x - 1])
                if curr_cell.top_left1_side == 0 or curr_cell.top_left2_side == 0:
                    if maze_values[cell_y - 1, cell_x] == 0:  # Lewy gorny sasiad
                        neighbours.append([cell_y - 1, cell_x])
                if curr_cell.down_left1_side == 0 or curr_cell.down_left2_side == 0:
                    if maze_values[cell_y + 1, cell_x] == 0:  # Lewy dolny sasiad
                        neighbours.append([cell_y + 1, cell_x])
                if curr_cell.right_side == 0 and maze_values[cell_y, cell_x + 1] == 0:  # Prawy sasiad
                    neighbours.append([cell_y, cell_x + 1])
                if curr_cell.top_right1_side == 0 or curr_cell.top_right2_side == 0:
                    if maze_values[cell_y - 1, cell_x + 1] == 0:  # Prawy gorny sasiad
                        neighbours.append([cell_y - 1, cell_x + 1])
                if curr_cell.down_right1_side == 0 or curr_cell.down_right2_side == 0:
                    if maze_values[cell_y + 1, cell_x + 1] == 0:  # Prawy dolny sasiad
                        neighbours.append([cell_y + 1, cell_x + 1])
            else:  # Gwiazdka
                if curr_cell.top_left1_side == 0 or curr_cell.top_left2_side == 0:
                    if maze_values[cell_y - 1, cell_x - 1] == 0:  # Lewy gorny sasiad
                        neighbours.append([cell_y - 1, cell_x - 1])
                if curr_cell.down_left1_side == 0 or curr_cell.down_left2_side == 0:
                    if maze_values[cell_y + 1, cell_x - 1] == 0:  # Lewy dolny sasiad
                        neighbours.append([cell_y + 1, cell_x - 1])
                if curr_cell.top_right1_side == 0 or curr_cell.top_right2_side == 0:
                    if maze_values[cell_y - 1, cell_x] == 0:  # Prawy gorny sasiad
                        neighbours.append([cell_y - 1, cell_x])
                if curr_cell.down_right1_side == 0 or curr_cell.down_right2_side == 0:
                    if maze_values[cell_y + 1, cell_x] == 0:  # Prawy dolny sasiad
                        neighbours.append([cell_y + 1, cell_x])

            # Losowanie sasiada
            if len(neighbours) == 0:  #Jak nie ma sasiadow to zapisujemy komorke jako typ 2
                maze_values[cell_y, cell_x] = 2
            else:
                if len(neighbours) == 1:
                    new_y, new_x = neighbours[0]
                else:
                    new_y, new_x = neighbours[np.random.randint(0, len(neighbours) - 1)]
                stack_cells.append([new_y, new_x])
        else:
            stack_cells.pop()

    #Rysowanie labiryntu
    maze[0][0].left_side = 0  # wejscie
    maze[y_length - 1][x_length - 1].right_side = 0  # wyjscie
    for i in range(0, y_length, 2):
        for j in range(x_length):
            curr_cell = maze[i][j]
            draw_decagon(curr_cell, radius)

    #Rysowanie drogi
    if rysuj_droge:
        start_point = maze[start_y][start_x].get_pos()
        start_point_outside = start_point.copy()
        start_point_outside[1] -= radius * 1.5
        end_point = maze[finish_y][finish_x].get_pos()
        end_point_outside = end_point.copy()
        end_point_outside[1] += radius * 1.5
        ax.plot([start_point[1], start_point_outside[1]], [start_point[0], start_point_outside[0]], 'b--')
        for i in range(len(stack_cells) - 1):
            point1 = maze[stack_cells[i][0]][stack_cells[i][1]].get_pos()
            point2 = maze[stack_cells[i+1][0]][stack_cells[i+1][1]].get_pos()
            ax.plot([point1[1], point2[1]], [point1[0], point2[0]], 'b--')
        ax.plot([end_point[1], end_point_outside[1]], [end_point[0], end_point_outside[0]], 'b--')
        ax.plot(start_point_outside[1], start_point_outside[0], 'ro')
        ax.plot(end_point_outside[1], end_point_outside[0], 'rx')



fig, ax = plt.subplots(figsize=(8, 8))
fig.suptitle("Decagonalny labirynt")
create_maze(8, 8, True)

plt.show()
