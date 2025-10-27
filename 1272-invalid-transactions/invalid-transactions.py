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
        
        hashmap = defaultdict(list)
        result = set()

        for i, txn in enumerate(transactions):
            name, time, price, city = txn.split(",")
            time = int(time)
            price = int(price)

            for j in hashmap[name]:
                prev_name, prev_time, prev_price, prev_city = transactions[j].split(",")
                prev_time = int(prev_time)

                if abs(time - prev_time) <= 60 and prev_city != city:
                    result.add(i)
                    result.add(j)
                    
            if price > 1000:
                result.add(i)

            hashmap[name].append(i)
     
        return [transactions[i] for i in result]




            
            