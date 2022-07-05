import os

def get_list_itens(folder):
    list_points = []
    for directory, subdirectory, points in os.walk(folder):
        for point in points:
            list_points.append(point[:-4])
    return list_points