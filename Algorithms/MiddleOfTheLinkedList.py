import sys

from LinkedList import listToLinkedList, printLinkedList


def middleNode(head):
    cur, skip, prev = head, None, head
    while cur and cur.next:
        skip = cur.next
        cur = skip.next
        prev = prev.next
    return prev


def middleNodeBetterSolution(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    head = [1, 2, 3, 4, 5, 6]
    head = listToLinkedList(head)
    printLinkedList(middleNodeBetterSolution(head))


if __name__ == "__main__":
    sys.exit(main())
