class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        Strategy:
        TC: O(len(items) * O(log(len(items))))
        SC: O(number_of_ids)
        Get a list of all scores in sorted order under an ID. Store that in a map
        Go over the map and calculate the average, populate result

        {
        student_ID = (min_heap containing all scores)

        }

        Easier approach: Go with this, easier to implement
        TC: O(log(n) * n) -> n = len(items)
        SC: O(number_of_ids)
        Sort the list (O(log(len(items))))
        Loop over list and Get the last 5 elements of each ID'd element, calculate average and populate res.
        """
        def get_avg(lower_bound, upper_bound):
            sum_ = 0
            for i in range(lower_bound, upper_bound + 1):
                sum_ += items[i][1]
            return sum_ // 5
        items.sort()
        res = []
        idx = 0
        while idx < len(items) - 1:
            # Encountered last id of current student
            if items[idx][0] != items[idx + 1][0]:
                # Grab the last five elements
                lower_bound = max(idx - 4, 0)
                avg = get_avg(lower_bound, idx)
                res.append([items[idx][0], avg])
            idx += 1
        avg = get_avg(max(len(items) - 5,0), len(items) - 1)
        res.append([items[idx][0], avg])
        return res
