#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * head: a pointer to the head pointer
 * number: the number we want to insert
 * Return: the address of the new node ro NULL if failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;
	temp = *head;
	
	while (temp != NULL && temp->next != NULL)
	{
		if (number > temp->n && number < temp->next->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);

			new->n = number;
			new->next = temp->next;
			temp->next = new;
			return (new);
			
		}
		else if (number < temp->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);

			new->n = number;
			new->next = *head;
			(*head)->next = new;
			return (new);
		}
		else
		{
			temp = temp->next;
		}
	}
	temp = *head;
	new = add_nodeint_end(&temp, number);
	return (new);
}
