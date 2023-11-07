#include <stdio.h>

int main(void)
{
	int n = 5;

	if(__builtin_types_compatible_p(typeof(n), double))
    	printf("p is of type double!\n");
	if(__builtin_types_compatible_p(typeof(n), float))
    	printf("n is of type float!\n");
	else
		printf("n is not a float\n");
	if(__builtin_types_compatible_p(typeof(int), int))
    	printf("n is of type int!\n");
	else
    	printf("n is not of type int!\n");
	return (0);
}