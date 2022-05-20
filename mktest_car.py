import sys
import random

if __name__ == "__main__":

    input_file = sys.argv[1]
    N = 100
    n_walls = 3000
    v_max = 10
    random.seed(1)

    with open(input_file, 'w') as f:
        f.write('%i %i %i\n' % (N, n_walls, v_max))
        f.write('%i %i %i %i\n' % (0, 0, N-1, N-1))
        for t in range(n_walls):
            # (x, y) can belongs to edge
            x = random.randint(0, N-1)
            y = random.randint(0, N-1)
            # direction can not make the second point get outside the map
            possible_points = []
            for i in range(4):
                if (i == 0 and x != 0):
                    possible_points.append(0)
                if (i == 1 and x != N-1):
                    possible_points.append(1)
                if (i == 2 and y != 0):
                    possible_points.append(2)
                if (i == 3 and y != N-1):
                    possible_points.append(3)
            k = possible_points[int(random.random() * len(possible_points))]
            if k == 0:
                x1 = x - 1
                y1 = y

            if k == 1:
                x1 = x + 1
                y1 = y

            if k == 2:
                x1 = x
                y1 = y - 1

            if k == 3:
                x1 = x
                y1 = y + 1
            f.write('%i %i %i %i\n' % (x, y, x1, y1))
