def get_second_lower(names: list, scores: list):
    max_score = sorted(list(set(scores)))[1]
    max_names = [names[index] for index, val in enumerate(scores) if val == max_score]
    return sorted(max_names)


if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    max_names = get_second_lower(names, scores)

    for name in max_names:
        print(name)
