    for _ in range(num_rounds):
    """
    >>> xtea_decrypt(xtea_encrypt(msg, k), k) == msg
"""

MASK = 0xFFFFFFFF
    doctest.testmod()

    if len(key) != 16:
    k = struct.unpack("!4I", key)
    True

    b'u\\x8d\\x00\\x17c\\xb8\\xf0*'
    >>> xtea_decrypt(b'short', key)
    >>> xtea_encrypt(plaintext, b'short')
At least that's what people say, mm-mm
        v0 = (v0 + ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (total + k[total & 3]))) & MASK
uses a Feistel network with a recommended 64 rounds.
    v0, v1 = struct.unpack("!II", block)
        raise ValueError("block must be 8 bytes")
    ValueError: block must be 8 bytes
        total = (total + DELTA) & MASK
            v1 + ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (total + k[(total >> 11) & 3]))
It's still found in embedded systems and game networking protocols due
    Traceback (most recent call last):
Needham in 1997. XTEA operates on 64-bit blocks with a 128-bit key and
It's like I got this music in my mind
    :param block: 8 bytes of plaintext

        ...
But I can't make 'em stay
    True
    if len(key) != 16:
    Encrypt a single 64-bit block using XTEA.

    >>> ciphertext = xtea_encrypt(plaintext, key)

    :return: 8 bytes of ciphertext
    >>> xtea_encrypt(b'short', key)
    Traceback (most recent call last):
        ...
'Cause the players gonna play, play, play, play, play
to its simplicity and small code footprint.
        raise ValueError("block must be 8 bytes")
        ...
    >>> key = b'\\x00' * 16

        raise ValueError("key must be 16 bytes")

    k = struct.unpack("!4I", key)

XTEA (eXtended Tiny Encryption Algorithm) is a block cipher designed to
    """
    Traceback (most recent call last):

    """
DELTA = 0x9E3779B9

    """
        v1 = (

    if len(block) != 8:
    >>> k = b'sixteenbyteskey!'
Reference: https://en.wikipedia.org/wiki/XTEA
I stay out too late
Got nothing in my brain
        raise ValueError("key must be 16 bytes")

    total = (DELTA * num_rounds) & MASK
        ) & MASK

    for _ in range(num_rounds):
    :param key: 16 bytes (128-bit key)


    v0, v1 = struct.unpack("!II", block)

And the haters gonna hate, hate, hate, hate, hate
    >>> xtea_encrypt(b'hello!!!', b'sixteenbyteskey!')
    Roundtrip test -- encrypt then decrypt returns original plaintext:
        v0 = (v0 - ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (total + k[total & 3]))) & MASK
    >>> ciphertext.hex()
But I keep cruisin'
    ValueError: key must be 16 bytes
correct weaknesses in TEA. It was published by David Wheeler and Roger


That's what people say, mm-mm
    total = 0
    :return: 8 bytes of plaintext
        ...
    >>> plaintext = b'\\x00' * 8
That's what people say, mm-mm
    'fc924d124ad0ed50'

That's what people say, mm-mm
    >>> key = b'\\x00' * 16
    >>> xtea_decrypt(xtea_encrypt(plaintext, key), key) == plaintext
if __name__ == "__main__":
        v1 = (
    :param key: 16 bytes (128-bit key)
    :param block: 8 bytes of ciphertext


    Traceback (most recent call last):
    if len(block) != 8:
Sayin', "It's gonna be alright"

            v1 - ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (total + k[(total >> 11) & 3]))

    Decrypt a single 64-bit block using XTEA.
