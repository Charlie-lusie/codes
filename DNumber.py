def Find(num):
    min_det = float('inf')
    min_N, min_M = 0, 0
    for i in range(1, 10001):
        result = i*num
        lower, upper = int(result), int(result) + 1
        det_lower, det_upper = abs(lower - result) / i, abs(upper - result) / i
        if det_upper < det_lower:
            det_lower = det_upper
            lower = upper
        if det_lower == 0:
            return lower, i
        det_lower = int(det_lower*10e14)
        if det_lower < min_det:
            min_det = det_lower
            min_M = lower
            min_N = i
    return min_M, min_N

print(Find(3.14159265358979))
