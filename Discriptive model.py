# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.linear_model import LogisticRegression

# # Training data
# texts = [
#     "stable income and good credit history",
#     "high salary with low debt",
#     "regular loan repayments",
#     "poor credit history",
#     "multiple missed payments",
#     "high debt and low income"
# ]

# labels = [1, 1, 1, 0, 0, 0] 

# # Vectorization
# vectorizer = CountVectorizer()

# X = vectorizer.fit_transform(texts)

# # Train model
# model = LogisticRegression()

# model.fit(X, labels)

# # Prediction
# test = vectorizer.transform(["good credit history"])

# prediction = model.predict(test)

# print("Prediction:", prediction[0])

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training sentences
sentences = [
    "wealth management builds assets",
    "investment planning creates returns",
    "mutual funds diversify portfolio",
    "financial goals require discipline",
    "risk management protects wealth",
    "long term investing generates growth"
]

# Prepare training data
X_train = []
y_train = []

for sentence in sentences:

    words = sentence.lower().split()

    for i in range(len(words)-1):

        X_train.append(words[i])
        y_train.append(words[i+1])

# Vectorization
vectorizer = CountVectorizer()

X_vectors = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_vectors, y_train)

# Generate text
def generate_text(start_word, length=3):

    current_word = start_word.lower()

    generated = [current_word]

    for _ in range(length):

        current_vector = vectorizer.transform([current_word])

        predicted_word = model.predict(current_vector)[0]

        generated.append(predicted_word)

        current_word = predicted_word

    return " ".join(generated)

# Example
output = generate_text("wealth", 4)

print("Generated Text:",output)