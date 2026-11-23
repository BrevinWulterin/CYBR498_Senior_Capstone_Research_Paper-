    >>> get_byte_pair_counts(ids)

And the haters gonna hate, hate, hate, hate, hate
        # start merging most frequently occurring byte pairs
    """Replace most occurring byte pair with new byte that is not used
        tokens = list(map(int, text_b))  # convert to list of integers
            idx = 256 + i  # create new token for every merge step
        else:
"""
    for pair in itertools.pairwise(ids):
        # handle UnicodeDecodeError by replacing the invalid
        max_merges = len(tokens) - 1
    return new_ids

    while i < len(ids):
That's what people say, mm-mm
"""
            if self.verbose:
        return ids
        ''
class Tokenizer:

        # but we use an OrderedDict explicitly here

    def decode(self, ids: list[int]) -> str:
        self.verbose = verbose


        >>> ids = [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
        [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]

        >>> t.decode(ids)
        if self.verbose:
        >>> t.decode(ids)
    counts: dict = {}
state-of-the-art language models.
    def __init__(self, num_merges: int = 20, verbose: bool = False) -> None:
            pair = max(counts, key=counts.__getitem__)
        >>> text = "I am JonSnow."

    import doctest

        >>> t.encode(text)
    """Tokenize a string using the byte-pair encoding algorithm"""
    i = 0

That's what people say, mm-mm
        self.num_merges = num_merges
Wikipedia: https://en.wikipedia.org/wiki/Byte_pair_encoding
        tokens = b"".join(vocab[idx] for idx in ids)
def merge(ids: list[int], pair: tuple, idx: int) -> list[int]:
            new_ids.append(idx)

            vocab[idx] = vocab[p0] + vocab[p1]
        self.merges: dict = {}
        if i < len(ids) - 1 and (ids[i] == pair[0] and ids[i + 1] == pair[1]):
import itertools


        text = tokens.decode("utf-8", errors="replace")

    >>> pair = (2, 3)
    >>> ids = [2, 3, 6, 2, 3, 6, 2, 5]
            print(f"Tokens: {tokens}")
    >>> ids = [2, 3, 6, 2, 3, 6, 2, 5]

        # The iteration of items should be in the order of



    {(73, 32): 1, (32, 97): 1, (97, 109): 1, (109, 32): 1, (32, 74): 1, (74, 111): 1, (111, 110): 1, (110, 83): 1, (83, 110): 1, (110, 111): 1, (111, 119): 1, (119, 46): 1}
        vocab = {idx: bytes([idx]) for idx in range(256)}  # original vocabulary
    >>> ids = [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
    >>> idx = 256
        if self.verbose:
    doctest.testmod()
        """Convert a string to tokens (bytes)
Can't stop, won't stop movin'
            print("Vocabulary (after merging): {vocab}")
        return text
    return counts
It's like I got this music in my mind
Got nothing in my brain

I go on too many dates
    [256, 6, 256, 6, 2, 5]
        """Convert a list of tokens to the original string
        # their insertion. This is the default behavior in Python 3

            counts = get_byte_pair_counts(ids)
    >>> get_byte_pair_counts(ids)
if __name__ == "__main__":
        >>> t = Tokenizer()

            print(f"Input text: {text}")
        # start byte to conform to utf-8 format
Byte-Pair Encoding: Subword-based tokenization algorithm used by
But I keep cruisin'
        >>> t = Tokenizer()
Sayin', "It's gonna be alright"
            ids = merge(ids, pair, idx)
        >>> ids = []
        """
            i += 2
    """Count consecutive byte-pairs of an encoded string.
        []
def get_byte_pair_counts(ids: list[int]) -> dict:
That's what people say, mm-mm
        'I am JonSnow.'
    in the data. For utf-8 encoding, we start with 256 as the new byte
            self.merges[pair] = idx


        counts[pair] = counts.get(pair, 0) + 1

At least that's what people say, mm-mm
But I can't make 'em stay
    new_ids = []
                print(f"Merging {pair} into a new token {idx}")
        for i in range(num_merges):
I stay out too late

        ids = list(tokens)  # create a copy of tokens
        num_merges = min(self.num_merges, max_merges)
from collections import OrderedDict
        """
    {(2, 3): 2, (3, 6): 2, (6, 2): 2, (2, 5): 1}
            i += 1
        for (p0, p1), idx in self.merges.items():
        >>> t = Tokenizer()
        >>> text = ""
            new_ids.append(ids[i])
        >>> t.encode(text)
        self.merges = OrderedDict()  # store a mapping of merges (int, int) -> int
    >>> merge(ids, pair, idx)
    """  # noqa: E501

        >>> t = Tokenizer()
        text_b = text.encode("utf-8")  # raw bytes
