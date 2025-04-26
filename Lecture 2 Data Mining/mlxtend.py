from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({
    'A': [1, 0, 1, 0],
    'B': [0, 1, 1, 1],
    'C': [1, 1, 1, 0],
    'E': [0, 1, 1, 1]})

# Convert data to boolean type
data = data.astype(bool)

# Find frequent itemsets using apriori algorithm
frequent_itemsets = apriori(data, min_support=0.5, use_colnames=True)
print(frequent_itemsets)

# Find frequent itemsets using fpgrowth algorithm
frequent_itemsets = fpgrowth(data, min_support=0.5, use_colnames=True)
print(frequent_itemsets)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
print(rules[["antecedents", "consequents", "support", "confidence"]])

# Filter rules by support >= 0.6
rules = rules[rules["support"] >= 0.6]
print(rules[["antecedents", "consequents", "support", "confidence"]])
