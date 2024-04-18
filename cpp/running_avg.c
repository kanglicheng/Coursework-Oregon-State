#include <stdio.h>
/*
Dartmouth_IMTx DART.IMT.C.01
C Programming: Getting Started
Find the average of rolled numbers
Final project assessment
*/

int main(void) {
    
    int i;
    int t;
    scanf("%d", &t);
    int a, b, c;
    double avg;
    avg = 0;
    for(i = 0; i < t; i ++){
        scanf("%d%d%d", &a, &b, &c);
        avg = ((c*100+b*10+a) + avg*(i))/(i+1);
        printf("%d. you rolled: %d%d%d, current average: %.1lf\n", i+1, c, b, a, avg);
    }
    
    return 0;
}

