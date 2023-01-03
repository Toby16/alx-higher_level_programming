#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Function to unsert node in a sorted list
 * @head: pointer to pointer argument | accepts the node
 * @number: integer value to be added and sorted into the list
 * Return: --value--
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *temp = NULL;

	if (newnode == NULL)
	{
		return (NULL);
	}
	else
	{
		newnode->n = number;
		newnode->next = NULL;
	}

	temp = *head;
	while (temp->next != NULL && (temp->next->n < newnode->n))
	{
		temp = temp->next;
	}

	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
