#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of linked list's head
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t is_pali = 1, list_len, i;
	int *list_vals;
	listint_t *temp;

	if (!head)
		return (!is_pali);
	list_len = get_list_len(*head);
	if (!list_len)
		return (is_pali);

	list_len = (list_len + 1) / 2;
	list_vals = malloc(sizeof(int) * list_len);
	if (!list_vals)
		return (is_pali = 0);
	temp = *head;
	for (i = 0; i < list_len; i++)
	{
		list_vals[i] = temp->n;
		temp = temp->next;
	}
	i = i % 2 ? i - 1 : i - 2;
	while (temp)
	{
		if (temp->n != list_vals[i])
		{
			is_pali = 0;
			break;
		}
		i--, temp = temp->next;
	}
	free(list_vals);
	return (is_pali);
}

/**
 * get_list_len - gets the length of a singly linked list
 * @head: pointer to list head
 * Return: the length or 0
 */
size_t get_list_len(listint_t *head)
{
	size_t len = 0;
	listint_t *temp;

	temp = head;
	while (temp)
		len++, temp = temp->next;
	return (len);
}
