import heapq 

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: 
            return 0 
        
        stop_to_buses = defaultdict(list) 
        bus_to_stops = defaultdict(set) 

        for bus_num, bus_route in enumerate(routes): 
            for stop in bus_route: 
                stop_to_buses[stop].append(bus_num) 
                bus_to_stops[bus_num].add(stop) 

        # min_heap 
        heap = []
        visited_buses = set() 
        visited_stops = set() 

        for bus in stop_to_buses[source]: 
            heapq.heappush(heap, (1, bus))
            visited_buses.add(bus) 
        visited_stops.add(source) 

        while heap: 
            buses_taken, bus_num = heapq.heappop(heap) 

            if target in bus_to_stops[bus_num]: 
                return buses_taken 
            
            for stop in bus_to_stops[bus_num]: 
                if stop in visited_stops: 
                    continue 
                for new_bus in stop_to_buses[stop]: 
                    if new_bus not in visited_buses: 
                        visited_buses.add(new_bus) 
                        visited_stops.add(stop)
                        heapq.heappush(heap, (buses_taken + 1, new_bus))
        
        return -1 
