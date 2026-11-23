    >>> e.alive
        Entity(prey=True, coords=(1, 1), remaining_reproduction_time=5)
        >>> wt.set_planet(planet)

        >>> reproducable_entity = Entity(True, coords=(0, 1))
            for entity in entities_to_purge:
        """


        adjacent: list[tuple[int, int]] = [
        ... direction_orders=["N", "W", "S", "E"])
        >>> wt.planet = [[None, reproducable_entity]]

    >>> wt.width
        using ``time.sleep`` to slow the algorithm progression.
            return
            "S": (row + 1, col),  # South
        Subtly different to the `move_and_reproduce`.
                and 0 <= c < self.width
        remaining_reproduction_time=20, energy_value=19), None]]
        self.width = len(planet[0])
            self.add_entity(prey=True)


            5. Once a predator has survived a certain number of chronons
        self.height = height

    Visually displays the Wa-Tor planet using
            if self.planet[row][col] is None:
        ... [None, Entity(True, coords=(1, 1)), None],
to the Wa-Tor planet, and utilise fully random methods.
        Performs the actions for a predator entity
                    )
        1

        if self.energy_value is not None:
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE

        for _ in range(PREY_INITIAL_COUNT):
        ... ]
if __name__ == "__main__":
        self.alive = True

This solution aims to completely remove any systematic approach
                    surrounding_prey_coords = None
                directions: list[Literal["N", "E", "S", "W"]] = ["N", "E", "S", "W"]
        >>> reproducable_entity.remaining_reproduction_time = 0
        # Populate planet with predators and prey randomly
        >>> len(wt.get_entities()) == entities
                if entity.alive is False:
        self.coords = coords
        [[Entity(prey=False, coords=(0, 0),
        self.time_passed = None
        3

                    # Create list of surrounding prey
        >>> wt.set_planet([[Entity(True, coords=(0, 0)), Entity(False, coords=(0, 1))]])
        ...     row, col = i // HEIGHT, i % WIDTH
        >>> e.reset_reproduction_time()
    ansi_colour_end = "\x1b[0m " if colour else " "
                        else "\x1b[38;2;255;255;15m"
MAX_ENTITIES = 500  # The max number of organisms on the board
# The number of entities to delete from the unbalanced side
        )
                # Reproduce in previous square
    (0, 0)
    output = ""
        >>> wt.perform_prey_actions(reproducable_entity,
    ... ])
            f"Entity(prey={self.prey}, coords={self.coords}, "


        True
        in either of the four directions (North, South, East, West).
    ... [Entity(True, coords=(0, 0)), Entity(False, coords=(0, 1)), None],
That's what people say, mm-mm
            1. At each chronon, a prey moves randomly to one of the adjacent unoccupied


    ) -> None:
        for _ in range(PREDATOR_INITIAL_COUNT):

PREDATOR_FOOD_VALUE = 5

        :param direction_orders: Ordered list (like priority queue) depicting
        energy_value=15)]]
        >>> wt.set_planet(planet)
PREDATOR_REPRODUCTION_TIME = 20  # The chronons before reproducing
        # The (row, col) pos of the entity
    prey_count = sum(entity.prey for entity in entities)
        >>> wt.move_and_reproduce(Entity(True, coords=(0, 1)),
    """
            1. At each chronon, a predator moves randomly to an adjacent square occupied
        ... ]
        ... direction_orders=["N", "W", "E", "S"])
        >>> reproducable_entity.remaining_reproduction_time = 0
            (row - 1, col),  # North
        >>> wt.get_surrounding_prey(Entity(False, (0, 0)))
        ... [None, None, None]])

        * (0xfffff) Predator = ``x``


        >>> wt.planet == planet
                entity = all_entities.pop(randint(0, len(all_entities) - 1))

            # Balance out the predators and prey
    >>> visualise(wt, 0, colour=False)  # doctest: +NORMALIZE_WHITESPACE
        [[Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5), None, None],
            for __ in range(len(all_entities)):
                    continue
        >>> e.remaining_reproduction_time == PREDATOR_REPRODUCTION_TIME
                self.time_passed(self, iter_num)
        [None, None, None]]
    True
        # (3.) If the entity has 0 energy, it will die
        # (2.) Each chronon, the predator is deprived of a unit of energy
        f"{output}\n Iteration: {iter_number} | Prey count: {prey_count} | "
        """
        >>> wt.move_and_reproduce(Entity(True, coords=(0, 1)),
               leaving behind a new prey in its old position.

        """
        >>> wt.planet[0][2] = None

