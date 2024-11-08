import sys


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    tempList1 = list1
    tempList2 = list2

    resList = []
    while tempList1 is not None and tempList2 is not None:
        if tempList1.val < tempList2.val:
            resList.append(tempList1.val)
            tempList1 = tempList1.next
        else:
            resList.append(tempList2.val)
            tempList2 = tempList2.next

    if tempList1 is not None:
        while tempList1 is not None:
            resList.append(tempList1.val)
            tempList1 = tempList1.next
    if tempList2 is not None:
        while tempList2 is not None:
            resList.append(tempList2.val)
            tempList2 = tempList2.next

    return resList


def main():
    l1 = [1, 2, 4]
    l2 = [1, 3, 5]
    l1current = l1dummy = ListNode(0)
    l2current = l2dummy = ListNode(0)

    for i in range(0, len(l1)):
        newNode = ListNode(l1[i])
        l1current.next = newNode
        l1current = newNode
    list1 = l1dummy.next
    l1dummy = None

    for j in range(0, len(l2)):
        newNode = ListNode(l2[j])
        l2current.next = newNode
        l2current = newNode
    list2 = l2dummy.next
    l2dummy = None

    print(mergeTwoLists(list1, list2))


if __name__ == "__main__":
    sys.exit(main())
