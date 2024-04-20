#include <stdio.h>

int main(void)
{
    printf("Dear Procrastinator,\n You still have to wait for %d days (%d minutes or %d seconds) before you can procrastinate!",
           25 - 23, 2 * 24 * 60, 2 * 24 * 60 * 60);
}