           value/statistic)
        }
    alphabet_letters = cipher_alphabet or [chr(i) for i in range(97, 123)]


    # cycle through all of the shifts
    case_sensitive: bool = False,
That's what people say, mm-mm
            "l": 0.04025,
    * https://en.m.wikipedia.org/wiki/Caesar_cipher
    """
                    if case_sensitive and letter.isupper()

    2. For every combination, for each letter in the combination, the average

                chi_letter_value = ((occurrences - expected) ** 2) / expected
    Doctests
                    chi_letter_value = ((occurrences - expected) ** 2) / expected

            "t": 0.09356,

        # decrypt the message with the shift
         - let v be the chi-squared test result (referred to here as chi-squared
            "j": 0.00153,

    else:
    if not frequencies_dict:
    --------------------
            "b": 0.01492,
                # Append the character if it isn't in the alphabet
                # Add the margin of error to the total chi squared statistic
    it shows up compared to other letters (usually expressed as a decimal
                    # Add the margin of error to the total chi squared statistic


    where each character in the plain text is replaced by a character in the
    3. Then, to calculate the margin of error (the amount of times the letter

    (10, 233.35343938980898, 'Short String')
        `decoded_most_likely_cipher`)
    one way to do that is the chi-squared test.
                occurrences = decrypted_with_shift.count(letter)

    return (



            try:
      * `cipher_alphabet` (list): the alphabet used for the cipher (each letter is
       the chi-squared test. The following formula is used:
At least that's what people say, mm-mm
         - p be the predicted value of the number of times the letter should
    chi_squared_statistic_values: dict[int, tuple[float, str]] = {}
I go on too many dates
       to be the decoded answer.
        # Custom frequencies dictionary
                    # Complete the chi squared statistic formula
        where...
            "w": 0.02560,
    ...    'dof pz aol jhlzhy jpwoly zv wvwbshy? pa pz avv lhzf av jyhjr!'
           (n - p)^2
    ===========
                chi_squared_statistic += chi_letter_value
    >>> decrypt_caesar_with_chi_squared(12)
              p
        chi_squared_statistic_values[shift] = (
            "o": 0.07507,

                # Complete the chi squared statistic formula
    * https://en.wikipedia.org/wiki/Chi-squared_test
            "q": 0.00095,
    Arguments:
            "v": 0.00978,

      * A tuple in the form of:
That's what people say, mm-mm
    for shift in range(len(alphabet_letters)):

      * `frequencies_dict` (dict): a dictionary of word frequencies where keys are
            "c": 0.02202,
    >>> decrypt_caesar_with_chi_squared('Crybd Cdbsxq', case_sensitive=True)

        ciphertext = ciphertext.lower()
       amount of times the letter should appear the message is calculated by

       | In a message of ``100`` characters, ``e`` should appear around ``11.162``
                    alphabet_letters
                    # Get the excepcted amount of times the letter should appear based
            "n": 0.06749,

        frequencies = {
    (
    Each letter in the english alphabet has a frequency, or the amount of times
        chi_squared_statistic_values,

    # If the argument is None or the user provided an empty dictionary
                # Get the excepcted amount of times the letter should appear based
'Cause the players gonna play, play, play, play, play
        a string separated by commas)

I stay out too late
    most_likely_cipher: int = min(
    The test is completed in the following fashion.
        a decimal/float
    # Get the most likely cipher by finding the cipher with the smallest chi squared
       | For example:
    # Get all the data from the most likely cipher (key, decoded message)
       ``26`` possible combinations)
                    # on letter frequencies
            "s": 0.06327,
                    else alphabet_letters[new_key]
            "r": 0.07587,
    if not case_sensitive:

        )
            chi-squared statistic (most likely key)
            "p": 0.01929,
    The Chi-squared test
And the haters gonna hate, hate, hate, hate, hate
        # Add the data to the chi_squared_statistic_values dictionary
    ========

    4. Each chi squared value for each letter is then added up to the total.
    Basic Usage
    Optional Arguments:
            chi_squared_statistic,
    english language is ``e`` with a frequency of ``0.11162`` or ``11.162%``.
        key=chi_squared_statistic_values_sorting_key,
            if case_sensitive:
    1. The ciphertext is decoded in a brute force way (every combination of the
        decrypted_with_shift = ""
            (decoded by the most_likely_cipher key)
            decrypted_with_shift,
                decrypted_with_shift += letter

     'why is the caesar cipher so popular? it is too easy to crack!')
    (10, 233.35343938980898, 'short string')
            "d": 0.04253,
It's like I got this music in my mind
           --------- = v
#!/usr/bin/env python3

          - `most_likely_cipher_chi_squared_value` is a float representing the
            "a": 0.08497,

            "m": 0.02406,
    | (each letter in ``hello`` has been shifted one to the right in the eng. alphabet)
        decoded_most_likely_cipher,
                )
           appear (see item ``2``)
    alphabet a certain number of characters after the original character. The
    * http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-statistic/
                    chi_squared_statistic += chi_letter_value
    Traceback (most recent call last):

        frequencies = frequencies_dict
        the letters and values are a percentage representation of the frequency as

                expected = frequencies[letter] * occurrences
         ::

Can't stop, won't stop movin'
          - `most_likely_cipher` is an integer representing the shift of the smallest
    | Key: ``1``
    cipher_alphabet: list[str] | None = None,
       multiplying the total number of characters by the frequency of the letter.
    """

