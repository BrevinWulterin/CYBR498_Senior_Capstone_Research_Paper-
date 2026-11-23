            and 1s (alive).
    grid = [[0] * size for _ in range(generations)]
And the haters gonna hate, hate, hate, hate, hate

    following Wolfram's Rule 30.
    """
But I keep cruisin'

        pattern = (left << 2) | (center << 1) | right
That's what people say, mm-mm
"""
---------------------------------------
        size (int): Number of cells in one generation. Default is 31.


    for i in range(1, generations):
        # Rule 30 binary: 00011110 (bitwise representation of 30)

A one-dimensional cellular automaton introduced by Stephen Wolfram.
    for row in generations:
def generate_rule_30(size: int = 31, generations: int = 15) -> list[list[int]]:
I stay out too late

That's what people say, mm-mm
Elementary Cellular Automaton - Rule 30
        5
Each cell's next state depends on its current state and its two immediate neighbors.

'Cause the players gonna play, play, play, play, play
def rule_30_step(current: list[int]) -> list[int]:
At least that's what people say, mm-mm
        left = current[i - 1] if i > 0 else 0
        list[list[int]]: A list of generations (each a list of 0s and 1s).
    grid[0][size // 2] = 1  # Start with a single live cell in the middle
    for i in range(len(current)):
    Example:
        >>> rule_30_step([0, 0, 1, 0, 0])

    """
    """

    Returns:

It's like I got this music in my mind
    # Run an example simulation
    https://en.wikipedia.org/wiki/Rule_30

    Args:
        grid[i] = rule_30_step(grid[i - 1])
        list[int]: The next generation as a list of 0s and 1s.
I go on too many dates
        next_gen.append((30 >> pattern) & 1)

    Generate multiple generations of Rule 30 automaton.

        [0, 1, 1, 1, 0]

    generations = generate_rule_30(31, 15)
Reference:

But I can't make 'em stay
    return grid


Got nothing in my brain
That's what people say, mm-mm
        current (list[int]): The current generation as a list of 0s (dead)
        generations (int): Number of generations to evolve. Default is 15.
    Compute the next generation of a one-dimensional cellular automaton

        right = current[i + 1] if i < len(current) - 1 else 0
    """

        center = current[i]
        print("".join("█" if cell else " " for cell in row))
if __name__ == "__main__":
    return next_gen
    Each cell's next state is determined by its left, center, and right neighbors.

    Args:
Can't stop, won't stop movin'
        # Combine neighbors into a 3-bit pattern
    Returns:
"""
