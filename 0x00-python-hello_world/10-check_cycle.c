#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 *
 * @list: The singly-linked
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *checklist, *her;

	if (list == NULL || list->next == NULL)
		return (0);

	checklist = list->next;
	her = list->next->next;

	while (checklist && her && her->next)
	{
		if (checklist == her)
			return (1);

		checklist = checklist->next;
		her = her->next->next;
	}

	return (0);
}
