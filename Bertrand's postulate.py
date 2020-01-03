N = 123456 * 2 + 1
tlist = [True]*N                            # 크기가 N인 리스트를 만들어 모두 True를 넣어준다

for i in range(2,round(N**0.5)+1) :         # 제곱근까지만 반복해서 시간 단축
    if tlist[i]==True :                     # 리스트 안의 값이 True이면
        for j in range(i*2,N,i):            # 그 값의 배수들을 모두 False로 바꿔준다(에라토스테네스의 체)
            tlist[j]=False


def prime_check(val):                       # 소수 판별 및 개수 세는 함수
    count = 0
    for i in range(val+1,val*2+1):
        if tlist[i]==True :
            count += 1
    print(count)

while True:
    v = int(input())
    if v == 0 :
        break
    prime_check(v)
