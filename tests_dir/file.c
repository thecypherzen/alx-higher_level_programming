#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char *msg  = malloc(1024), filename[] = "myfile.tx";
	int fd = open(filename,
	O_RDWR | O_CREAT  | O_APPEND, 00744);

	if (fd < 0)
		printf("Error opening file\n");
	msg = "My test file\n";
	write(fd, msg, strlen(msg));
	msg = "The day is bright and fair\n";
	write(fd, msg, strlen(msg));
	close(fd);
	return (0);
}