class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Notes
        
        each pre-req in the list has [0] = the course and [1] = the pre-req
        numCourses = number of courses you have to take from 0 -> numCourses - 1

        This is a graph problem where we are trying to find a cycle in the graph

        How do we do that? 

        Construct the graph, start at each node, see if you can get back to the node through the graph
        There will be at least 1 course
        '''

        visited = set()
        # steps
        courses = defaultdict(list)
        # create the graph by going through pre-reqs
        for prereq in prerequisites:
            crs, pre = prereq[0], prereq[1]
            courses[crs].append(pre)


        def dfs(course):
            prereqs = courses[course]
            for prereq in prereqs:
                if prereq in visited:
                    return False
                else:
                    visited.add(prereq)
                    if not dfs(prereq):
                        return False
                    visited.remove(prereq)
                courses[course] = []
            return True

        # go through each node in the graph and look for cycles
            # if there is a cycle return false
        for course_num in range(numCourses):
            visited.add(course_num)
            can_finish = dfs(course_num)
            if not can_finish:
                return False
            visited.remove(course_num)

        # return true
        return True