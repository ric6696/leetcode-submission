import sys
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
