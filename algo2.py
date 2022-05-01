
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for i, r in enumerate(id_list):
        print(i)
        if reports[r] >= k:
            answer[i] += 1

    return answer


print(solution(id_list, report, k))
