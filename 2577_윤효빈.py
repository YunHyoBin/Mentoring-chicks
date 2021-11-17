A = int(input())
B = int(input())
C = int(input())
N = A * B * C
print(N)
X = list(str(A * B * C))

for i in range(10):
    print(X.count(str(i)))

    