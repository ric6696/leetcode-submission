import sys

from removeLinkedListElements import listToLinkedList, printLinkedList


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        previous = head
        current = head.next

        while current:
            if previous.val == current.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        printLinkedList(head)


def main():
    solution = Solution()

    nums = [1, 1, 2, 3, 3]
    # dummy = current = ListNode(0)

    # i = 0
    # while i < len(nums):
    #     newNode = ListNode(nums[i])
    #     current.next = newNode
    #     current = current.next
    #     i += 1

    # listnode = dummy.next
    # dummy = None

    listnode = listToLinkedList(nums)
    solution.deleteDuplicates(listnode)

    return 0


if __name__ == "__main__":
    sys.exit(main())
