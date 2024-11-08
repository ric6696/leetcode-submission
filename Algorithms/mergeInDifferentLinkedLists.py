import sys

from LinkedList import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeInDifferent(list1, a, b, list2):
    prev, cur = None, list1
    l2cur = None
    cnt = 0
    while cur:
        prev = cur
        cur = cur.next
        cnt += 1
        if cnt == a:
            prev.next = list2
            l2cur = list2
            while l2cur and l2cur.next:
                l2cur = l2cur.next
        if cnt == b:
            l2cur.next = cur.next

    return list1


def main():
    list1, list2 = [0, 1, 2, 3, 4, 5, 6], [1000000, 1000001, 1000002, 1000003, 1000004]
    list1, list2 = listToLinkedList(list1), listToLinkedList(list2)
    a = 2
    b = 5
    resList = mergeInDifferent(list1, a, b, list2)
    printLinkedList(resList)
    return


if __name__ == "__main__":
    sys.exit(main())
