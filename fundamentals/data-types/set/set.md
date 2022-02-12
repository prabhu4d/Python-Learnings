# Set

- Sets are unordered containers of unique values

s = {1, 2, 3}

t = {3, 4, 5}

| Operation | Meaning                                       | Example         |
| --------- | --------------------------------------------- | --------------- |
| s \| t    | Union                                         | {1, 2, 3, 4, 5} |
| s & t     | Intersection                                  | {3}             |
| s - t     | Difference - elements is s but not in t       | {1, 2}          |
| s ^ t     | Symmetric difference - elements not in s or t | {1, 2, 4, 5}    |
| s < t     | Strict subset                                 | False           |
| s <= t    | Subset                                        | False           |
| s > t     | Strict superset                               | False           |
| s >= t    | Superset                                      | False           |

### Hashing

