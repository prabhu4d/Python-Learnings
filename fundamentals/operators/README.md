# Operators

Operators are used to manipulate data and values

## Unary

- postive `+x`
- negative `-x`
- negation `not x`
- bitwise invert `~x`
- deletion `del x`
- call `x()`
- `assert x`
- spalt operator `*args, **kwargs`

## Binary

- Assignment `x = y`
- Attribute Access `x.y`
- Attribute Deletion `del x.y`
- Index `x[y]`
- Index Deletion `del x[y]`
- Logical
  - And `x and y`
  - Or `x or y`

### Arithmetic Binary

- Addition `x + y`
- Subtraction `x - y`
- Multiplication `x * y`
- Division `x / y`
- Floor Division `x // y`
- Modulo `x % y`
- Exponential `x ** y`
- Bitwise
  - And `x & y`
  - Or `x | y`
  - Xor `x ^ y`
- Shift
  - Left `x << y`
  - Right `x >> y`
- In-Place `x op=y`

### Comparision Binary

- Equality `x == y`
- Not Equal `x != y`
- Less Than `x < y`
- Less Than or Equal `x <= y`
- Greater Than `x > y`
- Greater Than or Equal `x >= y`
- Containment `x in y`
- Not-Containment `x not in y`
- Identify Test `x is y`
- Not Identify Test `x is not y`

## Ternary

- Ternary Assignment `x = y = z`
- Attribute Assignment `x.y = z`
- Index Assignment `x[y] = z`
- Ternary Compare `x < y < z`
- Ternary Or `x if y else z`

---

## Definitions

- Composable operators are called **Expressions**. it doesn't take entire single line
- Not Composable operators are called **Statement**. a single line of execution
