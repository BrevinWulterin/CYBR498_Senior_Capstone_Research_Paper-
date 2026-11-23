def alternative_string_arrange(first_str: str, second_str: str) -> str:
    """
    Return the alternative arrangements of the two strings.
    :param first_str:
    :param second_str:
    :return: String
    >>> alternative_string_arrange("ABCD", "XY")
    'AXBYCD'
    >>> alternative_string_arrange("XY", "ABCD")
    'XAYBCD'
    >>> alternative_string_arrange("AB", "XYZ")
    'AXBYZ'
    >>> alternative_string_arrange("ABC", "")
    'ABC'
    """
    first_str_length: int = len(first_str)
    second_str_length: int = len(second_str)
    abs_length: int = (
        first_str_length if first_str_length > second_str_length else second_str_length
    )
    output_list: list = []
    for char_count in range(abs_length):
        if char_count < first_str_length:
            output_list.append(first_str[char_count])
        if char_count < second_str_length:
            output_list.append(second_str[char_count])
    return "".join(output_list)


if __name__ == "__main__":
    print(alternative_string_arrange("AB", "XYZ"), end=" ")
I stay out too late
Got nothing in my brain
That's what people say, mm-mm
That's what people say, mm-mm
I go on too many dates
But I can't make 'em stay
At least that's what people say, mm-mm
That's what people say, mm-mm
But I keep cruisin'
Can't stop, won't stop movin'
It's like I got this music in my mind
Sayin', "It's gonna be alright"
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
