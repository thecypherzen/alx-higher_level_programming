#include <stdio.h>
#include <sys/types.h>
#include <wait.h>
#include <unistd.h>


void pad_int(int val, int max_width, char *chrs);
/**
 * main - Entry point
 * Description goes here
 * Return: 0 always
 */
int main(void)
{
	int n, pid1, pid2, pid3, i, val;

	pid1 = fork();
	if (pid1 != 0)
		n = 16;
	else
	{
		pid2 = fork();
		if (pid2 != 0)
			n = 11;
		else
		{
			pid3 = fork();
			if (pid3 != 0)
				n = 6;
			else
				n = 1;
		}
	}
	if (pid1 != 0)
	{
		waitpid(pid1, NULL, 0);
		printf("parent(xxxx):\t");
	}
	if (pid2 != 0 && pid1 == 0)
	{
		waitpid(pid2, NULL, 0);
		printf("child2(%d):\t", pid2);
	}
	if (pid3 != 0 && pid1 == 0 && pid2 == 0)
	{
		waitpid(pid3, NULL, 0);
		printf("child3(%d):\t", pid3);
	}
	if (pid3 == 0)
	{
		printf("child4(0000):\t");
	}
	for (i = n; i < n + 5; i++)
	{
		printf("%d", i);
		if (i == n + 4)
			printf("\n");
		else
			pad_int(i, 3, " ");

	}
	return (0);
}

void pad_int(int val, int max_width, char *chrs)
{
	int val_width = 0, tmp = val, div = 10;

	while (tmp > 0)
	{
		val_width++;
		tmp /= div;
		div *= 10;
	}
	tmp = max_width - val_width;
	while (tmp--)
	{
		printf("%s", chrs);
	}
}
