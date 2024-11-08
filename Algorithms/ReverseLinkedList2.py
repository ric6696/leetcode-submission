import sys

from LinkedList import listToLinkedList, printLinkedList


def reverseBetween(head, left, right):
    revHead = head
    cur = head
    while cur:
        prev = cur
        cur = cur.next
    listTail = revTail = prev

    p, cnt = head, 1
    while p:
        if cnt == left:
            revHead = p
        elif cnt == right:
            revTail = p
        p = p.next
        cnt += 1

    if revTail.next:
        dummyHead = revTail.next
    else:
        dummyHead = None

    # Reverse Particular list
    prev = None
    cur = revHead
    while cur is not revTail:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    revTail.next = prev

    if head == revHead and listTail == revTail:
        return revTail
    elif head == revHead and listTail != revTail:
        revHead.next = dummyHead
        return revTail
    elif head != revHead and listTail == revTail:
        dummyHead = head
        while dummyHead.next != revHead:
            dummyHead = dummyHead.next
        dummyHead.next = None
        revHead.next = head
        return revTail
    else:
        dummyHead = head
        while dummyHead.next != revHead:
            dummyHead = dummyHead.next
        dummyHead.next = revTail
        revHead.next = listTail
        return head


def main():
    head = [1, 2, 3, 4, 5]
    head = listToLinkedList(head)
    left, right = 2, 4
    printLinkedList(reverseBetween(head, left, right))


if "__main__" == __name__:
    sys.exit(main())
