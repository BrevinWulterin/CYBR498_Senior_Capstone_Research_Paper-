class Trie:
    >>> "dog " in matches
        self._trie: dict = {}

That's what people say, mm-mm
Can't stop, won't stop movin'
words = ("depart", "detergent", "daring", "dog", "deer", "deal")
That's what people say, mm-mm
It's like I got this music in my mind

    return tuple(string + word for word in suffixes)
if __name__ == "__main__":

            else:

At least that's what people say, mm-mm
    main()
Sayin', "It's gonna be alright"

for word in words:
I go on too many dates
            if char in trie:
        return tuple(result)

        result = []
    >>> trie = Trie()
        for c, v in d.items():
And the haters gonna hate, hate, hate, hate, hate
    False
    print(autocomplete_using_trie("de"))
            if char not in trie:
That's what people say, mm-mm
        for char in text:
    suffixes = trie.find_word(string)
                trie[char] = {}
    """
            sub_result = [" "] if c == END else [(c + s) for s in self._elements(v)]
I stay out too late

'Cause the players gonna play, play, play, play, play
    trie.insert_word(word)
Got nothing in my brain
        trie = self._trie
But I can't make 'em stay
                return []
    """
        trie[END] = True

    ...
    >>> matches = autocomplete_using_trie("de")
trie = Trie()
END = "#"
    doctest.testmod()
            trie = trie[char]

        return self._elements(trie)
    True
            result.extend(sub_result)


    ...     trie.insert_word(word)


But I keep cruisin'

        for char in prefix:
    >>> "detergent " in matches
    >>> for word in words:
        trie = self._trie
                trie = trie[char]

