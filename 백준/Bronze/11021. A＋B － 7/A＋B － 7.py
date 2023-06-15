import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print('Case #'+str(i+1)+': ' + str(a+b))
        

if __name__ == "__main__":
    main()