import itertools


def get_permutations(x: int, y: int, z: int):
    i = list(range(0, x + 1))
    j = list(range(0, y + 1))
    k = list(range(0, z + 1))

    permutations = list(itertools.product(i, j, k))
    return permutations


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    permu = get_permutations(x, y, z)
    sort_permu = [list(i) for i in permu if sum(i) != n]
    print(sort_permu)
