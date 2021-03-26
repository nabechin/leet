class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        col_min = [min(i) for i in matrix]
        row_max = [max(i) for i in zip(*matrix)]
        return list(set(col_min) & set(row_max))
