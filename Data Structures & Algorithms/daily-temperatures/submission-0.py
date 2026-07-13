class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = list()
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and stack[-1][0] < temp:
                # get the index we want to update
                index = stack[-1][1]
                # update it with the value we want
                result[index] = i - index
                # remove the item from the end of the list
                stack.pop()
            
            # add the current item to the list
            stack.append((temp, i))

        return result