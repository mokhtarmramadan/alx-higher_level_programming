#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle or not
 * @list: a pointer to a linked list
 * Return: 0 if not cycle 1 if cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *temp;
	int counter;

	temp = list;
	counter = 0;
	while (counter < 2)
	{
		if (temp == list)
		{
			counter++;
			temp = temp->next;
		}
		else if (temp == NULL)
		{
			return (0);
		}
		else
		{
			temp = temp->next;
		}
	}
	return (1);
}
