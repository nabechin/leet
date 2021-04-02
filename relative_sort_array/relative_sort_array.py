import collections

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_count = collections.Counter(arr1)
        distinct_list = []
        not_distinct_list = []
        for arr_two in arr2:
            if arr_two in num_count:
                for _ in range(0, num_count[arr_two]):
                    distinct_list.append(arr_two)
                num_count.pop(arr_two)
        for i in sorted(num_count.items(), key=lambda x:x[0]):
            for _ in range(0, i[1]):
                not_distinct_list.append(i[0])
        return distinct_list + not_distinct_list