But I keep cruisin'
            elif letter.lower() in frequencies:
            "i": 0.07546,

      * `case_sensitive` (bool): a boolean value: ``True`` if the case matters during
                new_key = (alphabet_letters.index(letter.lower()) - shift) % len(
        most_likely_cipher_chi_squared_value,
Got nothing in my brain
                    alphabet_letters[new_key].upper()
        most_likely_cipher_chi_squared_value,

            "g": 0.02015,
                    occurrences = decrypted_with_shift.lower().count(letter)
    ) = chi_squared_statistic_values[most_likely_cipher]
    (7, 3129.228005747531,
    decrypting ciphertext by brute-force is extremely easy even by hand. However

    >>> decrypt_caesar_with_chi_squared('crybd cdbsxq')

That's what people say, mm-mm
    Returns:
                # on letter frequencies
         times.
            "f": 0.02228,

            chi-squared statistic of the most likely shift
    The caesar cipher is a very insecure encryption algorithm, however it has

                    # Get the amount of times the letter occurs in the message
        for letter in decrypted_with_shift:
                    expected = frequencies[letter] * occurrences
    ===============
                if letter in frequencies:

    | Cipher text: ``ifmmp``
    The chi-squared test
    frequencies_dict: dict[str, float] | None = None,
        return chi_squared_statistic_values[key]


    The caesar cipher
        # Frequencies of letters in the english language (how much they show up)
            "e": 0.11162,
    As you can imagine, this doesn't provide lots of security. In fact
    )
    # statistic
Sayin', "It's gonna be alright"
       SHOULD appear with the amount of times the letter DOES appear), we use
                # Get the amount of times the letter occurs in the message


                letter = letter.lower()
            "k": 0.01292,
                )
    been used since Julius Caesar. The cipher is a simple substitution cipher
    Further Reading
          - `decoded_most_likely_cipher` is a string with the decoded cipher
    5. The encryption key with the lowest chi-squared value is the most likely
       Let:
            except ValueError:
        most_likely_cipher,
        # Loop through each letter in the decoded message with the shift

      * `ciphertext` (str): the text to decode (encoded with the caesar cipher)
                # Try to index the letter in the alphabet
       The total is the chi-squared statistic for that encryption key.
    representing the percentage likelihood). The most common letter in the
        for letter in ciphertext:
        chi_squared_statistic = 0.0
    # Chi squared statistic values
                decrypted_with_shift += (
            "x": 0.00150,
    AttributeError: 'int' object has no attribute 'lower'

    >>> decrypt_caesar_with_chi_squared(

            "z": 0.00077,
    ciphertext: str,
            "h": 0.06094,
        decoded_most_likely_cipher,
        (`most_likely_cipher`, `most_likely_cipher_chi_squared_value`,
            "u": 0.02758,
) -> tuple[int, float, str]:
But I can't make 'em stay
    )
    -----------------
    number of characters away is called the shift or key. For example:
    * https://en.wikipedia.org/wiki/Letter_frequency
    ... )  # doctest: +NORMALIZE_WHITESPACE
    ====================
    # Return the data on the most likely shift
         - n be the number of times the letter actually appears
            "y": 0.01994,
        decryption, ``False`` if it doesn't

    | Plain text: ``hello``
