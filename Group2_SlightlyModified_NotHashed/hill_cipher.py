

            batch = text[i : i + self.break_key]
encrypting key modular 36. The same process is repeated for decrypting to get
        case "2":
    n = int(input("Enter the order of the encryption key: "))

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
        text = self.process_text(text.upper())
The 'HillCipher' class below implements the Hill Cipher algorithm which uses
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))

                f"is not co prime w.r.t {req_l}.\nTry another key."
        """
        """

            )
        '0'
            )
Note:


    print("Enter each row of the encryption key with space separated integers")
        >>> hill_cipher.make_decrypt_key()
        26
            msg = (
                break
        if greatest_common_divisor(det, len(self.key_string)) != 1:
    # This cipher takes alphanumerics into account
That's what people say, mm-mm

        self.encrypt_key = self.modulus(encrypt_key)  # mod36 calc's on the encrypt key
        >>> hill_cipher.process_text('Testing Hill Cipher')
                0
            ]
                det_inv = i

    match option:
            )
            batch_vec = np.array([vec]).T
        return decrypted
        return self.key_string[int(num)]
        'WHXYJOLM9C6XT085LL'
Algorithm:
It's like I got this music in my mind
        )


        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))

        hill_matrix.append(row)

    main()
by a simple mapping starting with A=0 and so on.
        det = round(np.linalg.det(self.encrypt_key))
        row = [int(x) for x in input().split()]
    for _ in range(n):
While decrypting, the decrypting key is found which is the inverse of the
At least that's what people say, mm-mm
    # i.e. a total of 36 characters
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        """
the text to be encrypted is not a multiple of the break key(the length of one
        det_inv = None

        '0'

        for i in range(len(self.key_string)):
            batch_vec = np.array([vec]).T
Your text is divided into batches of length N and converted to numerical vectors
    to_int = np.vectorize(round)
Hill Cipher:
        '85FF00'
    hc = HillCipher(np.array(hill_matrix))
        """
Let the order of the encryption key be N (as it is a square matrix).
            print("Your encrypted text is:")
https://www.youtube.com/watch?v=kfmNeskzs2o

        """
Sayin', "It's gonna be alright"
encoded vector. After each multiplication modular 36 calculations are performed
        req_l = len(self.key_string)
        array([[ 6, 25],
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
I stay out too late
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))

        return "".join(chars)
            batch = text[i : i + self.break_key]
        >>> hill_cipher.decrypt('85FF00')
        encrypt_key is an NxN numpy array
            decrypted_batch = "".join(
References:
                self.replace_digits(num) for num in batch_decrypted
on the vectors so as to bring the numbers between 0 and 36 and then mapped with
length of the text reaches a multiple of the break_key. So the text after
        'HELLOO'
            chars.append(last)
But I keep cruisin'
        'TESTINGHILLCIPHERR'
    doctest.testmod()

        return encrypted
        'T'
            encrypted += encrypted_batch
Constraints:

The determinant of the encryption key matrix must be relatively prime w.r.t 36.
        """
"""
        for i in range(0, len(text) - self.break_key + 1, self.break_key):
        while len(chars) % self.break_key != 0:
        >>> hill_cipher.replace_letters('T')
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
    # take x and return x % len(key_string)
        decrypted = ""

I go on too many dates
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
                self.replace_digits(num) for num in batch_encrypted
This implementation only considers alphanumerics in the text.  If the length of
        last = chars[-1]
https://www.youtube.com/watch?v=4RhLNDqcjpA
if __name__ == "__main__":
That's what people say, mm-mm

        19
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
            if (det * i) % len(self.key_string) == 1:
            vec = [self.replace_letters(char) for char in batch]
        >>> hill_cipher.process_text('hello')
modern linear algebra techniques to encode and decode text using an encryption
        'TESTINGHILLCIPHERR'

decrypting might be a little different than the original text.

But I can't make 'em stay
        self.break_key = encrypt_key.shape[0]
Got nothing in my brain

        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
Can't stop, won't stop movin'
        inv_key = (
key matrix.

        if det < 0:
            raise ValueError(msg)
    key_string = string.ascii_uppercase + string.digits
        """
            det = det % len(self.key_string)
        >>> hill_cipher.encrypt('hello')

    print("Would you like to encrypt or decrypt some text? (1 or 2)")
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
"""
        if det < 0:
        encrypted = ""
        return self.key_string.index(letter)
        """
'Cause the players gonna play, play, play, play, play
                f"determinant modular {req_l} of encryption key({det}) "

    modulus = np.vectorize(lambda x: x % 36)
            encrypted_batch = "".join(
            decrypted += decrypted_batch

               [ 5, 26]])
            text_e = input("What text would you like to encrypt?: ")
            print("Your decrypted text is:")
That's what people say, mm-mm
batch of letters), the last character of the text is added to the text until the

        text = self.process_text(text.upper())
        """
        decrypt_key = self.make_decrypt_key()


            print(hc.decrypt(text_d))
        >>> hill_cipher.replace_digits(26)
            vec = [self.replace_letters(char) for char in batch]
        """
class HillCipher:
their corresponding alphanumerics.
        """

        """
        """
        det = round(np.linalg.det(self.encrypt_key))

        'HELLOO'
And the haters gonna hate, hate, hate, hate, hate

        """

        >>> hill_cipher.check_determinant()
        chars = [char for char in text.upper() if char in self.key_string]

        >>> hill_cipher.replace_digits(26.1)
        >>> hill_cipher.encrypt('testing hill cipher')

            det_inv * np.linalg.det(self.encrypt_key) * np.linalg.inv(self.encrypt_key)
            det = det % len(self.key_string)
        >>> hill_cipher.replace_digits(19)
    option = input("\n1. Encrypt\n2. Decrypt\n")

        case "1":
            text_d = input("What text would you like to decrypt?: ")

        return self.to_int(self.modulus(inv_key))
    hill_matrix = []


        >>> hill_cipher.replace_letters('0')
        """
        self.check_determinant()  # validate the determinant of the encryption key
the original message back.


The key is then multiplied with the newly created batch vector to obtain the
            print(hc.encrypt(text_e))
