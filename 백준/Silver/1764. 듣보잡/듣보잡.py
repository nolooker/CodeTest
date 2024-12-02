n, m = map(int, input().split())
heard = set()

# 듣도 못한 사람의 명단 입력
for _ in range(n):
    heard.add(input().strip())

# 보도 못한 사람의 명단 입력 및 교집합 계산
total = set()
for _ in range(m):
    name = input().strip()
    if name in heard:
        total.add(name)

# 결과 출력
result = sorted(total)
print(len(result))
for name in result:
    print(name)