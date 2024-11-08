import sys

from LinkedList import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateList(head, k):
    if not head:
        return None
    cnt = 0
    prev, cur = None, head
    while cur:
        prev = cur
        cur = cur.next
        cnt += 1
    tail = prev
    tail.next = head

    prev, cur = None, head
    for _ in range(cnt - k % cnt):
        prev = cur
        cur = cur.next
    head = cur
    prev.next = None

    return head


def main():
    head = [0, 1, 2]
    head = listToLinkedList(head)
    k = 3
    printLinkedList(rotateList(head, k))


if __name__ == "__main__":
    sys.exit(main())
