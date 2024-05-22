import sys

input = sys.stdin.readline

alphabet = str(input().rstrip())

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in croatian:
    alphabet = alphabet.replace(char, '0')

print(len(alphabet))