import heapq

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        survivors = []
        robots = []
        pos_to_idx = {}

        for idx in range(len(positions)): 
            pos_to_idx[positions[idx]] = idx 
            robots.append((positions[idx], healths[idx], directions[idx]))
        
        robots.sort()

        # Stack to keep track of robots moving to the right
        right_stack = []

        for pos, health, direction in robots:
            if direction == "R":
                right_stack.append((pos, health))
            else: 
                while right_stack: 
                    right_pos, right_health = right_stack.pop()
                    if health > right_health: 
                        health -= 1
                    else: 
                        # If the right-moving robot has equal or more health
                        right_health -= 1
                        # If the right-moving robot survives the collision, push it back to the stack
                        if right_health != health - 1: 
                            right_stack.append((right_pos, right_health))
                        # The left-moving robot is destroyed
                        health = 0 
                        break
                
                # If the left-moving robot survives collisions
                if health != 0: 
                    heapq.heappush(survivors, (pos_to_idx[pos], health))
        
        # Add remaining right-moving
        while right_stack: 
            right_pos, right_health = right_stack.pop()
            heapq.heappush(survivors, (pos_to_idx[right_pos], right_health))

        result = []
        # Extract the healths
        while survivors: 
            _, health = heapq.heappop(survivors) 
            result.append(health) 
        
        return result
