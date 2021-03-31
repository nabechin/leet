class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        duplicate_list = list(A[0])
        for i in range(1, len(A)):
            temp_list = []
            for u in list(A[i]):
                if u in duplicate_list:
                    temp_list.append(u)
                    duplicate_list.remove(u)
            duplicate_list = temp_list
        return duplicate_list