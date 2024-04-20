#include <stdio.h>
int main(void) {
    // + - * / % : arithmetic operations
    // <  >  <=  >=  !=  ==  :  comparison operations
    double a;
    double b;
    scanf("%lf", &a);
    scanf("%lf", &b);
    int result;
   
    result = a + b;

    if(result >= 10 ){
        printf("Special Tax\n");
        printf("%d", 36);
    }else{
        result = result * 2;
        printf("Regular Tax\n");
        printf("%d", result);
    }
    return 0;
}