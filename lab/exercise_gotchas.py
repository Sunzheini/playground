"""
| #  | Code                                                                      | Output            | Explanation                                                                   |
| -- | ------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------- |
| 1  | `a = [1,2,3]; b = a; b.append(4); print(a)`                               | `[1,2,3,4]`       | Lists are mutable. `b` and `a` point to the same object.                      |
| 2  | `def f(x=[]): x.append(1); return x; print(f()); print(f())`              | `[1] [1,1]`       | Mutable default arguments are shared between calls.                           |
| 3  | `funcs = [lambda x: x+i for i in range(3)]; print([f(0) for f in funcs])` | `[2,2,2]`         | Lambdas capture `i` by reference, not value. Fix: `lambda x, i=i: x+i`.       |
| 4  | `a=[1,2,3,4]; b=a[:2]; print(a)`                                          | `[1,2,3,4]`       | Slicing creates a copy; original list unchanged.                              |
| 5  | `a=1000; b=1000; print(a is b)`                                           | `False`           | Python caches small integers `-5…256`. Larger integers are different objects. |
| 6  | `x=5; print(1<x<10)`                                                      | `True`            | Python supports chained comparisons `(1<x) and (x<10)`.                       |
| 7  | `x=None; print(x==None); print(x is None)`                                | `True True`       | `is` is preferred for checking `None`. `==` can be overridden.                |
| 8  | `a=0; b=10; print(a and b); print(a or b)`                                | `0 10`            | `and` returns first falsy value, `or` returns first truthy value.             |
| 9  | `for i in range(3): pass else: print("Done")`                             | `Done`            | `else` executes if loop completes normally (no `break`).                      |
| 10 | `print(0.1 + 0.2 == 0.3)`                                                 | `False`           | Floating-point precision issue. Use tolerance: `abs(0.1+0.2-0.3)<1e-10`.      |
| 11 | `a=[1,2]; b=a; b=[3,4]; print(a)`                                         | `[1,2]`           | Reassigning `b` makes it point to a new object; `a` unchanged.                |
| 12 | `a=(1,2); b=(1,2); print(a is b)`                                         | `True` or `False` | Small tuples may be cached; larger tuples are different objects.              |
| 13 | `print([]==False); print([] is False)`                                    | `False False`     | Empty list is falsy in condition but not equal to `False`.                    |
| 14 | `x = "hello"; y = "hello"; print(x is y)`                                 | `True`            | Python interns short strings; `is` may be `True`.                             |
| 15 | `a = [1,2]; b = a.copy(); print(a is b); print(a==b)`                     | `False True`      | `.copy()` creates a new object with same values.                              |
"""
