import sys

from LinkedList import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNodes(head):
    stack = []
    resList = ListNode(0)
    maxVal = 0
    cur = head

    while cur:
        stack.append(cur.val)
        cur = cur.next

    while stack:
        if stack[-1] >= maxVal:
            tmp = stack.pop()
            newNode = ListNode(tmp)
            if not resList.next:
                resList.next = newNode
            else:
                prev = resList.next
                resList.next = newNode
                newNode.next = prev

            maxVal = tmp
        else:
            stack.pop()

    return resList.next


def main():
    head = [5, 22, 6, 3, 8, 4]

    head = listToLinkedList(head)
    resList = removeNodes(head)
    printLinkedList(resList)


if __name__ == "__main__":
    sys.exit(main())
