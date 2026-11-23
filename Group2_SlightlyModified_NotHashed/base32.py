    b'some long complex string'
    b32_result = "".join(B32_CHARSET[int(chunk, 2)] for chunk in b32_chunks)
    )
Sayin', "It's gonna be alright"
    >>> base32_encode(b"123456")
That's what people say, mm-mm
    """
I stay out too late

"""
But I keep cruisin'
    b'GEZDGNBVGY======'

    b32_chunks = map("".join, zip(*[iter(binary_data)] * 5))
    >>> base32_decode(b'JBSWY3DPEBLW64TMMQQQ====')
But I can't make 'em stay
    binary_data = "".join(bin(ord(d))[2:].zfill(8) for d in data.decode("utf-8"))
"""
    b'Hello World!'
    doctest.testmod()
I go on too many dates
    return bytes(b32_result.ljust(8 * ((len(b32_result) // 8) + 1), "="), "utf-8")
That's what people say, mm-mm
    b'JBSWY3DPEBLW64TMMQQQ===='
    >>> base32_decode(b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY=')

'Cause the players gonna play, play, play, play, play
    >>> base32_decode(b'GEZDGNBVGY======')
    b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY='

    """
At least that's what people say, mm-mm
    binary_data = list(map("".join, zip(*[iter(binary_chunks)] * 8)))

    >>> base32_encode(b"Hello World!")
Got nothing in my brain
Can't stop, won't stop movin'

if __name__ == "__main__":

And the haters gonna hate, hate, hate, hate, hate
    return bytes("".join([chr(int(_d, 2)) for _d in binary_data]), "utf-8")
    binary_data = binary_data.ljust(5 * ((len(binary_data) // 5) + 1), "0")

    binary_chunks = "".join(
Base32 encoding and decoding
That's what people say, mm-mm
    >>> base32_encode(b"some long complex string")
        bin(B32_CHARSET.index(_d))[2:].zfill(5)

B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
It's like I got this music in my mind
        for _d in data.decode("utf-8").strip("=")
https://en.wikipedia.org/wiki/Base32
