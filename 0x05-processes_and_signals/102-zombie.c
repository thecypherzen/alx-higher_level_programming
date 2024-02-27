#include "zombie.h"

int infinite_while(void);
/**
 * main - Entry point
 * Description goes here
 * Return: 0 always
 */
int main(void)
{
	int n = 0, pid;

	while (n < 5)
	{
		pid = fork();
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			n += 1;
		}
		else
			return (0);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - sleeps infintely
 * Return: void
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
