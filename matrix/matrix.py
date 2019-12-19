from re import sub


def matrix(M, N, lines):
    chars = [""] * (M*N)
    for index, line in enumerate(lines):
        for jndex, char in enumerate(line):
            chars[jndex * N + index] = char
    combined = "".join(chars)
    return sub(r'(?<=[a-zA-Z_0-9])[^a-zA-Z_0-9]+(?=[a-zA-Z_0-9])', " ", combined)


if __name__ == "__main__":
    N, M = [int(i) for i in input().split()]
    lines = [input() for _ in range(N)]
    print(matrix(M, N, lines))
