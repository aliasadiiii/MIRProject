import nltk
from collections import defaultdict


class BaseIndexer(object):
    def save(self):
        raise NotImplementedError()

    def load(self):
        raise NotImplementedError()

    def add_document(self, doc_id, words):
        raise NotImplementedError()

    def delete_document(self, doc_id):
        raise NotImplementedError()


class PositionalIndexer(BaseIndexer):
    def __init__(self):
        self.inverted_index = defaultdict(list)
        self.deleted_docs = []

    def save(self):
        pass

    def load(self):
        pass

    def add_document(self, doc_id, words):
        distinct_words = list(set(words))
        for word in distinct_words:
            positions = [i for i, w in enumerate(words) if w == word]
            self.inverted_index[word].append((doc_id, positions))

    def delete_document(self, doc_id):
        self.deleted_docs.append(doc_id)

    def get_posting_list(self, word):
        return self.inverted_index[word]

    def get_all_words(self):
        return self.inverted_index.keys()


class BigramIndexer(BaseIndexer):
    def __init__(self):
        self.inverted_index = defaultdict(set)
        self.deleted_docs = []

    def save(self):
        pass

    def load(self):
        pass

    def add_document(self, doc_id, words):
        for word in words:
            for cc in nltk.ngrams(word, n=2):
                self.inverted_index[''.join(cc)].add(word)

    def delete_document(self, doc_id):
        self.deleted_docs.append(doc_id)


positional_indexer = PositionalIndexer()
bigram_indexer = BigramIndexer()
