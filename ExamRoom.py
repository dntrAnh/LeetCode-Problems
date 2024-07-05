from heapq import heappush, heappop, heapify

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.heap = []

    def seat(self) -> int:
        if not self.heap:
            start, end = -1, self.n
        else:
            _, start, end = heappop(self.heap)
        
        if start == -1:
            seat = 0
        elif end == self.n:
            seat = self.n - 1
        else:
            seat = (start + end) // 2
        
        dist_left = (seat - start) // 2 if start != -1 else seat
        dist_right = (end - seat) // 2 if end != self.n else self.n - 1 - seat

        heappush(self.heap, [-dist_left, start, seat])
        heappush(self.heap, [-dist_right, seat, end])
        
        return seat

    def leave(self, p: int) -> None:
        interval_start = interval_end = None
        for interval in self.heap:
            if interval[1] == p:
                interval_start = interval
            if interval[2] == p:
                interval_end = interval
        
        self.heap.remove(interval_start)
        self.heap.remove(interval_end)
        heapify(self.heap)
        
        start, end = interval_end[1], interval_start[2]
        dist = (end - start) // 2
        if start == -1:
            dist = end
        elif end == self.n:
            dist = self.n - 1 - start
        
        heappush(self.heap, [-dist, start, end])
