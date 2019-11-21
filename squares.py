

def read_ints():
    return [int(s) for s in input().split()]


def max_sum(M, X):
    print(M, X)
    covers = set([0])

    for x in X:
        for s in covers.copy():
            for v in x:
                covers.add((s + v * v) % M)

    return max(covers)


if __name__ == "__main__":
    K, M = read_ints()
    X = [read_ints()[1:] for _ in range(K)]
    print(max_sum(M, X))