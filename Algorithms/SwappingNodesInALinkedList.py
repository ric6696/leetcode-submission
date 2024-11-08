import sys

from LinkedList import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head, k):
    kth = head
    for _ in range(k - 1):
        kth = kth.next
    slow, fast = head, kth
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.val, kth.val = kth.val, slow.val
    return head


def main():
    head = [1, 2, 3, 4, 5]
    k = 2
    head = listToLinkedList(head)
    printLinkedList(swapNodes(head, k))


if __name__ == "__main__":
    sys.exit(main())
