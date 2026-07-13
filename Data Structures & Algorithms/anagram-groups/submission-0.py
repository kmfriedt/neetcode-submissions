class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # so we have a list of strings, that vary in length and vary
        # in which characters are in them

        # need a way to group all the strings with the same letters into 
        # the same group

        # could hash the strings, would need to sort the characters into
        # alphabetical order first

        # create a hash map (dict)
        string_map = defaultdict(list)

        # iterate through the strings
        for string in strs:
            # take the string and put the chars into alphabetical order
            key_string = "".join(sorted(string))
            # add the sorted string to the hash map as the key and
            # add the OG string to the list of values
            string_map[key_string].append(string)
        
        # build the output
        result = []
        for key, value in string_map.items():
            result.append(value)
        return result