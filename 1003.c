#include <stdio.h>

int zero[41], one[41]; // Memoization을 할 전역변수 배열(전역변수이기에 자동으로 초기화됨)

void fibonacci(int n) {
    if(n == 0) { // n이 0이면
        zero[n] = 1;
        one[n] = 0;
    } else if(n == 1) { // n이 1이면
        zero[n] = 0;
        one[n] = 1;
    } else if(zero[n] == 0 && one[n] == 0) { // n의 피보나치 함수 연산값이 없다면
        fibonacci(n-2); // 재귀호출로 하위 인덱스를 채워나감(메모이제이션)
        fibonacci(n-1);
        zero[n] = zero[n-1] + zero[n-2]; // 해당 n값의 연산값을 메모이제이션
        one[n] = one[n-1] + one[n-2];
    }
}

int main() {
    int T = 0, N = 0;

    scanf("%d", &T); // 테스트 횟수를 입력받음

    for(int i=0; i<T; i++) { // 입력받은 횟수만큼 테스트를 반복
        scanf("%d", &N); // 테스트할 정수를 입력받음
        
        fibonacci(N); // 테스트할 정수를 피보나치 함수에 전달

        printf("%d %d\n", zero[N], one[N]); // 0과 1이 나오는 수만큼 출력(전역배열 내 N번째 요소의 값)
    }

    return 0;
}