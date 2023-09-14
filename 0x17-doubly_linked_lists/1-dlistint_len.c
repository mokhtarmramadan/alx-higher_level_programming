#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked
 * @h: The head of the list
 * Return: the number of elements in a linked
 **/
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *temp = h;
	size_t counter = 0;

	while (temp != NULL)
	{
		counter++;
		temp = temp->next;
	}
	return (counter);
}
