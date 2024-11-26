def is_group_word(word):
    seen = set()  # 이미 등장한 문자를 저장할 집합
    prev_char = ''  # 이전 문자를 저장
    
    for char in word:
        if char != prev_char:  # 새로운 문자가 등장하면
            if char in seen:  # 이미 등장했던 문자라면 그룹 단어가 아님
                return False
            seen.add(char)  # 새로 등장한 문자를 추가
        prev_char = char  # 이전 문자 갱신
    
    return True  # 그룹 단어 조건을 만족하면 True 반환

# 입력 처리
n = int(input())  # 단어의 개수
count = 0

for _ in range(n):
    word = input()
    if is_group_word(word):
        count += 1

print(count)
