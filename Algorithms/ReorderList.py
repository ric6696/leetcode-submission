import sys

from LinkedList import listToLinkedList, printLinkedList


def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head.next:
        return head

    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    left, ldummy = head, head
    while ldummy:
        if ldummy.next == slow:
            ldummy.next = None
            break
        ldummy = ldummy.next

    revRight = slow

    lprev, lcur = None, left
    rprev, rcur = None, revRight
    while lcur:
        lprev = lcur
        lcur = lprev.next
        rprev = rcur
        rcur = rprev.next

        lprev.next = rprev
        if lcur:
            rprev.next = lcur
        else:
            break

    return left


def main():
    head = [1, 2, 3, 4, 5]
    head = listToLinkedList(head)

    printLinkedList(reorderList(head))


if __name__ == "__main__":
    sys.exit(main())
