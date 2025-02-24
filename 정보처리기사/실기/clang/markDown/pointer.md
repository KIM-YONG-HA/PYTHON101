# 포인터(Pointer)

정보처리 시험에서 좌절을 맛보게하는 포인터에 대해서 정리함. 

<br>

## 포인터란?

* 메모리 주소를 직접 다룰 수 있는 C언어의 강력한 기능

<br>

## 포인터 왜 쓰는지? 

* 동적 메모리 할당 후 해제 가능
* 배열 요소에 쉽게 접근 및 조작 가능 
* 함수에서 참조호출(Call by Reference)
함수 호출시 값을 복사하지 않고 직접 변수의 주소를 전달하여 성능향상 
구초제같은 큰 데이터를 복사하는 대신 포인터 사용하면 효율적이다 

* 문자열은 문자배열이므로 포인터로 쉽게 조작
* 구조체 포인터를 사용하면 메모리 절약 및 성능 향상 
* 함수 포인터 : 함수를 가리키는 포인터를 사용하면 함수를 동적으로 할당 가능 


※ 포인터를 사용하면 메모리 관리, 성능 최적화, 코드 효율성을 높일 수 있다고 함...

<br>


## 포인터 어떻게 쓰는지?

> 자료형* 변수명 | 자료형 *변수명 

### *(애스터리스트, asterisk) 위치 

애스터리스크는 포인터 타입을 나타내는 연산자로 타입 뒤에 또는 변수 앞에 붙인다. 


※ 스타일의 차이이므로 다중선언일 때만 주의깊게 볼 것.    
※ 변수 출력시 애스터리스크가 붙고 안붙고의 차이만 기억할 것.

``` c
int* ptr; // 포인터임을 강조 
int *ptr; // 변수와 가깝게 

int* p1, p2; // p1만 포인터
int *p1, *p2; // p1, p2 포인터 
```

### &(앰퍼샌드, ampersand)

주소 연산자로 사용되며, 변수의 메모리 주소를 가져오는 역할한다.

``` c 
#include <stdio.h>

int main() {
    int a = 10;
    printf("a의 값: %d\n", a);   // 변수 값 출력
    printf("a의 주소: %p\n", &a); // 변수의 주소 출력
    return 0;
}

```
※ 포인터 선언시 애스터리스크를 사용하고 주소 참조시 &을 사용   
※ 배열은 int *ptr = arr, int *ptr = &arr[0] 사용    





``` c
int* ptr;
int *ptr;
```
``` c 
#include <stdio.h>
int main(){

    int age = 30; // 변수 선언
    int *ptr = &age; // 포인터 선언, 변수의 주소값 참조

}
```



## 포인터 문제의 함정 

### 유형1. 포인터에 배열 저장 

``` c
#include <stdio.h>

int main() {
    int arr[3] = {1, 2, 3};
    int *ptr = arr;  // arr 자체가 첫 번째 요소의 주소

    printf("arr[0]의 주소: %p\n", ptr);
    printf("arr[1]의 주소: %p\n", ptr + 1); // 다음 요소의 주소

    printf("arr[0] 값: %d\n", *ptr); // 1
    printf("arr[0] + 1 값 : %d\n", *ptr + 1); // 값 + 1 = 2

    return 0;
}

```
``` c
int *ptr = arr;
```
``` c
int *ptr = &arr[0];
```

※ *ptr에 arr을 저장하면 arr[0]의 주소 값이 저장된다. 따라서 &arr[0]과 같다 
※ 주소 값을 출력하려면 ptr을 사용하고, 값을 출력하려면 *ptr을 사용한다.
※ 출력시 변수 앞에 *가 붙어 있다면 값이다!



### 유형2. 포인터의 연산 

주소값을 연산하는지, 배열의 원소값을 연산하는지, 배열의 인덱스를 연산하는지 
헷갈리게 나오는 경우가 있다. 


C언어 메모리 주소의 값은 16진수이고 0x7ffeefbff5a0 이런 형태로 출력이 된다. 
문제에서 편의상 주소를 1000이라하고 +1, +2를 묻는 경우가 있는데 

char 1바이트
int 4바이트
double 8바이트 









* 배열의 값에서 연산
* 배열의 인덱스 값을 연산
* 주소의 값을 연산 









## malloc(), free() 함수 

### malloc() : 메모리 할당 

* memory allocation의 약자(메모리 할당)

* Heap 영역에서 메모리를 할당하고 해당 메모리 주소 반환함
* 할당된 메모리 공간은 초기화되지 않음(쓰레기값 포함가능)

> 함수 원형

``` c 
void *malloc(size_t size);
```
* `size_t size` : 할당 메모리 크기(byte)
* `void*`타입을 반환하므로 형변환 하여 사용해야함

``` c
#include <stdio.h>
int main() {
    int *ptr = (int *)malloc(sizeof(int));  // 정수형 크기만큼 메모리 할당
    if (ptr == NULL) {  // 메모리 할당 실패 확인
        printf("메모리 할당 실패!\n");
        return 1;
    }

    *ptr = 42;  // 동적 할당된 메모리에 값 저장
    printf("값: %d\n", *ptr);

    free(ptr);  // 사용한 메모리 해제
    return 0;
}

```



### free() : 메모리 해제 

malloc(), calloc(), realloc()으로 할당된 메모리를 해제함 
메모리 해제 후 포인터는 여전히 주소를 가지고 있으므로 NULL로 초기화하는 것이 안전 

함수 원형 
``` c
void free(void *ptr);
```
`ptr` : 해제할 메모리의 포인터 


``` c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int *)malloc(5 * sizeof(int));  // 정수 5개 크기의 배열 할당
    if (arr == NULL) {
        printf("메모리 할당 실패!\n");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        arr[i] = i + 1;
    }

    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr);  // 메모리 해제
    arr = NULL; // dangling pointer 방지

    return 0;
}

```


## 주의사항 

* 메모리 누수 : malloc()으로 할당한 메모리를 free()로 해제하지 않으면 메모리 누수 발행 
프로그램이 실행되는 동안 점점 더 많은 메모리 차지하게 됨 

* 해제된 메모리 접근(Dangling Pointer) : free()한 메모리를 다시 사용하면 
정의되지 않은 동작(undefined behavior)이 발생 되므로 free(ptr) 후 ptr = NULL;로 초기화 

* 연속된 malloc()호출 시 메모리 부족 가능하며 NULL을 반환함 
* 항상 NULL 체크 후 사용해야한다 
* 동적메모리 할당시 초기화되지 않음 : malloc()은 쓰레기 값을 가진 메모리를 반환하므로 초기화가 필요하면
calloc() 사용할 수도 있음 




