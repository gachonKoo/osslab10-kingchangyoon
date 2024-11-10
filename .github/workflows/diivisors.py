import sys

number = int(sys.argv[1])

for i in range(1, number+1):  # 1부터 number까지 반복
    if number % i == 0:      # number를 i로 나누었을 때 나머지가 0이면
        print(i, end=" ")   # 약수를 공백으로 구분하여 출력

print()
