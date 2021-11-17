N = int(input())
X = list(map(int, input().split()))
max = X[0]
min = X[0]
for i in list(X):
    if i > max:
        max = i
    elif i < min:
        min = i 

print(min,max)



    