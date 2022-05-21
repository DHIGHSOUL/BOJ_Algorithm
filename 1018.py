# Brute-Force

n, m = map(int, input().split()) # m*n 정수 입력
chess = [] # 보드의 무늬(문자열)을 입력받을 리스트 생성
for i in range(n): # n(높이)만큼 문자열을 입력받아
    chess.append(input()) # chess 리스트에 할당함(append)
startColor = [] # 시작 무늬에 따른 무늬 변경횟수를 저장할 startColor 리스트 생성

for i in range(n-7):
    for j in range(m-7): # 보드를 8*8 크기로 만듬(n-7 = 0~7의 인덱스를 가짐)
        white = 0
        black = 0 # 보드의 왼쪽 위의 시작점부터 변경해야 하는 무늬를 기록하기 위한 변수 생성
        for a in range(i, i+8):
            for b in range(j, j+8): # 0~7의 인덱스(8*8)를 체크함
                if(a+b)%2==0: # 짝수 인덱스 위치에 있을 때
                    if chess[a][b]!='W': # 흰색 무늬가 아니면
                        white+=1 # 무늬를 변경해야 하므로 white를 1 증가
                    else: # 반대로 흑색 무늬가 아니면
                        black+=1 # 무늬를 변경해야 하므로 black을 1 증가
                else:
                    if chess[a][b]!='B':
                        white+=1
                    else:
                        black+=1 # 홀수 인덱스 위치에 있을 때도 흰색/흑색에 따라 체크
        startColor.append(white) # 흰색 무늬로 시작했을 때 변경횟수를 리스트에 저장
        startColor.append(black) # 흑색 무늬로 시작했을 때 변경횟수를 리스트에 저장
print(min(startColor)) # 리스트에 있는 변경횟수 중 최소값을 출력