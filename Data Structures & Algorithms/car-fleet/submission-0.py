class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        # build up the positions and speeds 
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        pos_speed.sort(reverse=True)
        num_fleets = 0

        # now that we have the position and speed we need to know when they will get there
        time_to_arrive = list()
        for i in range(len(pos_speed)):
            time = (target - pos_speed[i][0]) / pos_speed[i][1]
            time_to_arrive.append(time)

        stack = []
        for time in time_to_arrive:
            if stack and stack[0] < time:
                while stack and stack[-1] <= time:
                    stack.pop()
                num_fleets += 1 
            stack.append(time)
        
        if stack:
            num_fleets += 1
        
        return num_fleets


