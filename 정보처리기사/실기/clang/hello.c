#include <stdio.h>
int main(){
    

    // char* p = "KOREA";
    // printf("%s\n ", p);
    // printf("%s\n ", p+1);
    // printf("%c\n ", *p);
    // printf("%c\n ", *(p+3));
    // printf("%c\n ", *p+4);

    // int a = 10;
    // printf("a�� ��: %d\n", a);   // ���� �� ���?
    // printf("a�� �ּ�: %p\n", &a); // ������ �ּ� ���?


    int a = 10;
    int *p1 = &a;
    printf("a ��� : %d\n", a);
    printf("&a ��� : %p\n", &a);
    printf("&a+1 ��� : %p\n", &a+1);

    printf("*p1 ��� : %d\n", *p1);
    printf("*p1+1 ��� : %d\n", *p1+1);

    int arr[2][2] = {{1,2},{3,4}};
    int *p2 = arr;

    printf("*p2 ��� : %d\n", *p2);

}
