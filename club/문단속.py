# 트리구조로 들어가고 나오기전에 다시 체킹하고 나와야함.(음수값)

N = int(input())
list_door = list(map(int, input().split()))

used_doors = set()
opened_doors = set()
stack = []
i = 0
valid = True

while i < len(list_door):
    door = list_door[i]
    #추가
    if door >= 0:
        opened_doors.add(door)
        stack.append(door)
    else:
        #빼기
        if -door in opened_doors:
            # 스택의 마지막 문이 아니면 오류
            if stack[-1] != -door:
                valid = False
                break
            opened_doors.remove(-door)
            stack.pop()
    used_doors.add(abs(door))
    i += 1

# 남아있으면 오류
if opened_doors:
    valid = False

print('yes' if valid else 'no')
