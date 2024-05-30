def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                merged.next = list1
                
                list1, merged = list1.next, list1
            else:
                merged.next = list2
                list2, merged = list2.next, list2
        if list1 or list2:
            merged.next = list1 if list1 else list2