#include "lists.h"
/**
 * check_cycle - checks if a linked list loops
 * @list: the list head
 * Return: 0 if no loop, 1 if loop detected
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);
	slow = fast = list;
	while ((fast = fast->next->next))
	{
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
