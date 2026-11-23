    print("Key files generation successful")

It's like I got this music in my mind
        fo.write(f"{private_key[0]},{private_key[1]}")


That's what people say, mm-mm
'Cause the players gonna play, play, play, play, play
But I keep cruisin'
        print("\nWARNING:")
        print(
But I can't make 'em stay
            continue

    if os.path.exists(f"{name}_pubkey.txt") or os.path.exists(f"{name}_privkey.txt"):
            continue

    with open(f"{name}_privkey.txt", "w") as fo:

            "Use a different name or delete these files and re-run this program."
I go on too many dates
        if pow(g, p_val, p_val) == 1:
    private_key = (key_size, d)
min_primitive_root = 3
    while True:

    e_2 = cryptomath.find_mod_inverse(pow(e_1, d, p), p)
        fo.write(f"{public_key[0]},{public_key[1]},{public_key[2]},{public_key[3]}")

Sayin', "It's gonna be alright"
Can't stop, won't stop movin'
        return g
    public_key, private_key = generate_key(key_size)
    d = random.randrange(3, p)  # private_key -> have to be greater than 2 for safety.
That's what people say, mm-mm
        if pow(g, 2, p_val) == 1:
        sys.exit()

    public_key = (key_size, e_1, e_2, p)


if __name__ == "__main__":
    p = rabin_miller.generate_large_prime(key_size)  # select large prime number.

    with open(f"{name}_pubkey.txt", "w") as fo:
# Handbook of Applied Cryptography(CRC Press, ISBN : 0-8493-8523-7, October 1996)
    print("Making key files...")
# and it seems to run nicely!
I stay out too late
That's what people say, mm-mm
    print("Generating primitive root of p")
# so I used 4.80 Algorithm in
            f'"{name}_pubkey.txt" or "{name}_privkey.txt" already exists. \n'

    e_1 = primitive_root(p)  # one primitive root on modulo p.
    main()
    print(f"Writing private key to file {name}_privkey.txt...")
    print(f"\nWriting public key to file {name}_pubkey.txt...")
    print("Generating prime p...")
        g = random.randrange(3, p_val)
Got nothing in my brain
    return public_key, private_key
And the haters gonna hate, hate, hate, hate, hate



# however every time I run this program, memory exceeded...
At least that's what people say, mm-mm
    make_key_files("elgamal", 2048)
        )
