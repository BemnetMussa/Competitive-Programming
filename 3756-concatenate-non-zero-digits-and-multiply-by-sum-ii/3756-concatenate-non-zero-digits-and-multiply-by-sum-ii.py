class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        x_list = [0]
        sum_list = [0]
        lengths = [0]

        conc = 0
        curr_sum = 0
        length = 0

        power = [1] * (len(s) + 1)

        for i in range(1, len(s) + 1):
            power[i] = (power[i - 1] * 10) % MOD

        for num in s:
            digit = int(num)

            if digit > 0:
                conc = (conc * 10 + digit) % MOD
                length += 1

            curr_sum += digit

            x_list.append(conc % MOD)
            sum_list.append(curr_sum)
            lengths.append(length)

        answer = []
        for l, r in queries:
            r += 1

            digit = lengths[r] - lengths[l]
            # x = x_list[r] - ((x_list[l] * 10 ** digit) % MOD) # suprizingly comupting the digits is not time effeint 
            x = (x_list[r] - (x_list[l] * power[digit]) % MOD) % MOD
            digit_sum = sum_list[r] - sum_list[l]

            answer.append((x * digit_sum) % MOD)

        return answer

