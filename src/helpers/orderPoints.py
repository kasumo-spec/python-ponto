from datetime import datetime

def order_times_by_month(list_points):
    points_list = list_points
    points_list.sort(key=lambda date: datetime.strptime(date, '%d%m%Y%H%M%S'))
    organized_points = {}
    for point in points_list:
        if point[4:8] in organized_points.keys():
            if point[2:4] in organized_points[point[4:8]].keys():
                if point[:2] in organized_points[point[4:8]][point[2:4]].keys():
                    organized_points[point[4:8]][point[2:4]][point[:2]].append(point[8:])
                else:
                    organized_points[point[4:8]][point[2:4]][point[:2]] = [point[8:]]
            else:
                organized_points[point[4:8]][point[2:4]] = {}
                organized_points[point[4:8]][point[2:4]][point[:2]] = [point[8:]]
        else:
            organized_points[point[4:8]] = {}
            organized_points[point[4:8]][point[2:4]] = {}
            organized_points[point[4:8]][point[2:4]][point[:2]] = [point[8:]]

    
    return organized_points