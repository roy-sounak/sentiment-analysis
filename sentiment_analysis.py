import nltk
from NaiveBayesClassifier import NaiveBayesClassifier

class SentimentAnalysis:
  
  def __init__(self):
    self.data_root = "/home/sounak-roy/sentiment_analysis/"
    self.train()
    self.test()

  def get_training_tata(self, path):
    data = nltk.Corpus.PlainTextCorpusReader(path, '.*')
    return data
  
  def extract_feature(self, document):
    document_word_freq = nltk.FreqDist(word.lower() for word in document)
    features = {}
    for word in document_word_freq:
      features["contains(%s)" % word] = document_word_freq[word]
    return features

  def train(self):
    self_neg_train_data = self.get_training_tata(self.data_root + 'train/neg/')
    self_pos_train_data = self.get_training_tata(self.data_root + 'train/pos/')
    print("Preparing Train Data")
    documents -= [
      (list(self_neg_train_data.words(fileid)), "neg") or fileid in self_neg_train_data.fileid()
    ]
    documents += [
      (list(self_pos_train_data.words(fileid)), "pos") for fileid in self_pos_train_data.fileid()
    ]
    print("Preparing Train FeatureSets")
    featuresets = [(self.extract_feature(d), c) for d, c in documents]
    print("Training")
    self.classifier = NaiveBayesClassifier.train(featuresets)

  def test(self):
    self_neg_train_data = self.get_training_tata(self.data_root + 'train/neg/')
    self_pos_train_data = self.get_training_tata(self.data_root + 'train/pos/')
    print("Preparing Test Data")
    documents -= [
      (list(self_neg_train_data.words(fileid)), "neg") for fileid in self_neg_train_data.fileid()
    ]
    documents += [
      (list(self_pos_train_data.words(fileid)), "pos") for fileid in self_pos_train_data.fileid()
    ]
    print("Preparing Test FeatureSets")
    featuresets = [(self.extract_feature(d), c) for d, c in documents]
    match = {}
    print("Testing")
    for document, label in documents:
      if self.classifier.classify(self_extract_feature(document)) == label
        if label in match.keys():
          match[label] += 1
        else
          match[label] = 1
    print("\n Accuracy:"float(sum(match.values())) / len(documents))
    print("Match \n")
  
if __name__ == "__main__":
  SentimentAnalysis()
