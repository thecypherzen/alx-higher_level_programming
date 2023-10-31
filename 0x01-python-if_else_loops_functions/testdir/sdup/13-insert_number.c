#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a
 * sorted singly linked list.
 * @head: list head ptr
 * @number: number to insert
 * Return: ptr the new node on success. NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *prev = NULL, *new_node;

	/* if head is NULL or malloc fails, return NULL */
	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);


	/* straighten out a looping node (if there is)*/
	temp = get_loop(*head);
	if (temp)
	{
		printf("looping node: %p\n", (void *)temp);
		temp->next = NULL;
	}

	/* insert the new node */
	new_node->n = number;
	if (*head == NULL)
	{
		printf("head == null");
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		temp = *head;
		while (temp && (temp->n <= number))
		{
			/*printf("inside loop\n");*/
			prev = temp, temp = temp->next;
			/*printf("prev: %i, temp: %i\n", prev->n, temp->n);*/
			/*sleep(1); */
		}
		new_node->next = temp;
		if (prev)
			prev->next = new_node;
		else
			*head = new_node;
	}
	return (new_node);
}
/**
 * get_loop - gets the address of looping node
 * @head: ptr to head of list
 * Return: address of looping node if found. NULL if not found
 */
listint_t *get_loop(listint_t *head)
{
	listint_t *fast, *slow, *l_node = NULL;
	int found = 0;

	if (!head || !(head->next))
		return (NULL);
	slow = head, fast = head;
	while (fast && fast->next)
	{
		l_node = fast, slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			slow = head, found = 1;
			while (slow != fast)
				slow = slow->next, fast = fast->next;
			l_node->next = NULL;
			break;
		}
		if (!found)
			l_node = NULL;
	}
	return (l_node);
}
