class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort() 
        passengers.sort() 

        idx = 0 

        for bus in buses: 
            cap = capacity 
            while idx < len(passengers) and bus >= passengers[idx] and cap > 0:
                cap -= 1
                idx += 1 
        
        latest = buses[-1] if cap > 0 else passengers[idx - 1]

        passengers_set = set(passengers)
        while latest in passengers_set:
            latest -= 1

        return latest
