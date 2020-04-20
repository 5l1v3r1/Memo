# Memo
Tiny cache decorator

## Installation
```
python3 setup.py install
```

## Example
``` 
from memo import Memo

@Memo()
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))
```
Output:
```
Cache: [1]
Cache: [1, 2]
Cache: [1, 2, 6]
Cache: [1, 2, 6, 24]
Cache: [1, 2, 6, 24, 120]
120
```
