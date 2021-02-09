from collections import OrderedDict

testcases = [[(1,5,10),(4,6,8),(10,15,10),(11,12,8)],
             [(1,10,4),(1,8,6),(1,6,8)],
             [(0,6,2),(5,10,8),(7,8,12)],
             [(1, 2, 8), (3, 6, 4), (3, 6, 10), (4, 7, 6), (5, 8, 12)]]

outputs = [[(1,10),(5,8),(6,0),(10,10),(15,0)],
          [(1,8),(6,6),(8,4),(10,0)],
          [(0,2), (5,8),(7,12),(8,8), (10,0)],
          [(1, 8), (2, 0), (3, 10), (5, 12), (8, 0)]]

def boundary(boxes):
    max_x = max(boxes, key=lambda x: x[1])[1] + 1
    hm = [(0,0,0)]*(max_x)
    pts = OrderedDict()
    
    for box in boxes:
        x1, x2, h = box
        for i in range(x1,x2+1):
            if hm[i][2] < h:
                hm[i] = box
    
    if hm[0][2] != 0:
        pts[0] = hm[0][2]

    for i in range(1, len(hm)):
        if hm[i-1][2] == hm[i][2]:
            if i == hm[i][1] :
                pts[i] = 0

        elif hm[i-1][2] < hm[i][2]:
           pts[i] = hm[i][2]

        else:
            pts[i-1] = hm[i][2]

    return [(x,y) for x,y in pts.items()]


for testcase, output in zip(testcases, outputs):
    my_op = boundary(testcase)
    try:
        assert my_op == output
    except AssertionError:
        print('Testcase :: ', testcase)
        print('Output :: ', output)
        print('My Output :: ', my_op)
    else:
        print('passed')