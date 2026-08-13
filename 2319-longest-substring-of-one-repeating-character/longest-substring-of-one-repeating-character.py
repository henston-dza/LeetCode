from dataclasses import dataclass
class Solution:
    class SegTree:
        @dataclass
        class Node:
            prefix_len: int
            suffix_len: int
            best_len: int

        def __init__(self, init_str: str):
            self.n = len(init_str)
            self.char_array = list(init_str)
            self.tree = [self.Node(prefix_len=1, suffix_len=1, best_len=1) for _ in range(4 * self.n)]

            self.build_tree(parent_node=1, left=0, right=self.n-1)

        def build_tree(self, parent_node: int, left: int, right: int):
            if left == right:
                leaf = self.Node(prefix_len=1, suffix_len=1, best_len=1)
                self.tree[parent_node] = leaf
                return

            mid = (left + right) // 2
            left_child = parent_node * 2
            right_child = parent_node * 2 + 1
            self.build_tree(parent_node=left_child, left=left, right=mid)
            self.build_tree(parent_node=right_child, left=mid+1, right=right)
            self.merge_children(parent_node=parent_node, left=left, right=right)

        def merge_children(self, parent_node: int, left: int, right: int):
            mid = (left + right) // 2
            left_len = mid - left + 1
            right_len = right - mid

            left_child = parent_node * 2
            right_child = parent_node * 2 + 1

            self.tree[parent_node].prefix_len = self.tree[left_child].prefix_len
            self.tree[parent_node].suffix_len = self.tree[right_child].suffix_len
            self.tree[parent_node].best_len = max(
                self.tree[left_child].best_len,
                self.tree[right_child].best_len
            )

            if self.char_array[mid] != self.char_array[mid + 1]:
                return

            if self.tree[left_child].prefix_len == left_len:
                self.tree[parent_node].prefix_len = left_len + self.tree[right_child].prefix_len
            if self.tree[right_child].suffix_len == right_len:
                self.tree[parent_node].suffix_len = right_len + self.tree[left_child].suffix_len
            self.tree[parent_node].best_len = max(
                self.tree[parent_node].best_len,
                self.tree[left_child].suffix_len + self.tree[right_child].prefix_len
            )

        def update_char(self, update_index: int, new_char: str):
            self.char_array[update_index] = new_char
            self.update_tree(update_index=update_index, parent_node=1, left=0, right=self.n-1)

        def update_tree(self, update_index: int, parent_node: int, left: int, right: int):
            if left == right:
                return
            left_child = parent_node * 2
            right_child = parent_node * 2 + 1
            mid = (left + right) //2
            if update_index <= mid:
                self.update_tree(update_index=update_index, parent_node=left_child, left=left, right=mid)
            else:
                self.update_tree(update_index=update_index, parent_node=right_child, left=mid+1, right=right)
            self.merge_children(parent_node, left, right)

        @property
        def best_len(self):
            return self.tree[1].best_len
                

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        seg_tree = self.SegTree(s)
        result = []
        for query_index, new_char in zip(queryIndices, queryCharacters):
            seg_tree.update_char(update_index=query_index, new_char=new_char)
            result.append(seg_tree.best_len)
        return result