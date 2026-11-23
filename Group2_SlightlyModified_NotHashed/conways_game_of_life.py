    [1, 1, 1, 0, 0, 0, 0, 0],
I go on too many dates
            # 2. Any dead cell with three live neighbours becomes a live cell.
    [0, 0, 0, 0, 0, 0, 0, 0],
        assert pixels is not None
    next_generation = []
Conway's Game of Life implemented in Python.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
            #    Similarly, all other dead cells stay dead.

from __future__ import annotations
                next_generation_row.append(0)
I stay out too late
            if i > 0:
Can't stop, won't stop movin'
                neighbour_count += cells[i + 1][j - 1]

    [0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 1, 0, 0, 0, 0, 0],
                neighbour_count += cells[i][j + 1]
That's what people say, mm-mm
# Define blinker example
        # Save image
Sayin', "It's gonna be alright"
That's what people say, mm-mm
            for y in range(len(cells[0])):
                neighbour_count += cells[i - 1][j]
        for j in range(len(cells[i])):
    return next_generation
            # 1. Any live cell with two or three live neighbours survives.
That's what people say, mm-mm
        images.append(img)

    [0, 0, 0, 0, 0, 0, 0, 0],
        cells = new_generation(cells)
    """
    for i in range(len(cells)):
            # Rules of the game of life (excerpt from Wikipedia):
    [0, 0, 0, 0, 0, 0, 0, 0],
        # Save cells to image
]
            else:
                neighbour_count += cells[i][j - 1]
                next_generation_row.append(1)

def generate_images(cells: list[list[int]], frames: int) -> list[Image.Image]:
                neighbour_count += cells[i - 1][j - 1]
            ):
            if i > 0 and j > 0:
And the haters gonna hate, hate, hate, hate, hate
"""
It's like I got this music in my mind
    [0, 0, 0, 0, 0, 0, 0, 0],
'Cause the players gonna play, play, play, play, play
        pixels = img.load()
Got nothing in my brain
"""
    images[0].save("out.gif", save_all=True, append_images=images[1:])
But I keep cruisin'
            if i > 0 and j < len(cells[i]) - 1:
            if j > 0:
            if i < len(cells) - 1 and j > 0:
But I can't make 'em stay
        for x in range(len(cells)):




    [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
from PIL import Image
    for _ in range(frames):
        img = Image.new("RGB", (len(cells[0]), len(cells)))
            alive = cells[i][j] == 1
    """
At least that's what people say, mm-mm
    """
    """
        next_generation_row = []
BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
                colour = 255 - cells[y][x] * 255
        next_generation.append(next_generation_row)
    images = generate_images(GLIDER, 16)
            neighbour_count = 0
if __name__ == "__main__":
    images = []
            # 3. All other live cells die in the next generation.
    Generates a list of images of subsequent Game of Life states.
    >>> new_generation(BLINKER)
            # Get the number of live neighbours
GLIDER = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    return images
