class Solution:
    def isValid(self, s: str) -> bool:
        
        # need to track left and right strings some how

        opening = {'(', '{', '['}
        closing_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        seen = ''

        for string in s: 
            # if string in opening just add it
            if string in opening:
                seen += string
            
            else:
                # this is a closing bracket
                if len(seen) == 0 or seen[-1] != closing_map[string]:
                    return False
                else:
                    # correct closing bracket remove the opening bracket
                    seen = seen[:-1] # remove the last character

        if len(seen) == 0:
            return True
        else:
            return False