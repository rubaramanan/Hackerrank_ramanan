def get_average(student_marks: dict, keyword: str):
    if scores := student_marks.get(keyword):
        print(f"{sum(scores) / len(scores):.2f}")


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    get_average(student_marks,
                query_name)
