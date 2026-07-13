class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        letters = defaultdict(int)
        window_size = len(s1)
        # need to know which letters and the count of each letter in s1
        for letter in s1:
            letters[letter] += 1

        # need to go through s2 and start by finding a letter that exists in letters
        left = 0
        while left <= len(s2) - window_size and s2[left] not in letters:
            left += 1
        
        if left > len(s2) - window_size:
            return False
        right = left + window_size - 1
        # once we find it we then need to move through the letters to make sure the appropraite
        # number of letters are there or till we encounter a letter not in letters

        # we can create a window of size len(s1) that will set our bounds 
        # move the left side of the window till we encouter a letter in letters

        # once there iterate through the window to see if the appropriate letters are there

        # if a letter is not there or the count is already 0 then we fail to find it
        # we then move the window up by incrementing the current letter at the left side
        # and moving the left side till we find another letter that is in 

        i = left
        while right < len(s2):
            if s2[i] in letters:
                if letters[s2[i]] == 0:
                    # then the count is off need to move l up one
                    while s2[left] != s2[i]:
                        letters[s2[left]] += 1
                        left += 1
                    left += 1
                    # reset the window
                    right = left + window_size - 1
                    # move i ahead
                    i += 1
                else:
                    letters[s2[i]] -= 1 # decrement the count
                    if i == right:
                        return True
                    i += 1
            else:
                # character is not in letters so the whole window is not valid
                while left < i:
                    letters[s2[left]] += 1
                    left += 1
                left = i + 1
                right = left + window_size - 1
                i = left

        return False