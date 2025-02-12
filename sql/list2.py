class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp != None:
            n+=1
            temp = temp.next
        temp = head
        half = n//2
        while half:
            temp = temp.next
            half-=1
        return temp