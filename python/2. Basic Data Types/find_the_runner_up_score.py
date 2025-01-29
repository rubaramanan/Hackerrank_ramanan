def get_runnerup(scores: list):
    unique_scores = sorted(set(scores))
    return unique_scores[-2]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(get_runnerup(arr))
