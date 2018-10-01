import argparse
import os

from searchengine import InvertedIndex


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a text document")
    parser.add_argument("filename", help="Document to parse")

    args = parser.parse_args()

    with open(args.filename, "r") as f:
        data = f.read()

    _, filename = os.path.split(args.filename)

    index = InvertedIndex()
    index.index(document_name=filename, document=data)

    index.show()