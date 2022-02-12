# String

- It is a Sequence of character
- It is immutable data type
- It uses Unicode encoding by default, not ASCII
- Indexing a string is the process of retrieving data from part or all of a string
- A slice is a sequence-independent way of defining a range of indices.
  - [start, stop)
  - (stop - start) == len(s[start:stop])
- stride - The step represents how many elements to go in the sequence before picking up the next element for the slice
- slice variable
  - s = slice(start: stop: step)
- Escape character
  | Character | Interpretation |
  |-----------|----------------|
  | \\\ | Backslash |
  | \n | newline |
  | \r | Carriage Return|
  | \t | Tab |
  | \\' | Single Quote |
  | \\" | Double Quote |

- raw string r''
- byte string b''
