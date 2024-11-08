import sys

from LinkedList import listToLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPanlindrome(head):
    slow, fast, prev = head, head, None

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    prev, slow, prev.next = slow, slow.next, None

    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    fast, slow = head, prev

    while slow:
        if fast.val != slow.val:
            return False
        fast, slow = fast.next, slow.next
    return True


def main():
    head = [1, 2, 2, 1]
    head = listToLinkedList(head)
    print(isPanlindrome(head))


if __name__ == "__main__":
    sys.exit(main())
