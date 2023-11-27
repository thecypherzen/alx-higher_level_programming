#include <stdio.h>

int main(void)
{
	int n = 6;
	printf("%d\n", (~n + 1) & n);
}