# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k):
        arr = listnode_to_arr(head)
        # print("arr:",arr)
        n = len(arr)
        temp = arr[k-1]
        temp_k = arr[-k]
        arr[k-1] = temp_k
        arr[-k] = temp
        # print("arr:",arr)
        node = arr_to_listnode(arr)

        return node


def arr_to_listnode(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


def listnode_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def main():
    # input

    arr = [1, 2, 3, 4, 5]
    k = 2

    head = arr_to_listnode(arr)
    # print(head.val)

    # arr_temp = listnode_to_arr(head)
    # print(arr_temp)

    # solution
    s = Solution()
    ret = s.swapNodes(head, k)



    # result
    print("ret:", ret)


if __name__ == "__main__":
    main()
