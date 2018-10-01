import re


STOP_WORDS = [
    "ourselves",
    "hers",
    "between",
    "yourself",
    "but",
    "again",
    "there",
    "about",
    "once",
    "during",
    "out",
    "very",
    "having",
    "with",
    "they",
    "own",
    "an",
    "be",
    "some",
    "for",
    "do",
    "its",
    "yours",
    "such",
    "into",
    "of",
    "most",
    "itself",
    "other",
    "off",
    "is",
    "s",
    "am",
    "or",
    "who",
    "as",
    "from",
    "him",
    "each",
    "the",
    "themselves",
    "until",
    "below",
    "are",
    "we",
    "these",
    "your",
    "his",
    "through",
    "don",
    "nor",
    "me",
    "were",
    "her",
    "more",
    "himself",
    "this",
    "down",
    "should",
    "our",
    "their",
    "while",
    "above",
    "both",
    "up",
    "to",
    "ours",
    "had",
    "she",
    "all",
    "no",
    "when",
    "at",
    "any",
    "before",
    "them",
    "same",
    "and",
    "been",
    "have",
    "in",
    "will",
    "on",
    "does",
    "yourselves",
    "then",
    "that",
    "because",
    "what",
    "over",
    "why",
    "so",
    "can",
    "did",
    "not",
    "now",
    "under",
    "he",
    "you",
    "herself",
    "has",
    "just",
    "where",
    "too",
    "only",
    "myself",
    "which",
    "those",
    "i",
    "after",
    "few",
    "whom",
    "t",
    "being",
    "if",
    "theirs",
    "my",
    "against",
    "a",
    "by",
    "doing",
    "it",
    "how",
    "further",
    "was",
    "here",
    "than",
]


class SimpleTokenizer:
    """
    Generate a list of words and positions.

    This is the most simple possible tokenizer, it only split word on the
    spaces.
    """

    def tokenize(self, document):
        sentences = self._generate_sentences(document)

        result = []
        for i, s in enumerate(sentences):
            for term in s.split(" "):
                if term.lower() not in STOP_WORDS:
                    result.append((self._generate_term(term), i))

        return result

    def _generate_sentences(self, document):
        return [sentence.strip() for sentence in document.split(".") if sentence]

    def _generate_term(self, term):
        return re.sub("[^A-Za-z0-9]+", "", term.lower())


class InvertedIndex:
    """
    Create a simple inverted index to store a word and where it's used.

    This idea cames from the Elasticsearch invertedIndex. The good point here
    is it's possible to search documents with this word with the O(1)
    complexity.

    InvertedIndex:
    {
        "south": {
            "document_id": [sentence0, sentence1]
        }
    }
    """

    def __init__(self, tokenizer=SimpleTokenizer):
        self.inverted_index = {}
        self.document_store = {}
        self.tokenizer = SimpleTokenizer()

    def index(self, document_name, document):
        """
        Index a new word in the inverted index.

        Example:
          self.index(document_name, document)
        """
        self.document_store[document_name] = document

        terms = self.tokenizer.tokenize(document)

        for term, position in terms:
            if term not in self.inverted_index:
                self.inverted_index[term] = {}

            if document_name not in self.inverted_index[term]:
                self.inverted_index[term][document_name] = []

            self.inverted_index[term][document_name].append(position)

    def search(self, term):
        """
        Search documents with using this word.

        The complexity to discovery one document is O(1)

        Example:
            self.search("south")
        """
        data = self.inverted_index[term]
        document_ids = data.keys()

        result = []
        for doc_id in document_ids:
            sentences = self._generate_sentences(doc_id)

            for position in data[doc_id]:
                result.append(sentences[position])

        return (document_ids, result)

    def show(self):
        with open("sample.csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")

            for term in self.inverted_index.keys():
                ids, sentences = self.search(term)
                writer.writerow(
                    [term, self._format_ids(ids), self._format_sentences(sentences)]
                )

    def _format_ids(self, doc_ids):
        return ", ".join(doc_ids)

    def _format_sentences(self, sentences):
        return "| ".join(sentences)

    def _generate_sentences(self, document_id):
        """Split a document in sentences."""
        document = self.document_store[document_id]

        sentences = []
        for sentence in document.split("."):
            if not sentence:
                continue

            sentence = sentence.replace("\n", "")
            sentences.append(sentence.strip())

        return sentences
