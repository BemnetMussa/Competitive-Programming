'''
Given: array of strings transaction where transactions[i] consists of comma-separated values representing the (name, time (in minutes), amount, city of the transaction.)

Return: list of transactions that are possibly invalid. You may return the answer in **any order.
Transaction is invalid if: 
    - amount exceeds 1000
    - if it occurses within 60 minutes of another transaction with the same name, in differnet city.

transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
                                                                --> invalid = [txn1, txn2]
                       | (50-20) < 60
transactions = ["alice,20,8000,mtv","alice,100,100,beijing"]
                                                                --> invalid = [txn1]
                       | (100-20) > 60 
                       check the price > 1000

transactions.length <= 1000



'''

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        people = defaultdict(list) # people_name: [i]
        for i in range(len(transactions)):
            name, time, price, city = transactions[i].split(",")
            people[name].append((int(time), int(price), city, i))

        result = set()

        for name, txn in people.items():
            txn.sort() # sort the transactions based on time

            for i in range(len(txn)): 
                time, price, city, org_i = txn[i]
          
                for j in range(i+1, len(txn)):
                    time_j, price_j, city_j, org_j = txn[j]

                    if abs(time - time_j) <= 60 and city_j != city:
                        result.add(org_i)
                        result.add(org_j)
          
                if price > 1000:
                    result.add(org_i)

        return [transactions[i] for i in result] # tiem: O(N^2) and space of O(n)
            





            
            