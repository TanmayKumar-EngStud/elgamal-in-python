t = int(input())
ans = ''
Ns = []
As = []
for i in range(t):
    temp = []
    Ns.append(int(input()))
    temp=list(map(int, input().split(' ')))
    As.append(temp)
count = 0
print(0) # since the first object will always show 0 in the beginning.
for i in range(len(As)):
    for j in range(i):
        #first finding common start
        if As[i][0] == As[j][0]:
            for k in range(i):
                if As[i][len(As[i])-1] == As[k][len(As[k])-1] and k != j:
                    count= i -2
        elif As[j][len(As[j])-1] == As[i][len(As[i])-1]:
            for k in range(i):
                if As[i][0] == As[k][0] and k != j:
                    count = i -2
        if count !=i-2:
            count = -1
    print(count)