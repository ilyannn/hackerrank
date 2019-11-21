from collections import defaultdict


def read_ints():
    return [int(s) for s in input().split()]


def max_sum(M, X):
    solutions = {0: []}

    for x in X:
        sqs = set()

        for v in x:
            sq = (v * v) % M
            if sq in sqs:
                continue
            sqs.add(sq)
            for s, l in solutions.copy().items():
                ssq = (s + sq) % M
                if ssq not in solutions.keys():
                    solutions[ssq] = l + [v]

    a = max(solutions.keys())

    return a, solutions[a]


if __name__ == "__main__":
    K, M = read_ints()
    X = [read_ints()[1:] for _ in range(K)]
    a, _ = max_sum(M, X)
    print(a)