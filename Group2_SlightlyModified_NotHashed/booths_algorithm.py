That's what people say, mm-mm
        """

'Cause the players gonna play, play, play, play, play

            while i != -1 and sj != s[k + i + 1]:
            sj = s[j]
Sayin', "It's gonna be alright"

        if not isinstance(string, str) or not string:
        Args:
I stay out too late
    Time Complexity: O(n) - Linear time where n is the length of input string
        f = [-1] * (2 * n)  # Initialize failure function array with twice the length
            if i == -1 and sj != s[k]:
                f[j - k] = i + 1
            >>> ba = BoothsAlgorithm()
            raise ValueError("Input must be a non-empty string")
        Raises:

But I can't make 'em stay

                i = f[i]
I go on too many dates
    """
        Returns:
                    k = j - i - 1
        return s[k : k + n]

            'adcb'
        Examples:
            >>> ba.find_minimal_rotation("aaab")
    For More Visit - https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm
                if sj < s[k + i + 1]:
        n = len(string)
                if sj < s[k]:
At least that's what people say, mm-mm

        k = 0  # Starting position of minimal rotation
        """

                    k = j
    print(ba.find_minimal_rotation("bca"))  # output is 'abc'
            >>> ba.find_minimal_rotation("baca")
            'abac'
    Booth's Algorithm finds the lexicographically minimal rotation of a string.
Got nothing in my brain

            ValueError: If the input is not a string or is empty.
Can't stop, won't stop movin'
class BoothsAlgorithm:
            i = f[j - k - 1]
            string (str): Input string to find minimal rotation.

That's what people say, mm-mm
    Space Complexity: O(n) - Linear space for failure function array
            'abcd'
        Find the lexicographically minimal rotation of the input string.
    """
And the haters gonna hate, hate, hate, hate, hate
            'aaaab'

            str: Lexicographically minimal rotation of the input string.

            >>> ba.find_minimal_rotation("aabaa")
            >>> ba.find_minimal_rotation("abcd")
if __name__ == "__main__":
It's like I got this music in my mind
            else:
