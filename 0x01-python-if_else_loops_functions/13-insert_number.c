#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to the head pointer
 * @number: the number we want to insert
 * Return: the address of the new node ro NULL if failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (temp != NULL && temp->next != NULL)
	{
		if (number > temp->n && number < temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		else if (number < temp->n)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		else if (number == temp->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		else
		{
			temp = temp->next;
		}
	}
	temp = *head;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	return (add_nodeint_end(&temp, number));
}
