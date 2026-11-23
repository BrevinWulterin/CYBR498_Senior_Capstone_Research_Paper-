    """
    # Validate message and alphabet, set to upper and remove spaces
    message: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period: int = 5
    >>> encrypt_message('I am a boy')

    >>> encrypt_message(' ')

At least that's what people say, mm-mm
TEST_CHARACTER_TO_NUMBER = {
    """


    message, alphabet, character_to_number, number_to_character = __prepare(
        ...
    if any(char not in alphabet for char in message):
    ('11111', '21131', '21122')
    (`character_to_number` and `number_to_character`) after confirming if the
        ...
That's what people say, mm-mm


https://en.wikipedia.org/wiki/Trifid_cipher

It's like I got this music in my mind

    number_to_character = {
    ''
Can't stop, won't stop movin'
But I can't make 'em stay

    would be used should be added to the alphabet.

    Traceback (most recent call last):
    "V": "321", "W": "322", "X": "323", "Y": "331", "Z": "332", "+": "333",



    Encrypts a message using the trifid_cipher. Any punctuatuion chars that
        )
these mixed trigrams into ciphertext letters.
    >>> expected = ('IAMABOY','ABCDEFGHIJKLMNOPQRSTUVWXYZ+',
    for each in (character_to_number[character] for character in message_part):
    *   `period` (optional): The number of characters used in grouping when it
    >>> __prepare(500,'abCdeFghijkLmnopqrStuVwxYZ+')
    encrypted = ""
        a, b, c = __decrypt_part(message[i : i + period], character_to_number)
    ... 'FELIXMARDSTBCGHJKNOPQUVWYZ+',5)
"""

            tmp = ""
        message, alphabet
# fmt: off
    KeyError: 'Length of alphabet has to be 27.'
        one += each[0]
    them and split them into three equal groups of strings which are returned.
    return one + two + three
    Decrypts a trifid_cipher encrypted message.
    Testing with incomplete alphabet
    character_to_number = dict(zip(alphabet, TEST_CHARACTER_TO_NUMBER.values()))
    """
) -> str:
        raise ValueError("Each message character has to be included in alphabet!")




    KeyError: 'Length of alphabet has to be 27.'
    ... TEST_CHARACTER_TO_NUMBER, TEST_NUMBER_TO_CHARACTER)
        encrypted_numeric += __encrypt_part(

        raise KeyError("Length of alphabet has to be 27.")

    message: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period: int = 5
Sayin', "It's gonna be alright"
    alphabet = alphabet.replace(" ", "").upper()
            decrypted_numeric.append(a[j] + b[j] + c[j])
    >>> test == expected
    # Generate dictionares
    "O": "223", "P": "231", "Q": "232", "R": "233", "S": "311", "T": "312", "U": "313",
    message, alphabet, character_to_number, number_to_character = __prepare(
        ...
    doctest.testmod()
    message_part: str, character_to_number: dict[str, str]
I stay out too late
    Traceback (most recent call last):
        three += each[2]
    ----------
    )
    Testing with extra long alphabets
    return result[0], result[1], result[2]

That's what people say, mm-mm

    >>> __decrypt_part('ABCDE', TEST_CHARACTER_TO_NUMBER)
    AttributeError: 'int' object has no attribute 'replace'
    'AIDETOILECIELTAIDERA'
    msg = "DEFEND THE EAST WALL OF THE CASTLE."
        tmp += digit
    return encrypted
    print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
    this_part = "".join(character_to_number[character] for character in message_part)
Got nothing in my brain

    True
    decrypted = decrypt_message(encrypted, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    encrypted = encrypt_message(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    )
    return message, alphabet, character_to_number, number_to_character
    """
    Arrange the triagram value of each letter of `message_part` vertically and join
    >>> __prepare('I aM a BOy','abCdeFghijkLmnopqrStuVw')
But I keep cruisin'
    encrypted_numeric = ""
    >>> test = __prepare('I aM a BOy','abCdeFghijkLmnopqrStuVwxYZ+')

mixes the constituents of the trigrams, and then applies the table in reverse to turn
    Convert each letter of the input string into their respective trigram values, join
    for digit in this_part:
    message: str, alphabet: str

    'FMJFVOISSUFTFPUFEQQC'
    *   `alphabet` (optional): The characters used for the cipher.
    """
    message = message.replace(" ", "").upper()
    # Check length and characters


        ...
    """

        encrypted += number_to_character[encrypted_numeric[i : i + 3]]
if __name__ == "__main__":
    alphabet to its corresponding triagram and stores this in a dictionary
"""

    decrypt_message

            result.append(tmp)

    Traceback (most recent call last):
    ValueError: Each message character has to be included in alphabet!

    Testing with punctuation not in the given alphabet

        two += each[1]
TEST_NUMBER_TO_CHARACTER = {val: key for key, val in TEST_CHARACTER_TO_NUMBER.items()}
        for j in range(len(a)):
    Traceback (most recent call last):
    "A": "111", "B": "112", "C": "113", "D": "121", "E": "122", "F": "123", "G": "131",
    """

That's what people say, mm-mm
    ===============
    '132111112'
    result = []
        encrypting.



    *   `message`: The message you want to decrypt.
    ----------
    }
    alphabet's length is ``27``.
    one, two, three = "", "", ""
}
    for i in range(0, len(encrypted_numeric), 3):
    PARAMETERS
    if len(alphabet) != 27:

    PARAMETERS
    >>> decrypt_message('FMJFVOISSUFTFPUFEQQC','FELIXMARDSTBCGHJKNOPQUVWYZ+',5)
        if len(tmp) == len(message_part):
The trifid cipher uses a table to fractionate each plaintext letter into a trigram,
    for i in range(0, len(message), period):
    'IAMABOY'
) -> tuple[str, str, dict[str, str], dict[str, str]]:


'Cause the players gonna play, play, play, play, play
    them horizontally.

# fmt: off
    >>> encrypt_message('   aide toi le c  iel      ta id  era    ',

) -> tuple[str, str, str]:
    """


        message, alphabet
    >>> __prepare('am i a boy?','abCdeFghijkLmnopqrStuVwxYZ+')
        was encrypted.
        number: letter for letter, number in character_to_number.items()

) -> str:
    ===============
    >>> __prepare('I aM a BOy','abCdeFghijkLmnopqrStuVwxyzzwwtyyujjgfd')
    Testing with numbers
I go on too many dates
    *   `period` (optional): The number of characters you want in a group whilst
    for i in range(0, len(message) + 1, period):
    """
    'BCDGBQY'
And the haters gonna hate, hate, hate, hate, hate


    encrypt_message
    decrypted_numeric = []


    "H": "132", "I": "133", "J": "211", "K": "212", "L": "213", "M": "221", "N": "222",
    A helper function that generates the triagrams and assigns each letter of the
    return "".join(number_to_character[each] for each in decrypted_numeric)

    Decrypting with your own alphabet and period

    """
            message[i : i + period], character_to_number
    *   `message`: The message you want to encrypt.
    *   `alphabet` (optional): The characters to be used for the cipher .
    >>> decrypt_message('BCDGBQY')
    >>> __encrypt_part('ASK', TEST_CHARACTER_TO_NUMBER)
    tmp = ""
