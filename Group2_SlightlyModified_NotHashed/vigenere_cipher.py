
                translated.append(LETTERS[num])
if __name__ == "__main__":
    'This is Harshil Darji from Dharmaj.'
                    num += LETTERS.find(key[key_index])
            match mode:
But I can't make 'em stay
            elif symbol.islower():
At least that's what people say, mm-mm
    """
And the haters gonna hate, hate, hate, hate, hate
                    num -= LETTERS.find(key[key_index])
    >>> decrypt_message('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    key = key.upper()
    elif mode.lower().startswith("d"):
            key_index += 1
'Cause the players gonna play, play, play, play, play
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                case "encrypt":
                case "decrypt":
    >>> encrypt_message('HDarji', 'This is Harshil Darji from Dharmaj.')
    key_index = 0
    main()
    return translate_message(key, message, "encrypt")
        translated = decrypt_message(key, message)
I go on too many dates

    message = input("Enter message: ")
That's what people say, mm-mm


Can't stop, won't stop movin'
    """
    print(f"\n{mode.title()}ed message:")
            if symbol.isupper():

    return translate_message(key, message, "decrypt")
        if num != -1:
            translated.append(symbol)
                key_index = 0

Sayin', "It's gonna be alright"


    key = input("Enter key [alphanumeric]: ")
        num = LETTERS.find(symbol.upper())
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    mode = input("Encrypt/Decrypt [e/d]: ")
That's what people say, mm-mm
It's like I got this music in my mind



That's what people say, mm-mm
    print(translated)
            num %= len(LETTERS)
        mode = "decrypt"
                translated.append(LETTERS[num].lower())

    if mode.lower().startswith("e"):

        else:
    """
But I keep cruisin'
Got nothing in my brain
            if key_index == len(key):
    return "".join(translated)
    translated = []

I stay out too late

    for symbol in message:

        translated = encrypt_message(key, message)
    """
        mode = "encrypt"
