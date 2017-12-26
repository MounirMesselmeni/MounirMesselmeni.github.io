Title: Ordering a python list -> the simple way
Date: 2017-03-01 19:28
Category: Python
Tags: Python
Summary: A small simple guide on how to order Python list for different types
Keywords: python
          python list
          list
          sorting
          python sorting
          ordering
          ordering list
          list of strings
          list of string
          list of int
          list of integer
          list of dictionnary
          list of objects


Python is an easy, readable and simple language, many new python programmer will not know how to order/sort a python list.

I will demonstrate some simple examples on how to order different type of list. You will realize how simple it's.

## A list of integer

There are two ways to do so, using the [sort method of the list][4] object or using python builtin method [sorted][3]. The main difference is that the list's sort method will change the list, but sorted will creates a new list from the old and returns the new one will.

```python

  In [1]: my_list1 = [4, 8, 0, 3, 7, 2]

  In [2]: my_list1.sort()

  In [3]: my_list1
  Out[3]: [0, 2, 3, 4, 7, 8]

  In [4]: my_list2 = [4, 8, 0, 3, 7, 2]

  In [5]: sorted(my_list2)
  Out[5]: [0, 2, 3, 4, 7, 8]

  In [6]: my_list2
  Out[6]: [4, 8, 0, 3, 7, 2]
```

## A list of characters or strings

This apply the same to a list of strings or characters which will be ordered by the ascii code of the first characters. But pay attention that it will be case-sensitive sorting, to do so we have to use the key parameter to define what the sorting should be based on.

```python

  In [1]: my_list1 = ['z', 'Da', 'dC', 'b', 'a']

  In [2]: my_list1.sort()

  In [3]: my_list1
  Out[3]: ['Da', 'a', 'b', 'dC', 'z']

  In [4]: my_list1.sort(key=str.lower)

  In [5]: my_list1
  Out[5]: ['a', 'b', 'Da', 'dC', 'z']

  In [6]: my_list2 = ['z', 'Da', 'dC', 'b', 'a']

  In [7]: sorted(my_list2, key=str.lower)
  Out[7]: ['a', 'b', 'Da', 'dC', 'z']
```

## A list of dictionnary based on value

Here we need to use [lambda functions][1], there are some other way like using [attrgetter][2] from the builtin operator module from python but I prefer lambda as they are inline and more readable (in this case)

```python

  In [1]: my_list1 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]

  In [2]: my_list1.sort(key=lambda x: x['age'])

  In [3]: my_list1
  Out[3]: 
  [{'age': 20, 'name': 'Anna'},
   {'age': 25, 'name': 'Tom'},
   {'age': 50, 'name': 'John'}]

  In [4]: my_list2 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]

  In [5]: sorted(my_list2, key=lambda x: x['age'])
  Out[5]: 
  [{'age': 20, 'name': 'Anna'},
   {'age': 25, 'name': 'Tom'},
   {'age': 50, 'name': 'John'}]
```

## A list of object based on some attribute

Here we need can also to use [lambda functions][1], it's very similar to the dictionnary ordering but instead of accessing the dictionnary per key we will access the object attribute

```python

  In [1]: class Person(object):
     ...:     def __init__(self, name, age):
     ...:         self.name = name
     ...:         self.age = age

  In [2]: my_list1 = [Person(name='Tom', age=25), Person(name='John', age=50), Person(name='Anna', age=20)]

  In [3]: my_list1.sort(key=lambda x: x.age)

  In [4]: my_list1
  Out[4]: 
  [<__main__.Person at 0x7fa49abdaf50>,
   <__main__.Person at 0x7fa49abda590>,
   <__main__.Person at 0x7fa49abda250>]
```

## Reverse a list or order a list in a descending order

Both of the method we used (list.sort and sorted) support a boolena parameter called reverse, when set to `True` the order will be descending.

```python

  In [1]: my_list1 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]

  In [2]: my_list1.sort(key=lambda x: x['age'], reverse=True)

  In [3]: my_list1
  Out[3]: 
  [{'age': 50, 'name': 'John'},
   {'age': 25, 'name': 'Tom'},
   {'age': 20, 'name': 'Anna'}]

  In [4]: my_list2 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]

  In [5]: sorted(my_list2, key=lambda x: x['age'], reverse=True)
  Out[5]: 
  [{'age': 50, 'name': 'John'},
   {'age': 25, 'name': 'Tom'},
   {'age': 20, 'name': 'Anna'}]
```

## Reverse a list without sorting it

We have the same logic between [list.sort][4] and [sorted][3] as for list.reverse and reversed, **EXCEPT that reversed return a listreverseiterator object instead of a list**.

```python

  In [1]: my_list1 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]

  In [2]: my_list1.reverse()

  In [3]: my_list1
  Out[3]: 
  [{'age': 20, 'name': 'Anna'},
   {'age': 50, 'name': 'John'},
   {'age': 25, 'name': 'Tom'}]

  In [4]: my_list2 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]

  In [5]: list(reversed(my_list2))
  Out[5]: 
  [{'age': 20, 'name': 'Anna'},
   {'age': 50, 'name': 'John'},
   {'age': 25, 'name': 'Tom'}]

  In [6]: my_list2
  Out[6]: 
  [{'age': 25, 'name': 'Tom'},
   {'age': 50, 'name': 'John'},
   {'age': 20, 'name': 'Anna'}]
```

I used casted the return of the reversed as I mentioned above that it's returned result is not a list but an iterator. I recommend to cast the return of reversed if you will not just iterate over it or to use list comprehension.

```python

  In [1]: my_list2 = [dict(name='Tom', age=25), dict(name='John', age=50), dict(name='Anna', age=20)]
  In [2]: reversed(my_list2)
  Out[3]: <listreverseiterator at 0x7fe9508b5b50>
```

If you are new to Python and you don't know about such kind of usage, I beleive you will wonder how great it's to use such a cool language. All the examples were simple and there are plenty of other ways to do each of them, some could be more efficient regarding performance when dealing with larger list's elements and some could be more readable, I took the most simple ways I'm aware of.

Best luck!


[1]: https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
[2]: https://docs.python.org/3/library/operator.html#operator.attrgetter
[3]: https://docs.python.org/3.6/library/functions.html#sorteds
[4]: https://docs.python.org/3.6/library/stdtypes.html?highlight=list.sort#list.sort