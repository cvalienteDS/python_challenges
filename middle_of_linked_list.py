# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]

    def middleNodeTwoPointers(self, head):
        l, r = head, head
        while r.next:
            l = l.next
            r = r.next.next
        return l


linkedList = ListNode(val=1, next=2)

solution = Solution().middleNodeTwoPointers(linkedList)

print(solution)
print('')