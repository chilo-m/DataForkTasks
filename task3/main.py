def largest_rectangle(n, m, a, b):
    answer = 0
    minH = 0
    maxH = 0
    for h in a:
        if h in b:
            if h > maxH: 
                maxH = h
            if minH == 0:
                minH = h
            if h < minH:
                minH = h
    if minH*maxH != 0:
        answer = maxH - minH
    return answer
    # Write your code here
    

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    out = largest_rectangle(n, m, a, b)
    print(out)