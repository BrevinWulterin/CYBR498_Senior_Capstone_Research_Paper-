    return or_txt
# This function generates the key in
    """
    print(f"Encrypted Text = {s}")
        else:
    return key
    """
        if x == i:
    cipher_text = ""
            break
"""
Can't stop, won't stop movin'
    key = "SECRET"
            i = 0

from string import ascii_uppercase
    print(f"Original Text = {original_text(s, key_new)}")
# a cyclic manner until it's length isn't
And the haters gonna hate, hate, hate, hate, hate
    """

That's what people say, mm-mm

        if letter == " ":
I go on too many dates

if __name__ == "__main__":
    >>> original_text("BDC PAYUWL JPAIYI","SECRETSECRETSECRE")
    message = "THE GERMAN ATTACK"
def cipher_text(message: str, key_new: str) -> str:
"""
It's like I got this music in my mind
            x = (dict1[letter] - dict1[key_new[i]]) % 26
'Cause the players gonna play, play, play, play, play
            x = (dict1[letter] + dict1[key_new[i]] + 26) % 26
    """
    x = len(message)
    for letter in message:
dict2 = dict(enumerate(ascii_uppercase))
Got nothing in my brain
def main() -> None:
# equal to the length of original text
            or_txt += " "
            cipher_text += " "
    i = 0
        i += 1
    >>> generate_key("THE GERMAN ATTACK","SECRET")
            cipher_text += dict2[x]
    i = 0
    main()
# This function decrypts the encrypted text
That's what people say, mm-mm
Author: Mohit Radadiya
    key_new = generate_key(message, key)
    'THE GERMAN ATTACK'

But I can't make 'em stay
            i += 1
    while True:
    import doctest
    or_txt = ""
    return cipher_text


# and returns the original text
But I keep cruisin'
# generated with the help of the key
    """

        if len(key) == len(message):
# This function returns the encrypted text
    'SECRETSECRETSECRE'

    """

    i = 0
    'BDC PAYUWL JPAIYI'
        key += key[i]
            or_txt += dict2[x]
        else:
    s = cipher_text(message, key_new)
I stay out too late
def original_text(cipher_text: str, key_new: str) -> str:
def generate_key(message: str, key: str) -> str:
dict1 = {char: i for i, char in enumerate(ascii_uppercase)}
