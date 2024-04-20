/*
Your program will read an integer (between 0 and 12) indicating the number of hours past noon of your arrival.
For example, 0 indicates a noon arrival, 1 a 1pm arrival, 12 a midnight arrival, etc. The base price is 10 dollars,
 and 5 dollars are added for every hour after noon. Thankfully the total is capped at 53 dollars,
 so you'll never have to pay more than that. Your program should print the price (an integer) you have to pay, given the input arrival time.
*/
#include<stdio.h>
int main(void) {
    int hour;
    scanf("%d", &hour);
    int price;
    price = 10 + 5*hour;
    if(price <= 53){
        printf("%d", price);
    }else{
        printf("%d", 53);
    }
};


#include <stdio.h>
int main2() {
    int arrivalHour = 0;
    scanf("%d", &arrivalHour);
    int total = 10+5*arrivalHour;
    int totalExceeds53 = total > 53;
    if(totalExceeds53){
        printf("53");
    }else{
        printf("%d", total);
    }
    return 0;
}