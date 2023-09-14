#include "lists.h"

/**
 * print_dlistint -  prints all the elements of a dlistint_t list.
 * @h: the head pointer
 * Return: number of the nodes
 **/

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *temp = h;
	size_t counter = 0;

	while (temp != NULL)
	{
		printf("%d\n", temp->n);
		temp = temp->next;
		counter++;
	}
	return (counter);
}
