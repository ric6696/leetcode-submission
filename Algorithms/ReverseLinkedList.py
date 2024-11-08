import sys

from LinkedList import listToLinkedList, printLinkedList


def reverseList(head):
    if not head or not head.next:
        return head

    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


def main():
    head = [1, 2, 3, 4, 5]
    head = listToLinkedList(head)
    printLinkedList(reverseList(head))


if __name__ == "__main__":
    sys.exit(main())
