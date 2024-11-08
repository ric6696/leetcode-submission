import sys

from LinkedList import listToLinkedList, printLinkedList


def removeNthFromEnd(head, n):
    def reverseList(head):
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # reversed list
        rev = prev
        return rev

    rev = reverseList(head)
    cnt = 1
    prev, cur = None, rev
    while cur:
        if n == 1:  # head
            rev = rev.next
            break
        elif cnt == n:
            prev.next = cur.next
        prev = cur
        cur = cur.next
        cnt += 1
    rev = reverseList(rev)
    return rev


def main():
    head = [1, 2, 3]
    head = listToLinkedList(head)
    n = 1
    printLinkedList(removeNthFromEnd(head, n))


if __name__ == "__main__":
    sys.exit(main())
