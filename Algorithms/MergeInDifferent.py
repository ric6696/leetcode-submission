import sys

from removeLinkedListElements import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeInDifferent(list1, a, b, list2):
    prev, cur = None, list1
    cnt = 1
    while cur:
        print(cur.val, cnt)
        prev = cur
        cur = cur.next
        cnt += 1
        if cnt == a:
            print(a)
        if cnt == b:
            print(b)

    return


def main():
    list1, list2 = [10, 1, 13, 6, 9, 5], [1000000, 1000001, 1000002]
    list1, list2 = listToLinkedList(list1), listToLinkedList(list2)
    a = 3
    b = 4
    print(mergeInDifferent(list1, a, b, list2))
    return


if __name__ == "__main__":
    sys.exit(main())
