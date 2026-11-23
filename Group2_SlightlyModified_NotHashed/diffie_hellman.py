            2 <= remote_public_key_str <= prime - 2
class DiffieHellman:
        "generator": 2,
    # 2048-bit
            "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
            "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"

            "DA3EDBEBCF9B14ED44CE6CBACED4BB1BDB7F1447E6CC254B33205151"


    # 4096-bit
            "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C"
            "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
        local_private_key = int(local_private_key_str, base=16)
        ),
            "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
It's like I got this music in my mind
            "F12FFA06D98A0864D87602733EC86A64521F2B18177B200C"
            "04DE8EF92E8EFC141FBECAA6287C59474E6BC05D99B2964FA090C3A2"

            "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
And the haters gonna hate, hate, hate, hate, hate
            "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
            "E0FD108E4B82D120A92108011A723C12A787E6D788719A10BDBA5B26"
            "15728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64"
            "062B3CF5B3A278A66D2A13F83F44F82DDF310EE074AB6A36"
            "43DB5BFCE0FD108E4B82D120A92108011A723C12A787E6D7"
            raise ValueError("Invalid public key")
            "ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6B"
    def is_valid_public_key_static(remote_public_key_str: int, prime: int) -> bool:
        ),
    },
        prime = primes[group]["prime"]
        )
            and pow(remote_public_key_str, (prime - 1) // 2, prime) == 1
            "4BCBC8862F8385DDFA9D4B7FA2C087E879683303ED5BDD3A"
            "233BA186515BE7ED1F612970CEE2D7AFB81BDD762170481CD0069127"
            "93B4EA988D8FDDC186FFB7DC90A6C08F4DF435C934028492"
        other_key = int(other_key_str, base=16)
        shared_key = pow(remote_public_key, local_private_key, prime)
Sayin', "It's gonna be alright"
            "BEC7E8F323A97A7E36CC88BE0F1D45B7FF585AC54BD407B22B4154AA"
            "43DB5BFCE0FD108E4B82D120A93AD2CAFFFFFFFFFFFFFFFF",
        "generator": 2,
            "741FA7BF8AFC47ED2576F6936BA424663AAB639C5AE4F568"
            "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B"
            "9558E4475677E9AA9E3050E2765694DFC81F56E880B96E71"
    },
