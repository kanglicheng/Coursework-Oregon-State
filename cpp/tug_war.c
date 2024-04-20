#include <stdio.h>

int main(void)
{
    int numPlayers;
    scanf("%d", &numPlayers);
    int i, team1, team2;
    team1 = 0;
    team2 = 0;
    for (i = 0; i < numPlayers * 2; i++)
    {
        int temp;
        int flag = i % 2;
        scanf("%d", &temp);
        if (flag == 1)
        {
            team2 += temp;
        }
        else
        {
            team1 += temp;
        }
    }

    if (team1 > team2)
    {
        printf("Team 1 has an advantage\n");
    }
    else
    {
        printf("Team 2 has an advantage\n");
    }
    printf("Total weight for team 1: %d\n", team1);
    printf("Total weight for team 2: %d", team2);
}