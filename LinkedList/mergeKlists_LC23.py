class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 
        
def mergeKlist(lists):
    if not lists or len(lists) == 0:
        return None 
    
    while len(lists)>1:
        temp = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None 
            temp.append(merge(l1, l2))
        lists = temp
    return lists

def merge(l1, l2):
    dummy = ListNode()
    ans = dummy 
    while l1 and l2:
        if l1.val > l2.val:
            dummy.next = l2
            l2 = l2.next
        else:
            dummy.next = l1
            l1 = l1.next 
        dummy = dummy.next 
    if l1:
        dummy.next = l1 
    else:
        dummy.next = l2
    return ans.next 
        
    
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result       
                
lists = [
    build_linked_list([1, 4, 5]),
    build_linked_list([1, 3, 4]),
    build_linked_list([2, 6])
]

merged = mergeKlist(lists)

merged_head = merged[0]

print(linked_list_to_list(merged_head))