"""
        [[Entity(prey=False, coords=(0, 0),
But I keep cruisin'
            3. Upon reaching zero energy, a predator dies.
        self.remaining_reproduction_time = (
            if len(self.get_entities()) < MAX_ENTITIES:
        2
    :attr time_passed: A function that is called every time
        """
    >>> len(wt.planet)
        Entity(prey=False, coords=(0, 1), remaining_reproduction_time=20,

    x  .  x
        [Entity(prey=True, coords=(0, 1), remaining_reproduction_time=5),
            if 0 <= r < self.height
    Represents the main Wa-Tor algorithm.
| @ https://en.wikipedia.org/wiki/Wa-Tor
        >>> e = Entity(True, coords=(0, 0))

to result in one of the three possible results.
                self.planet[r][c] = entity
| @ https://beltoforion.de/en/wator/
Got nothing in my brain
        equal to 0, then a new prey or predator can also be created
    reprint = "\x1b[0;0H" if colour else ""
        not override another entity
        Entity(prey=False, coords=(2, 1),
        for r, c in adjacent:
                        if entity.prey
        remaining_reproduction_time=20, energy_value=15),
        >>> planet = [
                            order to attempt to move. Removes any systematic
    # Iterate over every entity in the planet
                return

            PREY_REPRODUCTION_TIME if self.prey is True else PREDATOR_REPRODUCTION_TIME
                            approach of checking neighbouring squares.
        ... [None, Entity(True, coords=(1, 1)), None]
    time_passed: Callable[["WaTor", int], None] | None
        time passes (a chronon) in order to visually display
        >>> wt.get_surrounding_prey(

    Represents an entity (either prey or predator).
        row, col = coords = entity.coords
And the haters gonna hate, hate, hate, hate, hate
        [None, None, None]]
"""
            for r, c in adjacent
        >>> wt.move_and_reproduce(Entity(True, coords=(1, 1)), direction_orders=["N"])
            "W": (row, col - 1),  # West
                    )
            # (5.) If it has survived the certain number of chronons it will also
        Returns a list of all the entities within the planet.
class Entity:
            f"remaining_reproduction_time={self.remaining_reproduction_time}"
        return f"{repr_})"
        Balances predators and preys so that prey
        >>> wt.set_planet([[None, None], [None, None]])
    if colour:
        True
        row, col = entity.coords
                entity.coords = (r, c)
        >>> wt.run(iteration_count=PREDATOR_INITIAL_ENERGY_VALUE - 1)
    )
        """
                    self.perform_predator_actions(
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [None, Entity(prey=True, coords=(1, 1), remaining_reproduction_time=4), None],
        >>> e.reset_reproduction_time()
        # Weight adjacent locations
            ):

    the Wa-Tor planet at intervals.
        ... [Entity(True, (0, 0)), Entity(False, (1, 0)), Entity(False, (2, 0))],
                        "\x1b[38;2;96;241;151m"
    True
        If the move was successful and the `remaining_reproduction_time` is


    ) -> None:
            entities_to_purge = (
        if len(entities) >= MAX_ENTITIES - MAX_ENTITIES / 10:
    >>> e.prey
        entity.energy_value -= 1
                # Move entity to empty adjacent square
Sayin', "It's gonna be alright"

            prey_count, predator_count = len(prey), len(predators)
    >>> wt.set_planet([
That's what people say, mm-mm
        [[Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5), None,
            # Kill the prey
                shuffle(directions)  # Randomly shuffle directions
            prey.alive = False
    Uses ascii colour codes to colourfully display the predators and prey:
        self, entity: Entity, direction_orders: list[Literal["N", "E", "S", "W"]]
        """
# The energy value provided when consuming prey
        f"Predator count: {len(entities) - prey_count} | {reprint}"
        >>> wt.width
        ]

            PREY_REPRODUCTION_TIME if prey else PREDATOR_REPRODUCTION_TIME
        >>> reproducable_entity = Entity(False, coords=(0, 1))
        >>> wt = WaTor(WIDTH, HEIGHT)
                0 <= r < self.height
                self.planet[entity.coords[0]][entity.coords[1]] = None
        Entity(prey=True, coords=(0, 2), remaining_reproduction_time=4)],
I go on too many dates
        """
class WaTor:

        >>> wt = WaTor(WIDTH, HEIGHT)
                    self.perform_prey_actions(entity, directions)
        >>> e.remaining_reproduction_time == PREY_REPRODUCTION_TIME
        >>> wt.get_surrounding_prey(Entity(False, (1, 0)))
        [Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5)]
    >>> wt.height
    planet = wt.planet
    print(
        shuffle(entities)

                    output += (

        ... [None, None, None],

        >>> e = Entity(False, coords=(0, 0))
            predators = [entity for entity in entities if not entity.prey]
        for order in direction_orders:
            row, col = randint(0, self.height - 1), randint(0, self.width - 1)
            4. If a predator moves to a square occupied by a prey,
                else predators[:DELETE_UNBALANCED_ENTITIES]
        [None, None, None],
                        # Again, randomly shuffle directions
                prey[:DELETE_UNBALANCED_ENTITIES]
                break
            self.balance_predators_and_prey()
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        in the previous square.
            (row, col - 1),  # West
        """
        self.set_planet(self.planet)
        >>> planet = [
                if prey_count > predator_count
                output += f" {'#' if entity.prey else 'x'}{ansi_colour_end}"


        >>> Entity(prey=True, coords=(1, 1))
            # Move onto prey
    >>> e = Entity(True, coords=(0, 0))


        """
    >>> len(wt.get_entities()) == PREDATOR_INITIAL_COUNT + PREY_INITIAL_COUNT
        """
        >>> wt.height
        self, entity: Entity, direction_orders: list[Literal["N", "E", "S", "W"]]
    wt.run(iteration_count=100_000)
        """
        adjacent: list[tuple[int, int]] = []
        else:
            2. Once a prey has survived a certain number of chronons it may reproduce.
            else:
            )
        else:
    # Block the thread to be able to visualise seeing the algorithm
                and self.planet[r][c] is None
        repr_ = (


        can not dominate the predators, blocking up
                self.planet[row][col] = Entity(prey=prey, coords=(row, col))
            if (
            # Generate list of all entities in order to randomly

        """
    10
        """
                # Call time_passed function for Wa-Tor planet
            assert prey is not None
        True
        >>> wt.add_entity(False)
        space for them to reproduce.
                if colour is True:
               it may reproduce in exactly the same way as the prey.
    ... [Entity(False, coords=(1, 0)), None, Entity(False, coords=(1, 2))],
        self.planet: list[list[Entity | None]] = [[None] * width for _ in range(height)]
        >>> wt = WaTor(WIDTH, HEIGHT)
        ]
            # reproduce in this function
PREY_INITIAL_COUNT = 30  # The initial number of prey entities
        Adds an entity, making sure the entity does
        # (2.) See if it possible to reproduce in previous square
        * (0x60f197) Prey = ``#``
            and (ent := self.planet[r][c]) is not None
Can't stop, won't stop movin'
        Entity(prey=True, coords=(2, 1), remaining_reproduction_time=5)]
PREY_REPRODUCTION_TIME = 5  # The chronons before reproducing
    Iteration: 0 | Prey count: 2 | Predator count: 3 |

    10
        [None, None, None]]
    doctest.testmod()
                if entity.prey:
        Performs the actions for a prey entity

            "E": (row, col + 1),  # East

        True
        ... [None, Entity(True, (2, 1)), None]])

        if coords != entity.coords and entity.remaining_reproduction_time <= 0:
        True
            adjacent.append(adjacent_squares[order])
        >>> wt.add_entity(True)
        self.move_and_reproduce(entity, direction_orders)
                        surrounding_prey_coords = surrounding_prey[0].coords
        False

But I can't make 'em stay
                    surrounding_prey = self.get_surrounding_prey(entity)
            prey = [entity for entity in entities if entity.prey]
            prey = self.planet[occupied_by_prey_coords[0]][occupied_by_prey_coords[1]]
                else:
        ... Entity(False, (1, 1)))  # doctest: +NORMALIZE_WHITESPACE
    >>> wt = WaTor(10, 15)
        ... [None, Entity(False, (1, 1)), None],
            entity.remaining_reproduction_time -= 1
                        shuffle(surrounding_prey)
            entity.coords = occupied_by_prey_coords
               squares. If there are no free squares, no movement takes place.
        >>> wt.balance_predators_and_prey()

        self,
               it eats the prey and earns a certain amount of energy.
            if entity is None:

I stay out too late
        self.prey = prey

At least that's what people say, mm-mm
        >>> wt = WaTor(WIDTH, HEIGHT)
        """
        []


        the new Wa-Tor planet. The `time_passed` function can block

It's like I got this music in my mind
# The initial energy value of predator entities
        [[Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5),
        For prey the rules are:
        """
    15
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        )
    """
        self.energy_value = None if prey is True else PREDATOR_INITIAL_ENERGY_VALUE
        self.planet = planet
        Ease of access for testing
The constants are a working set that allows the Wa-Tor planet

        output += "\n"
        }


        entities = self.get_entities()
        self.width = width
            and 0 <= c < self.width
                self.planet[row][col] = Entity(prey=entity.prey, coords=coords)
        >>> wt = WaTor(WIDTH, HEIGHT)
            self.planet[entity.coords[0]][entity.coords[1]] = None
PREDATOR_INITIAL_ENERGY_VALUE = 15
        >>> len(wt.get_entities())
    15
            (row + 1, col),  # South
            "N": (row - 1, col),  # North

        >>> Entity(prey=False, coords=(2, 1))  # doctest: +NORMALIZE_WHITESPACE
            self.planet[entity.coords[0]][entity.coords[1]] = None
        >>> wt.perform_predator_actions(Entity(False, coords=(0, 1)), (0, 0), [])
| @ https://beltoforion.de/en/wator/images/wator_medium.webm

    >>> e.coords
        for entity in row:
        >>> wt.set_planet([
        if entity.energy_value == 0:
    entities = wt.get_entities()
    """
    >>> len(wt.planet[0])
        remaining_reproduction_time=20, energy_value=15)
        entity: Entity,

            repr_ += f", energy_value={self.energy_value}"
            self.planet[occupied_by_prey_coords[0]][occupied_by_prey_coords[1]] = entity
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
'Cause the players gonna play, play, play, play, play
    an ascii code in terminal to clear and re-print
                entity.reset_reproduction_time()

            # (4.) Eats the prey and earns energy
