class MyCalendar:

    def __init__(self):
        self.dates = []

    def book(self, start: int, end: int) -> bool:
        if self.dates == []: 
            self.dates.append([start, end]) 
            return True 
        for i in self.dates: 
            if i[0] < start < i[1] or i[0] < end < i[1] or start < i[0] < end or start < i[1] < end or i[0] == start or i[1] == end:
                return False 
        self.dates.append([start, end])
        return True 

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
