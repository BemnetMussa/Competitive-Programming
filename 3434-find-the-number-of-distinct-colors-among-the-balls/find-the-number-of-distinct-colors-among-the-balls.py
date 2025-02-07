class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        

        query_count = defaultdict(int)
        color_count = defaultdict(int)

        ans = []
        for query in queries:

            if query_count[query[0]] > 0:
                # getting the previous color
                pop_colored = query_count[query[0]]

                # removing the old color from the color count dict
                color_count[pop_colored] -= 1
                if color_count[pop_colored] <= 0:
                    del color_count[pop_colored]

                # updating the ball of the color
                query_count[query[0]] = query[1]

                # updating the color_count with the new color
                if color_count[query[1]] > 0:
                    color_count[query[1]] += 1
                else:
                    color_count[query[1]] = 1

            else:
                query_count[query[0]] = query[1]

                # updating the color_count with the new color
                if color_count[query[1]] > 0:
                    color_count[query[1]] += 1
                else:
                    color_count[query[1]] = 1



            ans.append(len(color_count))

        return ans


        
                
            
            