import sys

input = sys.stdin.readline


def kmp(s):
    arr = [0 for _ in range(len(s))]
    j = 0
    answer = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = arr[j - 1]
        if s[i] == s[j]:
            j += 1
            arr[i] = j
            answer = max(answer, arr[i])

    return answer


if __name__ == '__main__':
    n = str(input().rstrip())
    ans = 0
    for i in range(len(n)):
        ans = max(ans, kmp(n[i:]))

    print(ans)