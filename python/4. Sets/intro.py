def average(array):
    # your code goes here
    array = list(set(array))
    # print(len(array))
    average = sum(array) / len(array)
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
