class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map = defaultdict(int)
        s_map = defaultdict(int)

        if len(s) != len(t):
            return False

        for index, char in enumerate(s):
            s_map[char] += 1
            t_map[t[index]] += 1

        for key, value in s_map.items():
            if key not in t_map:
                return False
            if value != t_map[key]:
                return False
        return True