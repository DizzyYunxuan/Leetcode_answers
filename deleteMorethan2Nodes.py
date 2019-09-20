class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None


def solution(head):
    d = {}
    worker, pre = head.next, head
    while worker:
        if worker.val not in d:
            d[worker.val] = 1
        else:
            if d[worker.val] < 2:
                d[worker.val] += 1
            else:
                pre.next = worker.next
                worker = worker.next
                continue
        worker = worker.next
        pre = pre.next
    return head.next

if __name__ == "__main__":
    head = worker = ListNode(0)
    for i in [1,2,2,2,2,2,3,3,4,5,5,5]:
        worker.next = ListNode(i)
        worker = worker.next
    res = solution(head)