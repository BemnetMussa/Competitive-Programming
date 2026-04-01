from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])

        stack = []          # holds indices of robots moving Right ("R")
        alive = [True] * n  # alive[i] = robot i survived or not

        for i in order:
            if directions[i] == "R":
                stack.append(i)
            else:  # directions[i] == "L"
                while stack and alive[i]:
                    j = stack[-1]  # last right-moving robot

                    if healths[j] < healths[i]:
                        # right robot dies
                        alive[j] = False
                        stack.pop()
                        healths[i] -= 1

                    elif healths[j] > healths[i]:
                        # left robot dies
                        alive[i] = False
                        healths[j] -= 1

                    else:
                        # both die
                        alive[i] = False
                        alive[j] = False
                        stack.pop()

        # return survivors in original order
        return [healths[i] for i in range(n) if alive[i]]