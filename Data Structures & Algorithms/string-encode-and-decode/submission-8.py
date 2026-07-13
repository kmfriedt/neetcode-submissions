class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = len(string)
            result += f"{length}#{string}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        
        while index < len(s):
            length = ""
            while s[index] != '#':
                length += s[index]
                index += 1
            # now we have the length as a string
            num_chars = int(length)
            # move the index past the delimiter
            index += 1
            new_index = index+num_chars
            sub_string = s[index:new_index]
            result.append(sub_string)
            index = new_index

        return result
