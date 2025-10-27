from typing import List
from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Group transactions by name
        people = defaultdict(list)
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            people[name].append((int(time), int(amount), city, i))

        invalid = set()

        for name, txns in people.items():
            # Sort transactions by time
            txns.sort(key=lambda x: x[0])
            l = 0  # left pointer for sliding window

            for r in range(len(txns)):
                time_r, amount_r, city_r, idx_r = txns[r]

                # Check amount > 1000
                if amount_r > 1000:
                    invalid.add(idx_r)

                # Move left pointer to maintain 60-minute window
                while time_r - txns[l][0] > 60:
                    l += 1

                # Compare current transaction with all in the window
                for k in range(l, r):
                    _, _, city_k, idx_k = txns[k]
                    if city_r != city_k:
                        invalid.add(idx_r)
                        invalid.add(idx_k)

        # Return transactions in original input order
        return [transactions[i] for i in sorted(invalid)]
