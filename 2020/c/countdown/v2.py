T = int(input().strip())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    k = K
    for num in A:
        if num == k:
            if k == 1:
                count += 1
                k = K
            else:                
                k -= 1
        elif num == K:
            k = K - 1
        else:
            k = K
    print(f"Case #{t}: {count}")
