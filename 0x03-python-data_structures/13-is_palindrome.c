#include "lists.h"
#include <stddef.h>

/**
 * palindrome - utility for is_palindrome
 *
 * @list: pointer to a pointer to the singly linked list
 * @list2: pointer to the singly linked list
 *
 * Return: 1 if palindrome
 *	   0 if not
 */
int palindrome(listint_t **list, listint_t *list2)
{
	int res = 0;

	if (list2 == NULL)
		return (1);

	if (palindrome(list, list2->next) && ((*list)->n == list2->n))
		res = 1;

	*list = (*list)->next;

	return (res);
}

/**
 * is_palindrome - Check if a giving singly linked list is a palindrome
 * @head: Adress to the givin list
 *
 * Return: 0 if it is not a palindrome
 *	   1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	return (palindrome(head, *head));
}
