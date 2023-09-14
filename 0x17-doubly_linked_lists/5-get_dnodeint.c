#include "lists.h"

/**
 * get_dnodeint_at_index - get node at a certian index
 * @head: is a list pointer
 * @index: to be added at
 * Return: data of that node
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *temp = head;
	unsigned int count = 0;

	if (head == NULL)
		return (NULL);
	while (count < index && temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	if (temp == NULL)
		return (NULL);
	return (temp);
}
