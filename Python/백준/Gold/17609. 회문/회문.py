import sys

input = sys.stdin.readline


def isPalindrome(s):
    s_idx, e_idx = 0, len(s) - 1
    cnt = 0
    while s_idx < e_idx:
        if s[s_idx] == s[e_idx]:
            s_idx, e_idx = s_idx + 1, e_idx - 1
            continue
        if s[s_idx] != s[e_idx]:
            if s[s_idx] == s[e_idx - 1]:
                temp = s[:e_idx] + s[e_idx + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            if s[s_idx + 1] == s[e_idx]:
                temp = s[:s_idx] + s[s_idx + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2

    return cnt


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        stmt = str(input().rstrip())
        if len(stmt) == 2:
            print(1)
        else:
            print(isPalindrome(stmt))
