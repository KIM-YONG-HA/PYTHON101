#include <stdio.h>
int main(){
    

    // char* p = "KOREA";
    // printf("%s\n ", p);
    // printf("%s\n ", p+1);
    // printf("%c\n ", *p);
    // printf("%c\n ", *(p+3));
    // printf("%c\n ", *p+4);

    // int a = 10;
    // printf("aï¿½ï¿½ ï¿½ï¿½: %d\n", a);   // ï¿½ï¿½ï¿½ï¿½ ï¿½ï¿½ ï¿½ï¿½ï¿?
    // printf("aï¿½ï¿½ ï¿½Ö¼ï¿½: %p\n", &a); // ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ ï¿½Ö¼ï¿½ ï¿½ï¿½ï¿?


    int a = 10;
    int *p1 = &a;
    printf("a Ãâ·Â : %d\n", a);
    printf("&a Ãâ·Â : %p\n", &a);
    printf("&a+1 Ãâ·Â : %p\n", &a+1);

    printf("*p1 Ãâ·Â : %d\n", *p1);
    printf("*p1+1 Ãâ·Â : %d\n", *p1+1);

    int arr[2][2] = {{1,2},{3,4}};
    int *p2 = arr;

    printf("*p2 Ãâ·Â : %d\n", *p2);

}
