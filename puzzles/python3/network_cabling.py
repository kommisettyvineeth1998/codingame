import math


if __name__ == "__main__":
    nb_buildings = int(input())
    cable_length = 0
    min_x = float("inf")
    max_x = 0
    y_coordinates = []

    for _ in range(nb_buildings):
        x, y = map(int, input().split())
        y_coordinates.append(y)
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

    # horizontal cable length
    cable_length += (max_x - min_x)
    
    # calculate y median to minimize vertical cable length(s)
    y_coordinates.sort()
    y_median = y_coordinates[nb_buildings // 2]
    
    # vertical cable(s) length
    for y in y_coordinates:
        cable_length += math.fabs(y_median - y)
    
    print(int(cable_length))
