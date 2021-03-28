class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        _list = [num_of_box for num_of_box in zip(*boxTypes)]
        _dict = {}
        for num_of_box, num_of_unit in zip(*_list):
            if num_of_unit in _dict:
                _dict[num_of_unit] += num_of_box
            else:
                _dict[num_of_unit] = num_of_box
        sorted_array = sorted(_dict.items(), key=lambda x: x[0], reverse=True)
        truck_size = truckSize
        output = 0
        for i in sorted_array:
            num_of_unit, num_of_box = i[0], i[1]
            if truck_size < num_of_box:
                output = output + truck_size * num_of_unit
                break
            output = output + num_of_unit * num_of_box
            truck_size = truck_size - num_of_box
        return output
