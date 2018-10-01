# searchengine
> Another python searchengine

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

### Getting Started

The idea of this project is to provide a rapid way to ```index``` and ```search``` words in a specified text.

This project requires:
* Python 3.6+
* And has no dependencies

### Using as a client

1. It´s possible to use this library as a client like:

```python
from searchengine import InvertedIndex

index = InvertedIndex()
index.index(document_name="doc1", document="Lorem ipsum...")

# It´s possible to search for a specific word like:
index.search("lorem")

# The ouput of this search will be with O(1) complexity:
{"lorem": {"doc1": [0]}}

# This output means the word lorem was found in the document ```doc1``` in the sentence 0
```

2. It's also possible to use as a command like this:
```sh
python main.py tests/fixtures/doc1.txt

# This will generate a CSV file called sample.csv like this

# Word; document_ids; Sentences (splited by | operator)
# lorem; doc1.txt, Lorem ipsum...|Lorem ipsum
```

### Tests
I wrote only one test for now, but there are many points to test's

I setup the pytest with the ```coverage``` and ```pep8```

1. To run all tests:

```sh
make tests
```

### Improvements

1. Increase the coverage of tests
2. At the moment I only consider sentence pieces with a "." at the end. Improve this to work with !, ?,
3. The performance to index and search one work it's really awesome, but to create the sample.csv output it's not really good
4. Setup TravisCI to run the tests
