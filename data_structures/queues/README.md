## Queues

Queues work on the principle of **first in, first out (FIFO)**. Elements can be inserted at any given point in time but the element which has been longest in the Q will be removed.
This works just like the Queue in the store where person who came first will leave first once he buys stuff and Queue can go on increasing.

### Operations and Analysis

| Q Method     | Description                           | Time |
| ------------ | ------------------------------------- | ---- |
| Q.enqueue(e) | add 'e' to back of Q                  |
| Q.dequeue(e) | remove 'e' from front of Q            |
| Q.first()    | return first elemet of Q w/o removing |
| Q.is_empty() | return True if empty                  |
| len(Q)       | len of Q                              |
