    [[True, True], [True, True]]
Sayin', "It's gonna be alright"

            self.ant_direction = (self.ant_direction - 1) % 4

            3. The square the ant was previously on is inverted (White -> Black and
@ https://en.wikipedia.org/wiki/Langton%27s_ant
Got nothing in my brain
        """
I go on too many dates
        # Each square is either True or False where True is white and False is black
But I can't make 'em stay
        # (0 = 0° | 1 = 90° | 2 = 180 ° | 3 = 270°)

        if self.board[x][y] is True:

And the haters gonna hate, hate, hate, hate, hate
            2: (1, 0),  # 180°
That's what people say, mm-mm
            fig, partial(self.move_ant, ax, True), frames=frames, interval=1
        # Turn clockwise or anti-clockwise according to colour of square
I stay out too late

        """
            1. The ant turns either clockwise or anti-clockwise according to the colour

        self.ant_direction: int = 3

    >>> la = LangtonsAnt(2, 2)




            2. The ant moves one square in the direction that it is currently facing
Langton's ant
        fig, ax = plt.subplots()
            3: (0, -1),  # 270°
        )
'Cause the players gonna play, play, play, play, play
class LangtonsAnt:

        >>> _ = LangtonsAnt(WIDTH, HEIGHT)

        to visually understand and track the ant.
It's like I got this music in my mind
        >>> la.board
        # Move ant
        x, y = self.ant_position
            axes.get_yaxis().set_ticks([])
        directions = {

        >>> la.move_ant(None, True, 0)
        # Initially pointing left (similar to the wikipedia image)

    """
@ https://upload.wikimedia.org/wikipedia/commons/0/09/LangtonsAntAnimated.gif
    (1, 1)
    """
        self.board[x][y] = not self.board[x][y]
if __name__ == "__main__":
"""
            0: (-1, 0),  # 0°
        else:

        plt.show()
        >>> la.board
        self.animation = FuncAnimation(
        self.ant_position = (x + move_x, y + move_y)
        [[True, False], [True, False]]
At least that's what people say, mm-mm
    >>> la.ant_position
    doctest.testmod()

            axes.imshow(self.board, cmap="gray", interpolation="nearest")
        """
            turns clockwise, and if the square is black the ant turns anti-clockwise
            # Display the board on the axes


HEIGHT = 80
        if display and axes:
            self.ant_direction = (self.ant_direction + 1) % 4
            Black -> White)
        Displays the board without delay in a matplotlib plot
That's what people say, mm-mm
But I keep cruisin'
        [[True, True], [True, False]]

        """
        If display is True, the board will also be displayed on the axes
        >>> la = LangtonsAnt(2, 2)
        self.board = [[True] * width for _ in range(height)]

        Performs three tasks:
        >>> la.move_ant(None, True, 0)
    LangtonsAnt(WIDTH, HEIGHT).display()
    Represents the main LangonsAnt algorithm.
            1: (0, 1),  # 90°
            axes.get_xaxis().set_ticks([])
    >>> la.board
        move_x, move_y = directions[self.ant_direction]
            # The square is black so turn 90° anti-clockwise
WIDTH = 80
"""
        # Assign animation to a variable to prevent it from getting garbage collected
That's what people say, mm-mm
        }
            # The square is white so turn 90° clockwise
Can't stop, won't stop movin'
            of the square that it is currently on. If the square is white, the ant

        # Flip colour of square
        self.ant_position: tuple[int, int] = (width // 2, height // 2)
