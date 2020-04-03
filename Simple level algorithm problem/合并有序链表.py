
# 问题：
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeOrderedListProblem(object):
    @staticmethod
    def merge_ordered_list(l1: ListNode, l2: ListNode):
        # 增加一个冗余的节点，方便后续处理
        p = ListNode(-1)
        head = p
        # 这里的意思是l1!=null && l2!=null
        while l1 and l2:
            # 如果l1的val<=l2的val，就将p指向l1
            # p.next,l1 = l1,l1.next这里是将两行合并了
            # 只是为了代码简洁，面试时如果没有十足把握尽量分多行写
            if l1.val <= l2.val:
                p.next, l1 = l1, l1.next
            # else时，将p指向l2节点
            else:
                p.next, l2 = l2, l2.next
            p = p.next
        # 这里是一个三目表达式，类似
        # l1==null? l2:l1
        # 如果l1不为空就将p.next指向l2
        # 如果l1为空就指向l2，如果l2也为空那就指向空
        p.next = l1 if l1 else l2
        return head.next


linked_list1 = ListNode([1, 2, 4])
linked_list2 = ListNode([1, 3, 4])
MergeOrderedListProblem().merge_ordered_list(linked_list1, linked_list2)


# 链表的节点的结构如下：
# +---------+--------+
# |  data   |  next  |
# +---------+--------+
#
# data为自定义的数据，next为下一个节点的地址。
# 链表的结构为，head保存首位节点的地址：
# +---------+--------+    +---------+--------+    +---------+--------+
# |  data1  |  next  |--->|  data2  |  next  |--->|  data3  |  next  |--->....
# +---------+--------+    +---------+--------+    +---------+--------+
#    ↑
#    |
#   head



