coral_params = [
    [0.307692, -0.531469, -0.461538, -0.293706, 5.401953, 8.655175, 0.40],
    [0.307692, -0.076923, 0.153846, -0.447552, -1.295248, 4.152990, 0.15],
    [0.000000, 0.545455, 0.692308, -0.195804, -4.893637, 7.269794, 0.45]
]

def update_xy(x, y, p, params):
    pp = 0
    calc = lambda xi, yi, q, k: k[xi]*x + k[yi]*y + k[q]
    X = lambda k: calc(0, 1, 4, k)
    Y = lambda k: calc(2, 3, 5, k)
    for k in params:
        pp += k[-1]
        if p <= pp:
            return X(k), Y(k)
    return X(params[-1]), Y(params[-1])
