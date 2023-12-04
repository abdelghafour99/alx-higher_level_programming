#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - Check if a giving singly linked list is a palindrome
 * @head: Adress to the givin list
 *
 * Return: 0 if it is not a palindrome
 *	   1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	listint_t *last_nod = *head, *pre = NULL;

	if (!head || !(*head))
		return (1);
	if (!(*head)->next)
		return (1);

	while (last_nod->next)
		last_nod = last_nod->next;

	while (cur)
	{
		if (pre)
		{
			while ((last_nod->next != pre) && last_nod->next)
				last_nod = last_nod->next;

			if (last_nod == cur)
				break;
		}

		if (last_nod->n == cur->n)
		{
			if (cur->next == last_nod)
				break;

			pre = last_nod;
			cur = cur->next;
			last_nod = cur;
		}
		else
			return (0);
	}
	return (1);
}
