"""
Name: Vu Van Phong
MSSV: 19020392
Class: K64J
"""


import sys
import math
from collections import deque

# Encode by direction
# ['N', 'W', 'S', 'E']
D_ROW = [-1, 0, 1, 0]
D_COL = [0, -1, 0, 1]
DIRECTION = 'NWSE'


def read_list_int(st):
    tmp = st.strip().split(' ')
    return [int(x.strip()) for x in tmp]


def is_inside(x, y, N):
    return (0 <= x) and (x < N) and (0 <= y) and (y < N)


def read_input(input_file):
    """

    :param input_file:
    :return:
        N, vmax, (x_start, y_start), (x_goal, y_goal), A
    """

    with open(input_file, "r") as f:
        N, n_walls, vmax = read_list_int(f.readline())
        x_start, y_start, x_goal, y_goal = read_list_int(f.readline())

        # Use bit
        A = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]

        for i in range(n_walls):
            x1, y1, x2, y2 = read_list_int(f.readline())
            for k in range(4):
                if (x1 + D_ROW[k] == x2) and (y1 + D_COL[k] == y2):
                    A[x1][y1][k] = 1
                    if k % 2 == 0:
                        A[x2][y2][2 - k] = 1
                    else:
                        A[x2][y2][4 - k] = 1

                    break

    return N, vmax, (x_start, y_start), (x_goal, y_goal), A


def next_position(x0, y0, d, v, A, N):
    """

    :param x0:
    :param y0:
    :param d: moving direction, ['N', 'W', 'S', 'E']
    :param v: speed
    :param A: store wall information
    :return:
        x1, y1:
        if invalid move (collision) return -1, -1
    """
    x1 = x0
    y1 = y0

    # Move along d, v step
    # return -1 -1 if cat not
    for i in range(v):
        if not is_inside(x1, y1, N):
            return -1, -1

        if A[x1][y1][d] == 0:
            x1 += D_ROW[d]
            y1 += D_COL[d]
        else:
            return -1, -1

    return x1, y1


def turn_left(d):
    return (d + 3) % 4


def turn_right(d):
    return (d + 1) % 4


def process(input_file):

    N, vmax, start, goal, A = read_input(input_file)

    # Encode: x, y, direction, v, step, cost
    Q = deque([(start[0], start[1], 0, 0, 0, 0)])
    visited = set([(start[0], start[1], 0, 0)])
    count_nodes = 0

    while len(Q) > 0:
        u = Q.popleft()

        x = u[0]
        y = u[1]
        d = u[2]
        v = u[3]

        step = u[4]
        cost = u[5]
        count_nodes += 1
        if v == 0:
            if (x, y, turn_left(d), v) not in visited:
                visited.add((x, y, turn_left(d), v))
                Q.append((x, y, turn_left(d), v, step + 1, cost + 1))

            if (x, y, turn_right(d), v) not in visited:
                visited.add((x, y, turn_right(d), v))
                Q.append((x, y, turn_right(d), v, step + 1, cost + 1))

            x3, y3 = next_position(x, y, d, v+1, A, N)
            if is_inside(x3, y3, N):
                if (x3, y3, d, v+1) not in visited:
                    visited.add((x3, y3, d, v+1))
                    Q.append((x3, y3, d, v+1, step + 1,
                             cost + 1 + math.sqrt(v+1)))
                    # Check if (x3, y3) is the goal
                    if (x3, y3) == goal:
                        return step + 1, count_nodes, cost + 1 + math.sqrt(v+1)
        else:
            x1, y1 = next_position(x, y, d, v, A, N)
            # Add the remaining code here
            if is_inside(x1, y1, N):
                if (x1, y1, d, v) not in visited:
                    visited.add((x1, y1, d, v))
                    Q.append((x1, y1, d, v, step + 1, cost + 1 + math.sqrt(v)))

                    if (x1, y1) == goal:
                        return step + 1, count_nodes, cost + 1 + math.sqrt(v)

            if v > 0:
                x2, y2 = next_position(x, y, d, v-1, A, N)
                if is_inside(x2, y2, N):
                    if (x2, y2, d, v-1) not in visited:
                        visited.add((x2, y2, d, v-1))

                        Q.append((x2, y2, d, v-1, step + 1,
                                 cost + 1 + math.sqrt(v-1)))
                        if (x2, y2) == goal:
                            return step + 1, count_nodes,  cost + 1 + math.sqrt(v-1)

            if v < vmax:
                x3, y3 = next_position(x, y, d, v+1, A, N)
                if is_inside(x3, y3, N):
                    if (x3, y3, d, v+1) not in visited:
                        visited.add((x3, y3, d, v+1))
                        Q.append((x3, y3, d, v+1, step + 1,
                                 cost + 1 + math.sqrt(v+1)))

                        if (x3, y3) == goal:
                            return step + 1, count_nodes, cost + 1 + math.sqrt(v+1)

    return -1, -1, -1


if __name__ == "__main__":

    result = process(input_file=sys.argv[1])
    print('Total = ', result[1])
    print('N steps = ', result[0])

    # Q1. Compute the cost
    print('Cost = ', result[2])
