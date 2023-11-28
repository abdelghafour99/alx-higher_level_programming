#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Program insert a number
 *		 into a sorted singly-linked list
 * @head: Pointer to head of the linked list
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL
 *         Pointer to the node contain the number added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *checklist = *head, *her;

	her = malloc(sizeof(listint_t));
	if (her == NULL)
		return (NULL);
	her->n = number;

	if (checklist == NULL || checklist->n >= number)
	{
		her->next = checklist;
		*head = her;
		return (her);
	}

	while (checklist && checklist->next && checklist->next->n < number)
		checklist = checklist->next;

	her->next = checklist->next;
	checklist->next = her;

	return (her);
}
