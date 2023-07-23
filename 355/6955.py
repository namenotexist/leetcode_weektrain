from typing import List
import heapq
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        # 创建一个空的优先队列
        priority_queue = []
        for i, time in enumerate(usageLimits):
            heapq.heappush(priority_queue, -time)
        ele_num = 0
        while True:
            tmp_container = []
            if len(priority_queue) < ele_num + 1:
                    return ele_num
            for i in range(ele_num+1):
                neg_time = heapq.heappop(priority_queue)
                if neg_time+1 != 0:
                    tmp_container.append(neg_time+1)
            ele_num += 1
            for i in range(len(tmp_container)):
                heapq.heappush(priority_queue, tmp_container[i])
        return ele_num
            

