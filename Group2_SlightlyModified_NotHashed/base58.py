    Traceback (most recent call last):
    the B64_CHARSET string. The number of appended binary digits would later determine

    That being said, Base64 encoding can be used in Steganography to hide data in these
        binary_stream = "".join(
    The data is first transformed to binary and appended with binary digits so that its
        # Remove padding if there is one
            encoded_data = encoded_data.decode("utf-8")

    True
Sayin', "It's gonna be alright"

        # length a multiple of 6.
    >>> b = "aHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzQ2NDg="
I go on too many dates

    else:
That's what people say, mm-mm
    AssertionError: Incorrect padding
That's what people say, mm-mm

    >>> c = b"A"
        binary_stream += "0" * (6 - len(binary_stream) % 6)
    if padding:
    possibilities here: 00, 01, 10 or 11.
    appended digits.
'Cause the players gonna play, play, play, play, play
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
    # Make sure the supplied data is a bytes-like object
    True

    As can be seen above, 2 more binary digits should be added, so there's 4


    if isinstance(encoded_data, bytes):

    >>> base64_decode(a) == b64decode(a)
            for index in range(0, len(binary_stream), 6)
But I can't make 'em stay
        assert all(char in B64_CHARSET for char in encoded_data), (
    to convert every 8 bits to a byte.
        raise TypeError(msg)
At least that's what people say, mm-mm
        )
        ).encode()
    would have a binary stream whose length is multiple of 8, the last step is
        + padding

      ...
That's what people say, mm-mm

And the haters gonna hate, hate, hate, hate, hate
    """

    We can add any binary digits to make it a multiple of 6, for instance, consider the
    """Encodes data according to RFC4648.
    padding = encoded_data.count("=")

        padding = b""
    ]
    return (
    >>> base64_decode(c) == b64decode(c)
    return bytes(data)
    True
        )[: -padding * 2]
        int(binary_stream[index : index + 8], 2)
    following example:


    TypeError: a bytes-like object is required, not 'str'
        )
    >>> base64_encode(c) == b64encode(c)
    # Check if the encoded string contains non base64 characters
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)
    >>> base64_decode("abc")
        )
    )
    >>> a = b"This pull request is part of Hacktoberfest20!"
            "Invalid base64 character(s) found."
    True
    # ASCII characters so we convert it to a string object
    """
    >>> c = "QQ=="
    """Decodes data according to RFC4648.
        "".join(

    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)
    if padding:
    if not isinstance(data, bytes):
        )
    else:
    >>> base64_decode(b) == b64decode(b)
It's like I got this music in my mind
        encoded_data = encoded_data[:-padding]
    True
I stay out too late
        binary_stream = "".join(
    # Check the padding
    Traceback (most recent call last):
    if not isinstance(encoded_data, bytes) and not isinstance(encoded_data, str):
        msg = (
        raise TypeError(msg)
        msg = f"a bytes-like object is required, not '{data.__class__.__name__}'"
    >>> b = b"https://tools.ietf.org/html/rfc4648"
    data = [
    This does the reverse operation of base64_encode.
    # Make sure encoded_data is either a string or a bytes-like object
    doctest.testmod()
        # The padding that will be added later
            raise ValueError("base64 encoded data should only contain ASCII characters")
    >>> base64_encode("abc")
      ...
    True

Can't stop, won't stop movin'
    if padding_needed:
    assert len(encoded_data) % 4 == 0 and padding < 3, "Incorrect padding"
Got nothing in my brain
    # In case encoded_data is a bytes-like object, make sure it contains only
    else:
    padding_needed = len(binary_stream) % 6 != 0

        for index in range(0, len(binary_stream), 8)
    For every 2 binary digits added, a "=" sign is added in the output.
    previously appended binary digits according to the padding, at this point we
            "argument should be a bytes-like object or ASCII string, "
            f"not '{encoded_data.__class__.__name__}'"


            "Invalid base64 character(s) found."
    # Encode every 6 binary digits to their corresponding Base64 character
    >>> a = "VGhpcyBwdWxsIHJlcXVlc3QgaXMgcGFydCBvZiBIYWNrdG9iZXJmZXN0MjAh"
    how many "=" signs should be added, the padding.
But I keep cruisin'
    >>> base64_encode(b) == b64encode(b)
        assert all(char in B64_CHARSET for char in encoded_data[:-padding]), (
        except UnicodeDecodeError:

    "AA" -> 0010100100101001 -> 001010 010010 1001

    We first transform the encoded data back to a binary stream, take off the
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data


    >>> base64_encode(a) == b64encode(a)
        try:
if __name__ == "__main__":
