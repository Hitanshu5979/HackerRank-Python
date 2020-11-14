if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    high = max(scores)
    while (high == max(scores)):
        scores.remove(max(scores))
    print(max(scores))