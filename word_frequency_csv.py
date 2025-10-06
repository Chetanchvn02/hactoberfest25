# word_frequency_csv.py
import pandas as pd
from collections import Counter

data = {
    "Comment": [
        "Hacktoberfest is fun and educational",
        "I love open source contribution",
        "Python is powerful for data analysis",
        "Learning by doing is the best way"
    ]
}

df = pd.DataFrame(data)
all_words = " ".join(df["Comment"]).lower().split()
freq = Counter(all_words)

print("📝 Word Frequency Analysis:")
for word, count in freq.items():
    print(f"{word}: {count}")
