from collections import defaultdict

class PincerSearch:

    def __init__(self, transactions, min_support):

        self.transactions = transactions

        self.min_support = min_support

        self.itemsets = defaultdict(int)

        self.frequent_itemsets = {}

    def run(self):

        # Phase 1: Generate 1-itemsets and their counts

        for transaction in self.transactions:

            for item in transaction:

                self.itemsets[frozenset([item])] += 1

        # Phase 2: Generate k-itemsets and their counts

        k = 2

        while self.itemsets:

            candidate_itemsets = self.generate_candidate_itemsets(k)

            frequent_itemsets = self.get_frequent_itemsets(candidate_itemsets)

            if frequent_itemsets:

                self.frequent_itemsets[k] = frequent_itemsets

                k += 1

            else:

                break

        return self.frequent_itemsets

    def generate_candidate_itemsets(self, k):

        # Generate candidate k-itemsets by joining frequent (k-1)-itemsets

        candidate_itemsets = set()

        for itemset1 in self.itemsets:

            for itemset2 in self.itemsets:

                if len(itemset1.union(itemset2)) == k:

                    if len(itemset1.intersection(itemset2)) == k - 2:

                        candidate_itemsets.add(itemset1.union(itemset2))

        return candidate_itemsets

    def get_frequent_itemsets(self, candidate_itemsets):

        # Count occurrences of candidate itemsets

        itemset_counts = defaultdict(int)

        for transaction in self.transactions:

            for itemset in candidate_itemsets:

                if itemset.issubset(transaction):

                    itemset_counts[itemset] += 1

        # Prune candidate itemsets that don't meet minimum support threshold

        frequent_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count >= self.min_support}

        # Update itemsets with frequent itemsets

        self.itemsets = frequent_itemsets

        return frequent_itemsets

transactions = [    [1, 2, 3],

    [1, 2, 4],

    [1, 3, 4],

    [2, 3, 4],

    [1, 2, 3, 4],

    [2, 3],

    [1, 4]

]

min_support = 2

psa = PincerSearch(transactions, min_support)

frequent_itemsets = psa.run()

print(frequent_itemsets)