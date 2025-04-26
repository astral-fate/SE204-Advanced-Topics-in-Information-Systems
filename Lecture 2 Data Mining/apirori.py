import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Define the transaction data
transactions = [
    ['Pen', 'Eraser', 'Pencil'],
    ['Pen', 'Ruler', 'Eraser', 'Book'],
    ['Ruler', 'Book'],
    ['Ruler', 'Eraser', 'Book']
]

# A. Determine frequent patterns using FP-Growth with min_support=0.4 (40%)
# Convert transactions to one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply FP-Growth algorithm
frequent_itemsets = fpgrowth(df, min_support=0.4, use_colnames=True)
print("A. Frequent itemsets with minimum support of 40%:")
print(frequent_itemsets)
print("\n")

# B. Determine the strongest association rules with min_support=0.4 and min_confidence=0.8
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
print("B. Association rules with minimum support of 40% and minimum confidence of 80%:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# For better understanding, let's sort the rules by confidence and lift
print("\nSorted by confidence:")
print(rules.sort_values(['confidence', 'lift'], ascending=[False, False])[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