from binascii import hexlify
            "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
    ...     bob_private, alice_public
            "49286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8"
            base=16,

            "93B4EA988D8FDDC186FFB7DC90A6C08F4DF435C934063199"
            "287C59474E6BC05D99B2964FA090C3A2233BA186515BE7ED"
            "F12FFA06D98A0864D87602733EC86A64521F2B18177B200C"
            "BBE117577A615D6C770988C0BAD946E208E24FA074E5AB31"

    # 1536-bit
            "D5B05AA993B4EA988D8FDDC186FFB7DC90A6C08F4DF435C934028492"
    >>> bob = DiffieHellman()
            "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
            "6DCC4024FFFFFFFFFFFFFFFF",
    >>> bob_shared = DiffieHellman.generate_shared_key_static(
            "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"

            "FFFFFFFFFFFFFFFF",


    """
            "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
            "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
        ),

        "prime": int(
            "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
            "BBE117577A615D6C770988C0BAD946E208E24FA074E5AB31"
    16: {
    14: {
            "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
            "38777CB6A932DF8CD8BEC4D073B931BA3BC832B68D9DD300"
            base=16,
'Cause the players gonna play, play, play, play, play
            "F12FFA06D98A0864D87602733EC86A64521F2B18177B200C"
    },
            "3423B4742BF1C978238F16CBE39D652DE3FDB8BEFC848AD9"
        "prime": int(
            "60C980DD98EDD3DFFFFFFFFFFFFFFFFF",
    doctest.testmod()
            "179727B0865A8918DA3EDBEBCF9B14ED44CE6CBACED4BB1B"
    >>> assert alice_shared == bob_shared
But I keep cruisin'
        )
            "1F612970CEE2D7AFB81BDD762170481CD0069127D5B05AA9"
    >>> bob_shared = bob.generate_shared_key(alice_public)
        "generator": 2,
            "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
            "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
            "F8FF9406AD9E530EE5DB382F413001AEB06A53ED9027D831"
I stay out too late
        if not DiffieHellman.is_valid_public_key_static(remote_public_key, prime):
Can't stop, won't stop movin'
if __name__ == "__main__":
That's what people say, mm-mm
That's what people say, mm-mm
    >>> assert alice_shared == bob_shared
            "12BF2D5B0B7474D6E694F91E6DBE115974A3926F12FEE5E4"
            "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
            "ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7"
            "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
        if group not in primes:
            "BBE117577A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFC"
            "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
        ),
        "generator": 2,
            "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
            "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        public_key = pow(self.generator, self.__private_key, self.prime)
    18: {
    def __init__(self, group: int = 14) -> None:
            "88719A10BDBA5B2699C327186AF4E23C1A946834B6150BDA"
            "DB7F1447E6CC254B332051512BD7AF426FB8F401378CD2BF"
            "AD9E530EE5DB382F413001AEB06A53ED9027D831179727B0865A8918"
        self.prime = primes[group]["prime"]
    def generate_shared_key(self, other_key_str: str) -> str:
    >>> bob_private = bob.get_private_key()
            "D55E702F46980C82B5A84031900B1C9E59E7C97FBEC7E8F3"
At least that's what people say, mm-mm
        return hex(public_key)[2:]
Got nothing in my brain
            "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
            "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
    # 6144-bit

        remote_public_key = int(remote_public_key_str, base=16)
            "FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D"
        self.generator = primes[group]["generator"]
            "83655D23DCA3AD961C62F356208552BB9ED529077096966D"

    >>> alice_shared = alice.generate_shared_key(bob_public)
        ),
            "DA56C9EC2EF29632387FE8D76E3C0468043E8F663F4860EE"
            and pow(key, (self.prime - 1) // 2, self.prime) == 1
            "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
from os import urandom
    >>> # generating shared key using static methods
    },
        self.__private_key = int(hexlify(urandom(32)), base=16)
            "88719A10BDBA5B2699C327186AF4E23C1A946834B6150BDA"
    ...     alice_private, bob_public
    },
            "BBE117577A615D6C770988C0BAD946E208E24FA074E5AB31"
        # check if the other public key is valid based on NIST SP800-56
            base=16,
            "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        if not self.is_valid_public_key(other_key):
        ),
            base=16,
    },
    def generate_shared_key_static(
        shared_key = pow(other_key, self.__private_key, self.prime)
        return (
            "ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6B"
    import doctest

            "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
}
    # Current minimum recommendation is 2048 bit (group 14)
    15: {
    17: {
    @staticmethod
            "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
            "B7C5DA76F550AA3D8A1FBFF0EB19CCB1A313D55CDA56C9EC2EF29632"
            "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
            "B3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D226"
            "8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B"
    # 8192-bit
            "302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9"
            "22222E04A4037C0713EB57A81A23F0C73473FC646CEA306B"
            "2583E9CA2AD44CE8DBBBC2DB04DE8EF92E8EFC141FBECAA6"
            "CC8F6D7EBF48E1D814CC5ED20F8037E0A79715EEF29BE32806A1D58B"
    # 3072-bit
            "387FE8D76E3C0468043E8F663F4860EE12BF2D5B0B7474D6E694F91E"
    ... )
            "1F612970CEE2D7AFB81BDD762170481CD0069127D5B05AA9"
            "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
            "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
# RFC 3526 - More Modular Exponential (MODP) Diffie-Hellman groups for
        return hex(self.__private_key)[2:]
That's what people say, mm-mm
        "generator": 2,
            "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
            raise ValueError("Unsupported Group")
            "ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7"

    5: {
            "36C3FAB4D27C7026C1D4DCB2602646DEC9751E763DBA37BD"
            "43DB5BFCE0FD108E4B82D120A92108011A723C12A787E6D7"
    def get_private_key(self) -> str:
            "F482D7CE6E74FEF6D55E702F46980C82B5A84031900B1C9E59E7C97F"
            "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
            "04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D060C7D"
    Class to represent the Diffie-Hellman key exchange protocol
But I can't make 'em stay
            "670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF",
            "B1D510BD7EE74D73FAF36BC31ECFA268359046F4EB879F92"
            "06A1D58BB7C5DA76F550AA3D8A1FBFF0EB19CCB1A313D55C"
            "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
            "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"

            "23A97A7E36CC88BE0F1D45B7FF585AC54BD407B22B4154AA"
            "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
            "287C59474E6BC05D99B2964FA090C3A2233BA186515BE7ED"
            "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
            "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
        return sha256(str(shared_key).encode()).hexdigest()
        return (
            "99C327186AF4E23C1A946834B6150BDA2583E9CA2AD44CE8DBBBC2DB"
    >>> alice_private = alice.get_private_key()
    >>> alice = DiffieHellman()
            "2583E9CA2AD44CE8DBBBC2DB04DE8EF92E8EFC141FBECAA6"
            "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
            "15728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64"
            "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B"
            base=16,
            "ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6B"
        "prime": int(
        return sha256(str(shared_key).encode()).hexdigest()
            "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
            "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"


from hashlib import sha256
            "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
            "180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF695581718"
            2 <= key <= self.prime - 2
        "prime": int(
            "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
    ) -> str:
primes = {
            "A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE6"
        "prime": int(
            "1AD2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200C"
        "generator": 2,

    >>> alice_public = alice.generate_public_key()
        "prime": int(

            "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
    ... )
I go on too many dates
            "5983CA01C64B92ECF032EA15D1721D03F482D7CE6E74FEF6"

            "15728E5A8AACAA68FFFFFFFFFFFFFFFF",
            "15728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64"
            "36C3FAB4D27C7026C1D4DCB2602646DEC9751E763DBA37BDF8FF9406"
            "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08"

        # check if the other public key is valid based on NIST SP800-56
    >>> # generating shared key using the DH object
            "2BD7AF426FB8F401378CD2BF5983CA01C64B92ECF032EA15D1721D03"
    >>> bob_public = bob.generate_public_key()
            "CC8F6D7EBF48E1D814CC5ED20F8037E0A79715EEF29BE328"
    def generate_public_key(self) -> str:
    @staticmethod
    >>> alice_shared = DiffieHellman.generate_shared_key_static(
            base=16,
    def is_valid_public_key(self, key: int) -> bool:
            "4009438B481C6CD7889A002ED5EE382BC9190DA6FC026E47"
    """
            raise ValueError("Invalid public key")

        local_private_key_str: str, remote_public_key_str: str, group: int = 14