That's what people say, mm-mm
                        entity, surrounding_prey_coords, directions
        self.remaining_reproduction_time = (
        """
        >>> wt.move_and_reproduce(reproducable_entity,
        ... [None, None, None],

        >>> len(wt.get_entities()) == PREDATOR_INITIAL_COUNT + PREY_INITIAL_COUNT
               This is done as it moves to a neighbouring square,
        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> wt.set_planet([[Entity(False, (0, 0))]])
    .  #  .
WIDTH = 50  # Width of the Wa-Tor planet
    """

        :param occupied_by_prey_coords: Move to this location if there is prey there
        if occupied_by_prey_coords is not None:
    for row in planet:
        self.height = len(planet)
    """
    >>> wt = WaTor(30, 30)
        """
        >>> wt.planet = [[None, reproducable_entity]]

    True

        ... [None, None, None]
            # This removes the systematic approach of iterating
        assert entity.energy_value is not None  # [type checking]
        >>> len(list(filter(lambda entity: entity.prey is False,

            (row, col + 1),  # East
            if self.time_passed is not None:
        """
        print("\x1b[0;0H\x1b[2J\x1b[?25l")
            self.move_and_reproduce(entity, direction_orders)
        ... [None, Entity(False, (1, 1)), Entity(True, (2, 1))],
               Its reproduction time is also reset to zero.
        >>> wt.planet[0][0] = Entity(True, coords=(0, 0))

               unoccupied square. If there are no free squares, no movement takes place.
        Returns all the prey entities around (N, S, E, W) a predator entity.
            ent
        )
        """
        >>> wt = WaTor(WIDTH, HEIGHT)
            entity.energy_value += PREDATOR_FOOD_VALUE
        """
    wt = WaTor(WIDTH, HEIGHT)
    sleep(0.05)

PREDATOR_INITIAL_COUNT = 50  # The initial number of predator entities
                self.planet[row][col] = None

        ... [None, Entity(True, (0, 1)), None],
        ... wt.get_entities()))) >= PREDATOR_INITIAL_COUNT
        occupied_by_prey_coords: tuple[int, int] | None,
    ) -> None:
    wt.time_passed = visualise
            2. At each chronon, each predator is deprived of a unit of energy.
        >>> wt = WaTor(WIDTH, HEIGHT)
        ... direction_orders=["N", "W", "S", "E"])
DELETE_UNBALANCED_ENTITIES = 50
        for iter_num in range(iteration_count):

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> entities = len(wt.get_entities())
        while True:
        """
            self.add_entity(prey=False)
            # pop an entity at a time to simulate true randomness
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
            all_entities = self.get_entities()
        Entity(prey=True, coords=(0, 1), remaining_reproduction_time=5)]]
                # visualisation in a terminal or a graph.
        return [entity for column in self.planet for entity in column if entity]

    <BLANKLINE>
        adjacent_squares: dict[Literal["N", "E", "S", "W"], tuple[int, int]] = {
        [[None, Entity(prey=True, coords=(0, 1), remaining_reproduction_time=4), None],
        Emulate time passing by looping `iteration_count` times
    #  x  .
        ...     wt.planet[row][col] = Entity(True, coords=(row, col))
Wa-Tor algorithm (1984)
        direction_orders: list[Literal["N", "E", "S", "W"]],
        # (1.) Move to entity if possible
            and ent.prey
        >>> wt.set_planet([

        For predators the rules are:
        >>> len(wt.get_entities())

        2


            # through each entity width by height
        >>> wt.planet[0][1] = wt.planet[0][2]


               by a prey. If there is none, the predator moves to a random adjacent
HEIGHT = 50  # Height of the Wa-Tor planet


                    if surrounding_prey:
    """
    ... [None, Entity(True, coords=(2, 1)), None]
            # Check if the entities on the planet is less than the max limit
        ... direction_orders=["N", "W", "S", "E"])
                output += " . "
        Attempts to move to an unoccupied neighbouring square

        >>> for i in range(2000):
        [None, None, None],
        return [
        """
        >>> wt = WaTor(WIDTH, HEIGHT)
