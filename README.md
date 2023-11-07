# triehugger
Memory efficient [trie](https://en.wikipedia.org/wiki/Trie) with incremental garbage collection.

## Example
Initialize a triehugger and add some words to it:
```python
triehugger = Triehugger()
triehugger.add("beets")
triehugger.add("beetle")
triehugger.add("beetlejuice")
```
Your triehugger looks like:
```bash
-
 - b
  - be
   - bee
    - beet
     - beets
     - beetl
      - beetle
       - beetlej
        - beetleju
         - beetlejui
          - beetlejuic
           - beetlejuice
```
Now let's delete `beetlejuice`:
```python
triehugger.delete("beetlejuice")
```
It now looks like:
```bash
-
 - b
  - be
   - bee
    - beet
     - beets
     - beetl
      - beetle
```
Note that when you deleted the word `beetlejuice`, the nodes `beetlej`, `beetleju`, `beetlejui`, `beetlejuic` were also removed, since they only existed to direct you to `beetlejuice`.
Once `beetlejuice` is gone, they have no reason to remain!
However, `beetle` remains because it was a word we explicitly added and one we want to store.
