# npuzzle

A solver for the [8-puzzle game](http://en.wikipedia.org/wiki/15_puzzle), using
state-space search with A* and different heuristics (Manhattan distance or
number of misplaced tiles), with no external dependencies.


## Usage

```bash
python npuzzle.py
```

You can change the initial state and the desired goal state in npuzzle.py.


## Testing

```bash
python -m unittest discover
```
