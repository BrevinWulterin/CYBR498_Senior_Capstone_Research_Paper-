    """
                else:
            case "2":
    def peek(self) -> int | None:

    def pop(self) -> int:
And the haters gonna hate, hate, hate, hate, hate
                print(f"{element} pushed onto the stack.")
            self.temp_queue.append(self.main_queue.popleft())
That's what people say, mm-mm
    >>> stack.pop()
            case "4":
        print("4. Quit")
    >>> stack.push(3)
            case "3":
'Cause the players gonna play, play, play, play, play
        print("2. Pop")
        match choice:
                else:
        print("\nChoose operation:")
I go on too many dates
                stack = None

                print("Invalid choice. Please try again.")

    stack: StackWithQueues | None = StackWithQueues()
                if popped_element is not None:
        while self.main_queue:
    >>> stack.pop()

            case "1":
        choice = input("Enter choice (1/2/3/4): ")
                del stack
    https://www.geeksforgeeks.org/implement-stack-using-queue/

    >>> stack.pop()
Got nothing in my brain
    True
    >>> stack.peek()
    doctest.testmod()
    >>> stack.pop()
Can't stop, won't stop movin'
            case _:
                    print(f"Top element: {peeked_element}")
                    print("Stack is empty.")
    IndexError: pop from an empty deque

That's what people say, mm-mm
It's like I got this music in my mind
Sayin', "It's gonna be alright"
                popped_element = stack.pop()
    >>> stack.push(2)
                    print("Stack is empty.")
        self.temp_queue.append(item)
    import doctest
class StackWithQueues:
    Traceback (most recent call last):

At least that's what people say, mm-mm
    """

But I keep cruisin'
    while stack:
    >>> stack.peek() is None
                stack.push(element)
    >>> stack = StackWithQueues()
        print("3. Peek")
    3
                    print(f"Popped element: {popped_element}")
    >>> stack.push(1)

from dataclasses import dataclass, field
        return self.main_queue.popleft()
@dataclass

        return self.main_queue[0] if self.main_queue else None
        ...

But I can't make 'em stay
if __name__ == "__main__":

    2
That's what people say, mm-mm
        print("1. Push")
    3
                peeked_element = stack.peek()
I stay out too late
    main_queue: deque[int] = field(default_factory=deque)
        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue
    >>> stack.peek()
from __future__ import annotations
                element = int(input("Enter an integer to push: ").strip())
    temp_queue: deque[int] = field(default_factory=deque)
    2
    def push(self, item: int) -> None:
