#include "lists.h"

/**
 * add_dnodeint -  adds a new node at the beginning
 * @head: a pointer to th head pointer
 * @n: data
 * Return: the address of the new node
 **/
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *temp = *head;
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->prev = NULL;

	if (temp == NULL)
	{
		new->next = NULL;
	}
	else
	{
		new->next = temp;
	}
	*head = new;
	return (new);
}
