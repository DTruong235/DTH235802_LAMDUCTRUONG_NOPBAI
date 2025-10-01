# viết hàm ocillate(n) in Python để in ra hình: -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4 
def oscillate(n, m):
    if n > m:
        return
    for i in range(n, m):
        if i != 0:
            yield i
            yield -i
        else:
            yield 0

for n in oscillate(-3,5):
    print(n, end=' ')
print()
