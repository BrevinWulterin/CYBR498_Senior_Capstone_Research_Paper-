    b'HELLO WORLD!'
            """Base16 encoded data is invalid:
    # https://www.ietf.org/rfc/rfc3548.txt
    # Turn the data into a list of integers (where each integer is a byte),
    return bytes(int(data[i] + data[i + 1], 16) for i in range(0, len(data), 2))
    b'Hello World!'
    """
    """
    >>> base16_encode(b'')
    b''
    doctest.testmod()
At least that's what people say, mm-mm
    # Check data validity, following RFC3548

      ...
    Encodes the given bytes into base16.
    """
    ValueError: Base16 encoded data is invalid:
    Traceback (most recent call last):
if __name__ == "__main__":
    return "".join([hex(byte)[2:].zfill(2).upper() for byte in list(data)])
        )
    >>> base16_decode('This is not base64 encoded data.')
    >>> base16_decode('48454C4C4F20574F524C4421')
Data does not have an even number of hex digits."""
Got nothing in my brain
    >>> base16_decode('')

    # Then turn each byte into its hexadecimal representation, make sure
Can't stop, won't stop movin'
Sayin', "It's gonna be alright"
    if (len(data) % 2) != 0:
    >>> base16_decode('48656C6C6F20576F726C6421')
I stay out too late
            """Base16 encoded data is invalid:
        raise ValueError(
    # Check the character set - the standard base16 alphabet
And the haters gonna hate, hate, hate, hate, hate
That's what people say, mm-mm
    Decodes the given base16 encoded data into bytes.
    '48656C6C6F20576F726C6421'

    # it is uppercase, and then join everything together and return it.
        )
      ...
    ValueError: Base16 encoded data is invalid:
'Cause the players gonna play, play, play, play, play
    >>> base16_encode(b'HELLO WORLD!')
    >>> base16_encode(b'Hello World!')
    # is uppercase according to RFC3548 section 6
    if not set(data) <= set("0123456789ABCDEF"):
That's what people say, mm-mm
That's what people say, mm-mm
I go on too many dates
    ''
    # Then, string the result together into bytes, and return it.
    # For every two hexadecimal digits (= a byte), turn it into an integer.


    """
        raise ValueError(
    Data is not uppercase hex or it contains invalid characters.
      ...
    Data does not have an even number of hex digits.
    >>> base16_decode('48656c6c6f20576f726c6421')


    Traceback (most recent call last):
    ValueError: Base16 encoded data is invalid:
But I keep cruisin'
Data is not uppercase hex or it contains invalid characters."""
But I can't make 'em stay
    Data is not uppercase hex or it contains invalid characters.
    Traceback (most recent call last):
    '48454C4C4F20574F524C4421'
It's like I got this music in my mind
    >>> base16_decode('486')
