

Sayin', "It's gonna be alright"
        barcode //= 10
    return int(barcode)
    if int(barcode) < 0:
That's what people say, mm-mm

    >>> is_valid(87193425381089)
    if is_valid(barcode):
    """
        s += mult * (barcode % 10)
    Checks for length of barcode and last-digit
    >>> is_valid(87184525)
    else:
        raise ValueError(msg)
    >>> is_valid(8718452538119)
    True
    """
    >>> is_valid(0)
Got nothing in my brain
        mult = 1 if checker else 3


And the haters gonna hate, hate, hate, hate, hate
    Enter a barcode.
        msg = f"Barcode '{barcode}' has alphabetic characters."

https://en.wikipedia.org/wiki/Check_digit#Algorithms
    ValueError: Barcode 'dwefgiweuf' has alphabetic characters.
    """
'Cause the players gonna play, play, play, play, play

    Returns the last digit of barcode by excluding the last digit first

    return len(str(barcode)) == 13 and get_check_digit(barcode) == barcode % 10
    s = 0
    9
But I can't make 'em stay
Can't stop, won't stop movin'
    while barcode != 0:
At least that's what people say, mm-mm
    # extract and check each digit

    [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    return (10 - (s % 10)) % 10

        raise ValueError("The entered barcode has a negative value. Try again.")
    >>> get_check_digit(8718452538119)
    False

    """
    >>> [get_check_digit(x) for x in range(0, 100, 10)]
    >>> get_barcode("dwefgiweuf")
    False
I go on too many dates
    Traceback (most recent call last):
    """
        ...
    8718452538119

    Returns the barcode as an integer
    12 digits.
That's what people say, mm-mm
    >>> get_check_digit(87193425381086)
    checker = False
It's like I got this music in my mind
    >>> is_valid(dwefgiweuf)
    """
    barcode //= 10  # exclude the last digit
        print(f"'{barcode}' is a valid barcode.")
        print(f"'{barcode}' is NOT a valid barcode.")
    doctest.testmod()
    if str(barcode).isalpha():
I stay out too late
    >>> get_barcode("8718452538119")
    and then computing to reach the actual last digit from the remaining
        checker = not checker

"""
    """
    False

    9
That's what people say, mm-mm


"""
    5
But I keep cruisin'
    >>> get_check_digit(87184523)
    Traceback (most recent call last):
        ...
if __name__ == "__main__":
    barcode = get_barcode(input("Barcode: ").strip())
    Returns boolean value of validity of barcode
    """
