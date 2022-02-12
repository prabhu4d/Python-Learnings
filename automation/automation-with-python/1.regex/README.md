# Regular Expressions

- `()` - grouping the patterns
- `?` - optional match
  - zero instance or 1 instance
- `*` - match zero or more
  - zero or more instance
- `+` - match one or more
- `{n}` - match specific repetitions
  - `{min, max}` - greedy, means it matches the longest string
  - `{min, max}?` - non greedy, means it matches the shortest string
  - `{, max}`
  - `{min, }`
- `^` - match at start of the string
- `$` - match t end of the string
- `.` - wildcard operator
  - match any character except for a newline

## Character Class

- `\d` - Any numeric digit from 0 to 9.
- `\D` - Any character that is not a numeric digit from 0 to 9
- `\w` - Any letter, numeric digit, or the underscore character.
- `\W` - Any character that is not a letter, numeric digit, or the underscore character.
- `\s` - Any space, tab, or newline character.
- `\S` - Any character that is not a space, tab, or newline
- `[anything]` - to create a own character class
  - inside the square brackets, the normal regular expression
    symbols are not interpreted
  - no need to write escape character \?, just write ?
  - `[^anything]` - negative character class

## Python re methods

- `r''` - raw string python, that do not escape characters
- search() will return a Match object of the first matched text
  in the searched string
- findall() method will return the strings of every
  match in the searched string
