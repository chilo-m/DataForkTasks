def solve(n, a):
    answer = True
    for i in range(1, n):
        if a[i] < i:
            answer = False
            break
    if answer:
        return "Yes"
    else:
        return "No"
    # Write your code here


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    out = solve(n, a)
    print(out)