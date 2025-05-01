from bisect import bisect_left
from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        tasks.sort()
        workers.sort()

        def can_assign(k):
            task_list = tasks[:k]
            worker_list = SortedList(workers[-k:])
            pills_left = pills

            for i in range(k - 1, -1, -1):
                idx = worker_list.bisect_left(task_list[i])
                if idx < len(worker_list):
                    worker_list.pop(idx)
                else:
                    if pills_left == 0:
                        return False
                    idx = worker_list.bisect_left(task_list[i] - strength)
                    if idx == len(worker_list):
                        return False
                    worker_list.pop(idx)
                    pills_left -= 1
            return True

        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2
            if can_assign(mid):
                low = mid
            else:
                high = mid - 1
        return low
