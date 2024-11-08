import sys

from LinkedList import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def doubleLinkedListNumber(head):
    # reverse Linked List
    prev, cur = None, head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    head = prev

    # Double Linked List
    doubleHead = ListNode(0)

    carry, num = 0, 0
    while head:
        num = (head.val * 2 + carry) % 10
        carry = (head.val * 2 + carry) // 10

        newNode = ListNode(num)
        if not doubleHead.next:
            doubleHead.next = newNode
        else:
            newNode.next = doubleHead.next
            doubleHead.next = newNode
        if not head.next and carry == 1:
            doubleHead.val = 1
            return doubleHead

        head = head.next
    return doubleHead.next


def main():
    head = [4]
    head = listToLinkedList(head)
    printLinkedList(doubleLinkedListNumber(head))


if __name__ == "__main__":
    sys.exit(main())
