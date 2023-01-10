#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * is_palindrome - Function to check if a singly linked list is a palindrome
 * @head: argument
 * Return: value
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (1);
	}

	/*find the middle of the list*/
	struct ListNode *slow = head;
	struct ListNode *fast = head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

    /*reverse the second half of the list*/
	struct ListNode *prev = NULL;
	struct ListNode *curr = slow->next;

	while (curr != NULL)
	{
		struct ListNode *temp = curr->next;

		curr->next = prev;
		prev = curr;
		curr = temp;
	}
	slow->next = prev;

    /*compare the first and second halves of the list*/
	while (head != slow)
	{
		if (head->val != slow->val)
		{
			return (0);
		}
		head = head->next;
		slow = slow->next;
	}
	return (1);
}
