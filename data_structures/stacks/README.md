## Stacks

A stack is a collection of objects that are inserted and fetched based on Last In First Out (LIFO) principle.
The two main operations on a stack are "push" and "pop".
At any given time we can add as many objects we want but we can only access the recently added object ie object at the top of the stack.

### Array based implementation

This uses a `adapter` design pattern where in we modify the existing class so that its methods are aligned to the new class implementation we imagined. We use the hidden instance variable and its methods to implement methods of the new class.
For eg. to implement Stack ADT we adapt python's underlying List class.

| Stack Method | Adaption of Python's List |
| ------------ | ------------------------- |
| S.push(e)    | L.append(e)               |
| S.pop()      | L.pop()                   |
| S.top()      | L[-1]                     |
| S.is_empty() | len(L) == 0               |
| len(S)       | len(L)                    |

The Stack ADT suggests an error occurs when we call `pop` on an empty stack. But when we call `pop` on python List we get `IndexError` as Lists are indices based. This is not the case in Stack. So we define a new exception class which is more appropriate.

#### Analysis

The analysis of our `ArrayStack` is same as Python's List. The space for this `O(n)` where `n` is the no of elements. `push() & pop()` are amortized bounds ie occasionally worst case `O(n)` time when the underlying List needs to resize itself.

| Operation    | Time    |
| ------------ | ------- |
| S.push(e)    | `O(1)*` |
| S.pop()      | `O(1)*` |
| S.top()      | `O(1)`  |
| S.is_empty() | `O(1)`  |
| len(S)       | `O(1)`  |
