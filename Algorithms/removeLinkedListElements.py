import sys


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeLinkedListElements(nums, target):
    if not nums:
        return []

    previous = None
    current = nums

    while current:
        if current.val == target:
            if previous:
                previous.next = current.next
            else:
                nums = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return nums


def listToLinkedList(nums):
    dummy = current = ListNode(0)

    i = 0
    while i < len(nums):
        newNode = ListNode(nums[i])
        current.next = newNode
        current = current.next
        i += 1

    listnode = dummy.next
    dummy = None
    return listnode


def printLinkedList(nums):
    p = nums
    while p:
        print(p.val)
        p = p.next


def main():
    list = [1, 2, 3, 6, 4, 5, 6]
    target = 6
    nums = listToLinkedList(list)

    printLinkedList(nums)
    removeLinkedListElements(nums, target)
    printLinkedList(nums)
    return


if __name__ == "__main__":
    sys.exit(main())
