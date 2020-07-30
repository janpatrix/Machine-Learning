import math
import pandas as pd


bug_data = pd.read_csv("/Users/patrick.gross/Development/MachineLearning/Lesson4/data/bug_data.csv")
colors = bug_data['Color'].value_counts()
big_bugs = bug_data[bug_data['Size'] < 17.0]
bigger_bugs = bug_data[bug_data['Size'] < 20.0]

big_bugs_count = [big_bugs['Size'].size, bug_data['Size'].size - big_bugs['Size'].size]
bigger_bugs_count = [bigger_bugs['Size'].size, bug_data['Size'].size - bigger_bugs['Size'].size]

def calculate_entropy(feature_test):
    entropy = 0
    for f in feature_test:
        entropy += -f/sum(feature_test)*math.log2(f/sum(feature_test))
    return entropy

total_entropy = calculate_entropy(colors)
print("COLORS")
print(total_entropy)

print("SMALLER 17")
smaller_17 = calculate_entropy(big_bugs_count)
print("SMALLER 20")
smaller_20 = calculate_entropy(bigger_bugs_count)

#color = bug_data.sort_values(['Color', 'Bugs'])
blue = bug_data[bug_data['Color'] == 'Blue']['Bugs'].value_counts()
brown = bug_data[bug_data['Color'] == 'Brown']['Bugs'].value_counts()
green = bug_data[bug_data['Color'] == 'Green']['Bugs'].value_counts()

print("BLUE")
print(total_entropy - calculate_entropy(blue))
print("BROWN")
print(total_entropy - calculate_entropy(brown))
print("GREEN")
print(total_entropy - calculate_entropy(green))

child_big_bug = bug_data[bug_data['Size'] < 17.0]['Bugs'].value_counts()

print('BIG BUG')
print(smaller_17 - calculate_entropy(child_big_bug))

print("BIGGER BUG")
child_bigger_bug = bug_data[bug_data['Size'] < 20.0]['Bugs'].value_counts()
print(smaller_20 - calculate_entropy(child_bigger_bug))

#print(smaller_20 - (calculate_entropy(child_bigger_bug) + calculate_entropy(child_biggerbig_bug))/2)
