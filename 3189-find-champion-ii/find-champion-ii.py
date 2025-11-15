class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        '''
            what we are given: DAG where a is directed to b whic means a stronger than b 
            Requered : to return the winner node or -1 if there is no one relashion ship 

            approche ~ toplogical sort
            - giving each node a rank. Which the rank is the count of incomming nodes
            - idetnifying the nodes that have 0 ranks 
                - if there is one node. Return the node
                - else return -1

        '''

        indegree = [0] * n

        for a, b in edges:
            indegree[b] += 1
     
        winner = [i for i in range(len(indegree)) if indegree[i] == 0]

        return winner[0] if len(winner) == 1 else -1

        