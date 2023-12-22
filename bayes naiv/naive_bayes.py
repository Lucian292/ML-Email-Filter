import math
from collections import defaultdict


class NaiveBayesClassifier:
    def __init__(self):
        self.class_probs = defaultdict(float)
        self.word_probs = defaultdict(lambda: defaultdict(float))
        self.vocab = set()

    def fit(self, X, y):
        total_docs = len(y)
        spam_docs = sum(y)
        non_spam_docs = total_docs - spam_docs

        self.class_probs['spam'] = spam_docs / total_docs
        self.class_probs['non_spam'] = non_spam_docs / total_docs

        spam_word_counts = defaultdict(int)
        non_spam_word_counts = defaultdict(int)

        for doc, label in zip(X, y):
            for word in doc:
                if label == 1:
                    spam_word_counts[word] += 1
                else:
                    non_spam_word_counts[word] += 1

        self.vocab = set(spam_word_counts.keys()) | set(non_spam_word_counts.keys())

        for word in self.vocab:
            self.word_probs[word]['spam'] = (spam_word_counts[word] + 1) / (spam_docs + len(self.vocab))
            self.word_probs[word]['non_spam'] = (non_spam_word_counts[word] + 1) / (non_spam_docs + len(self.vocab))

    def predict(self, X, threshold=0.5):
        predictions = []
        for doc in X:
            spam_score = math.log(self.class_probs['spam'])
            non_spam_score = math.log(self.class_probs['non_spam'])

            for word in doc:
                if word in self.vocab:
                    # Adăugăm o condiție pentru a trata cuvintele prezente doar într-un tip de clasă
                    if self.word_probs[word]['spam'] == 0 and self.word_probs[word]['non_spam'] == 0:
                        continue

                    spam_score += math.log(self.word_probs[word]['spam'])
                    non_spam_score += math.log(self.word_probs[word]['non_spam'])

            # Adăugăm o condiție pentru a clasifica un document ca spam numai dacă probabilitatea este semnificativă
            prediction = 1 if spam_score > non_spam_score and spam_score - non_spam_score > math.log(threshold) else 0
            predictions.append(prediction)

        return predictions
