// One room costs nothing if you are exactly 60 (the age of the innkeeper),
// or 5 dollars if you are less than 10 years old. For everyone else, the cost
// is 30 dollars plus an additional 10 dollars if you bring more than 20 pounds of luggage
// . Your program should read the customer's
// age first, then the weight of their luggage, then output the price they have to pay.

#include <stdio.h>
int main(void)
{
    int age, bagWeight;
    scanf("%d%d", &age, &bagWeight);
    if (age == 60)
    {
        printf("%d", 0);
    }
    if (age < 10)
    {
        printf("%d", 5);
    }
    if (age != 60 && age > 10)
    {
        if (bagWeight > 20)
        {
            printf("%d", 40);
        }
        else
        {
            printf("%d", 30);
        }
    }
};

#include <stdio.h>

int main2()
{
    int is60, isLessThan10, luggageMoreThan20;
    int age = 0;
    int luggageWeight = 0;

    scanf("%d %d", &age, &luggageWeight);

    is60 = age == 60;
    isLessThan10 = age < 10;
    luggageMoreThan20 = luggageWeight > 20;

    if (is60)
    {
        printf("0");
    }
    else
    {
        if (isLessThan10)
        {
            printf("5");
        }
        else
        {
            if (luggageMoreThan20)
            {
                printf("40");
            }
            else
            {
                printf("30");
            }
        }
    }
    return 0;
}