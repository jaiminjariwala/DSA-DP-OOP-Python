import math
def closest_pair_of_points(points):
    n = len(points) # 4
    min_distance = float("inf")
    pair = None
    
    for i in range(n-1):            # 0, 1, 2
        for j in range(i+1, n):     # 1, 2, 3
            # euclidean distance d = sqrt((x1-x2)**2 + (y1-y2)**2)
            d = math.sqrt((points[i][0] - points[j][0])**2 +
                          (points[i][1] - points[j][1])**2)
                          
            if d < min_distance:
                min_distance = d
                pair = (points[i], points[j])
    
    return min_distance, pair
    
points = [(0,0), (1,1), (2,2), (5,5)]
dist, pair = closest_pair_of_points(points)
print(f"min distance: {dist}")
print(f"pair: {pair}")