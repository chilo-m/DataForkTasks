def maximum(s, t):
    answer = 0
    dictS = {}
    dictT = {}
    for letter in s:
        if dictS.get(letter) is not None:
            newVal = dictS.get(letter) + 1
            dictS[letter] = newVal
        else:
            dictS[letter] = 1

    for letter in t:
        if dictT.get(letter) is not None:
            newVal = dictT.get(letter) + 1
            dictT[letter] = newVal
        else:
            dictT[letter] = 1
    for letter in dictS:
        if dictT.get(letter) is not None:
            answer += min(dictS.get(letter),dictT.get(letter))
    return answer
    # Write your code here


t = int(input())
for _ in range(t):
    s = input()
    t = input()

    out = maximum(s, t)
    print(out)