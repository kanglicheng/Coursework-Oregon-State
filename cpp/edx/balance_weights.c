/*
You are responsible for a rail convoy of goods consisting of several boxcars. You start the train and after
a few minutes you realize that some boxcars are overloaded and weigh too heavily on the rails while others
are dangerously light. So you decide to stop the train and spread the weight more evenly so that all
the boxcars have exactly the same weight (without changing the total weight). For that you write a program which
helps you in the distribution of the weight.

Your program should first read the number of cars to be weighed (integer) followed by the weights of the cars (doubles).
Then your program should calculate and display how much weight to add or subtract from each car such that every car has
the same weight. The total weight of all of the cars should not change.These additions and subtractions of weights should be
 displayed with one decimal place.

You may assume that there are no more than 50 boxcars.
*/
#include <stdio.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    double array[n];
    double readValue = 0.0;
    double total = 0.0;
    double avg = 0.0;
    int i = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%lf", &readValue);
        total = total + readValue;
        array[i] = readValue;
    }
    avg = total / n;
    for (i = 0; i < n; i++)
    {
        printf("%.1lf\n", avg - array[i]);
    }
    return 0;
}

int main2(void)
{
    int nbBoxCars, carNumber;
    double weights[50];
    double totalWeight = 0.0;
    double averageWeight;

    scanf("%d\n", &nbBoxCars);
    for (carNumber = 0; carNumber < nbBoxCars; carNumber = carNumber + 1)
    {
        scanf("%lf", &weights[carNumber]);
        totalWeight = totalWeight + weights[carNumber];
    }

    averageWeight = totalWeight / nbBoxCars;

    for (carNumber = 0; carNumber < nbBoxCars; carNumber = carNumber + 1)
    {
        printf("%.1lf\n", averageWeight - weights[carNumber]);
    }
    return 0;
}