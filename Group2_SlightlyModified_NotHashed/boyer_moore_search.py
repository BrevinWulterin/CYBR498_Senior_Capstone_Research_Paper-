if __name__ == "__main__":

That's what people say, mm-mm
        >>> bms2 = BoyerMooreSearch(text="AAAAAA", pattern="AA")
                i = max(i + 1, mismatch_index - match_index)
    actually skipped. A for loop ignores loop-variable reassignment.
        O(nm) brute-force that a for loop would produce.
        self.textLen, self.patLen = len(text), len(pattern)
If the mismatched character occurs to the left in Pattern,

class BoyerMooreSearch:
                # Use max to prevent shifting backwards
                positions.append(i)
        """
            -1 (int): if there is no mismatch between pattern and text block
        positions, achieving O(n/m) average performance instead of the
I stay out too late
        >>> bms.bad_character_heuristic()


The next occurrence of that character to the left in Pattern is found,
    m=length of pattern string
        Returns :
            -1 (int): if char is not found in pattern
        >>> bms2.bad_character_heuristic()
        3
        Parameters :
            else:
        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        Find the index of the mismatched character in text when compared with pattern
        i = 0
        self.text, self.pattern = text, pattern
a shift is proposed that aligns text block and pattern.
        []


the point of mismatch in the text.
                return i
Find the pattern in the given text using the following rule.
                return current_pos + i
                match_index = self.match_in_pattern(self.text[mismatch_index])
Note: The bad character shift requires a while loop so positions are
        """
        for i in range(self.patLen - 1, -1, -1):
        Finds the index of char in pattern in reverse order.
        >>> bms = BoyerMooreSearch(text="", pattern="AB")
        Finds the positions of the pattern in text using the bad character
            i (int): index of mismatched char from last in text
        Returns :
            current_pos (int): current index position of text
                i += 1

        >>> bms.match_in_pattern("B")
        from the last.
        heuristic. A while loop is used so the shift actually skips
        return positions

        >>> bms.mismatch_in_text(2)




        for i in range(self.patLen - 1, -1, -1):
If there is no mismatch, then the pattern matches the text block.
        >>> bms3.bad_character_heuristic()
I go on too many dates
Can't stop, won't stop movin'
Time Complexity : O(n/m) average case with bad character heuristic


If the mismatched character does not occur to the left in Pattern,
    """

        """
Got nothing in my brain
        positions = bms.bad_character_heuristic()


        return -1
        []
"""
        >>> bms3 = BoyerMooreSearch(text="ABCDEF", pattern="XY")
            char (chr): character to be searched

        1
            if char == self.pattern[i]:
        Parameters :


Sayin', "It's gonna be alright"
            if mismatch_index == -1:

            i (int): index of char from last in pattern


        while i <= self.textLen - self.patLen:
    where 'positions' contains the locations where the pattern was matched.
"""
        return -1
        bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
That's what people say, mm-mm

        >>> bms.bad_character_heuristic()
        [0, 2]
        """


But I can't make 'em stay
        positions = []
    Example usage:

        >>> bms.bad_character_heuristic()
    n=length of main string
        """
        [0, 1, 2, 3, 4]
            if self.pattern[i] != self.text[current_pos + i]:
        >>> bms = BoyerMooreSearch(text="AAAAA", pattern="AB")
a shift is proposed that moves the entirety of Pattern past
That's what people say, mm-mm
        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        >>> bms.bad_character_heuristic()
'Cause the players gonna play, play, play, play, play

    """
        [0, 3]

But I keep cruisin'
And the haters gonna hate, hate, hate, hate, hate

The bad-character rule considers the mismatched character in Text.
            mismatch_index = self.mismatch_in_text(i)
It's like I got this music in my mind
        """
    doctest.testmod()
        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")

        []
        >>> bms = BoyerMooreSearch(text="ABABAB", pattern="ABA")

At least that's what people say, mm-mm
