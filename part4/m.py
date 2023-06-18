T = int(input())

for _ in range(T+1):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))
    total_stones = sum(piles)

    if total_stones % 2 == 1:
        print("Bob\n")
    else:
        print("Alice\n")
